/* Privacy-friendly Vercel Web Analytics bootstrap and conversion signals. */
window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };

document.addEventListener('submit', function (event) {
  if (event.target && event.target.id === 'qform') {
    window.va('event', { name: 'Quote Request Started' });
  }
});

document.addEventListener('click', function (event) {
  var link = event.target && event.target.closest && event.target.closest('a[href^="tel:"]');
  if (link) window.va('event', { name: 'Phone Link Clicked' });
});
