self.addEventListener('install', (e) => {
  console.log('Service Worker Installato');
});

self.addEventListener('fetch', (e) => {
  // Questo permette all'app di caricare i file
  e.respondWith(fetch(e.request));
});
