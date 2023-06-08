import {build, files, version} from '$service-worker'

# --- Create a unique cache name for this deployment
CACHE = "cache-#{version}"

ASSETS = [
	build...    # the app itself
	files...    # everything in `static`
	]

self.addEventListener 'install', (event) =>
	# --- Create a new cache and add all files to it
	addFilesToCache = () ->
		cache = await caches.open(CACHE)
		await cache.addAll(ASSETS)

	event.waitUntil(addFilesToCache())

self.addEventListener 'activate', (event) =>
	# --- Remove previous cached data from disk
	deleteOldCaches = () ->
		for key of await caches.keys()
			if (key != CACHE)
				await caches.delete(key)

	event.waitUntil deleteOldCaches()

self.addEventListener 'fetch', (event) =>
	# --- ignore POST requests etc
	if (event.request.method != 'GET')
		return

	respond = () ->
		url = new URL(event.request.url)
		cache = await caches.open(CACHE)

		# --- `build`/`files` can always be served from the cache
		if (ASSETS.includes(url.pathname))
			return cache.match(event.request)

		# --- for everything else, try the network first, but
		#     fall back to the cache if we're offline
		try
			response = await fetch(event.request)

			if (response.status == 200)
				cache.put event.request, response.clone()

			return response
		catch err
			return cache.match(event.request)

	event.respondWith(respond())
