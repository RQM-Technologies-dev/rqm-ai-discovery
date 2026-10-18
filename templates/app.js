'use strict';
const search = document.querySelector('#search');
const entries = [...document.querySelectorAll('.capability')];
search.addEventListener('input', () => {
  const query = search.value.trim().toLowerCase();
  let visible = 0;
  entries.forEach(entry => {
    const match = entry.dataset.search.toLowerCase().includes(query);
    entry.hidden = !match;
    if (match) visible += 1;
  });
  document.querySelector('#result-count').textContent = `${visible} ${visible === 1 ? 'service' : 'services'}`;
  document.querySelector('#empty').hidden = visible !== 0;
});
document.querySelector('#copy').addEventListener('click', async () => {
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(document.querySelector('#endpoint').textContent);
    status.textContent = 'Endpoint copied.';
  } catch {
    status.textContent = 'Select and copy the endpoint above. Clipboard access is unavailable.';
  }
});
