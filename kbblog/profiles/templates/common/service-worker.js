const PRE_CACHE_NAME = 'cache_storage_image';

const urlsToCache = [
  'static/common/images/profile.jpg',
  'static/common/images/background.jpg',
  'static/profiles/images/inavi.jpg',
  'static/profiles/images/samsung.jpg',
  'static/profiles/images/skinfood.jpg',
];

// self: keyword => service-worker object
const _ = self;

_.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(PRE_CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
      .then(() => _.skipWaiting()),
  );
});

_.addEventListener('activate', () => {
});

_.addEventListener('fetch', (e) => {
  console.log('fetch: ', e.request);
  e.respondWith(
    caches.match(e.request)
      .then((response) => {
        if (response) return response;
        return fetch(e.request);
      }),
  );
});
