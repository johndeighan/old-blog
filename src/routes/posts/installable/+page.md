Make Web App Installable
========================

You will need an SVG icon. The easiest way to get one
is to visit `https://simpleicons.org/` and download one.
A good one to start with is the Svelte icon - simply search
for 'svelte' on the page and click on the download icon.

To create a unique icon, you can:
1. Modify the SVG code, e.g. by changing the color
2. Create your own icon - SVG is an HTML syntax and
	fairly easy to learn.

Place the SVG icon in the folder containing your static files.
Name it `favicon.svg`.

Add the file `manifest.json` to the folder containing
your static files:

```json
{
	"id": "starter",
	"name": "starter",
	"short_name": "starter",
	"start_url": "/",
	"scope": "/",
	"display": "standalone",
	"orientation": "any",
	"theme_color": "#00b1d1",
	"background_color": "#ffffff",
	"lang": "en",
	"dir": "ltr",
	"icons": [
		{
			"src": "favicon.svg",
			"sizes": "any",
			"type": "image/svg"
			}
		]
	}
```

[See this web page]
(https://developer.mozilla.org/en-US/docs/Web/Manifest)

In your main HTML file, add these links (you may need to adjust
the path to the files, depending on where you placed them):

```html
<link rel="icon" href="favicon.svg" />
<link rel="manifest" href="/manifest.json"/>
```

If using SvelteKit, use these instead:

```html
<link rel="icon" href="%sveltekit.assets%/favicon.svg" />
<link rel="manifest" href="%sveltekit.assets%/manifest.json"/>
```

If using SvelteKit, add the file `service-worker.js`
to your `src` folder, if not, place it in the same folder
as your main HTML page:

```js
/// <reference types="@sveltejs/kit" />
import { build, files, version } from '$service-worker';

// Create a unique cache name for this deployment
const CACHE = `cache-${version}`;

const ASSETS = [
    ...build, // the app itself
    ...files  // everything in `static`
];

self.addEventListener('install', (event) => {
    // Create a new cache and add all files to it
    async function addFilesToCache() {
        const cache = await caches.open(CACHE);
        await cache.addAll(ASSETS);
    }

    event.waitUntil(addFilesToCache());
});

self.addEventListener('activate', (event) => {
    // Remove previous cached data from disk
    async function deleteOldCaches() {
        for (const key of await caches.keys()) {
            if (key !== CACHE) await caches.delete(key);
        }
    }

    event.waitUntil(deleteOldCaches());
});

self.addEventListener('fetch', (event) => {
    // ignore POST requests etc
    if (event.request.method !== 'GET') return;

    async function respond() {
        const url = new URL(event.request.url);
        const cache = await caches.open(CACHE);

        // `build`/`files` can always be served from the cache
        if (ASSETS.includes(url.pathname)) {
            return cache.match(url.pathname);
        }

        // for everything else, try the network first, but
        // fall back to the cache if we're offline
        try {
            const response = await fetch(event.request);

            if (response.status === 200) {
                cache.put(event.request, response.clone());
            }

            return response;
        } catch {
            return cache.match(event.request);
        }
    }

    event.respondWith(respond());
});
```

Or, you can try the CoffeeScript version `service-worker.coffee`:

```coffeescript
import {build, files, version} from '$service-worker'

CACHE = "cache-#{version}"
ASSETS =  [
	build...,   # the app itself
	files...,   # everything else in static dir
	]

self.addEventListener 'install', (event) =>

	# --- create a new cache and add all files to it
	addFilesToCache = () =>
		cache = await caches.open(CACHE)
		await cache.addAll(ASSETS)

	event.waitUntil addFilesToCache()

self.addEventListener 'activate', (event) =>

	# --- remove previous cached data from disk
	deleteOldCaches = () =>
		for key of await caches.keys()
			if (key != CACHE)
				await caches.delete(key)

	event.waitUntil deleteOldCaches()

self.addEventListener 'fetch', (event) =>

	# --- ignore non-GET requests
	if (event.request.method != 'GET')
		return

	respond = () =>
		url = new URL(event.request.url)
		cache = await caches.open(CACHE)

		if (ASSETS.includes(url.pathname))
			return cache.match(event.request)

		try
			resp = await fetch(event.request)
			if (resp.status == 200)
				cache.put(event.request, resp.clone())
			return resp
		catch err
			return cache.match(event.request)

	event.respondWith(respond())
```

Test if your app is truly installable
-------------------------------------

Run your app locally in development mode, e.g. if using
SvelteKit:

```bash
$ npm run dev
```

View your web site in the Chrome browser

