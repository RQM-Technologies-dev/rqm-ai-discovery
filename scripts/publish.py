"""Publish a reviewed GitHub commit to the exact public static HF Space."""
import json
import subprocess
import sys
from pathlib import Path
from validate import ROOT


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()


def main():
    from huggingface_hub import HfApi
    subprocess.run([sys.executable, str(ROOT / 'scripts/build.py'), '--check'], check=True)
    subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests'], cwd=ROOT, check=True)
    if git('status', '--porcelain'):
        raise SystemExit('Commit and review changes before publication.')
    sha = git('rev-parse', 'HEAD')
    remote = git('ls-remote', 'origin', 'refs/heads/main').split()[0]
    if sha != remote:
        raise SystemExit('Publish only the exact commit already on GitHub main.')
    record = json.loads((ROOT / 'content/record.json').read_text())
    repo = record['space'].removeprefix('https://huggingface.co/spaces/')
    owner = repo.split('/')[0]
    api = HfApi()  # Existing HF_TOKEN or authenticated HF cache; never print credentials.
    identity = api.whoami()
    allowed = identity.get('name', '').casefold() == owner.casefold()
    allowed |= any(o.get('name', '').casefold() == owner.casefold()
                   and o.get('roleInOrg') in ('admin', 'write') for o in identity.get('orgs', []))
    if not allowed:
        raise SystemExit('Authenticated account lacks verified publishing access to the planned namespace.')
    api.create_repo(repo_id=repo, repo_type='space', space_sdk='static', private=False, exist_ok=True)
    info = api.repo_info(repo_id=repo, repo_type='space')
    if info.private or getattr(info, 'sdk', None) != 'static':
        raise SystemExit('Existing destination is not a public static Space; review without changing it.')
    files = list((ROOT / 'site').iterdir())
    if any(not p.is_file() or p.is_symlink() for p in files):
        raise SystemExit('Unexpected file or symlink in publication folder.')
    commit = api.upload_folder(repo_id=repo, repo_type='space', folder_path=str(ROOT / 'site'),
                               commit_message=f'Mirror reviewed GitHub source {sha}',
                               parent_commit=info.sha)
    print(json.dumps({'space': record['space'], 'source_commit': sha, 'hf_commit': commit.oid}))


if __name__ == '__main__':
    main()
