OpenLayers - Open source GIS library
====================================

Begin with a starter project

Install with:

```bash
$ npm install ol
```

To get a basic application, modify `routes/+page.svelte`:

```svelte
<h1>Open Layers Tutorial</h1>
<p>Click on the map to see coordinates</p>

<div bind:this={targetElem} class="map"></div>

<p bind:this={popupElem}>
	{defined(coords) ? coords : ''}
</p>

<script lang="coffee">
	import {onMount} from 'svelte'
	import {undef, defined} from '@jdeighan/base-utils'
	import Map from 'ol/Map.js'
	import Overlay from 'ol/Overlay.js'
	import OSM from 'ol/source/OSM.js'
	import TileLayer from 'ol/layer/Tile.js'
	import VectorLayer from 'ol/layer/Vector.js'
	import View from 'ol/View.js'

	targetElem = undef
	view = undef
	map = undef
	popupElem = undef
	coords = undef

	onMount () =>
		view = new View {
			center: [0,0]
			zoom: 2
			minZoom: 2
			maxZoom: 6
			enableRotation: true
			rotation: 0    # in radians
			}
		map = new Map {
			target: targetElem
			view
			layers: [
				new TileLayer({
					source: new OSM()
					})
				]
			}
		overlay = new Overlay {
			element: popupElem
			position: undef   # initially hidden
			positioning: 'center-left'
			}
		map.addOverlay overlay
		map.addEventListener 'click', (evt) =>
			coords = evt.coordinate
			console.log "click at #{coords}"
			overlay.setPosition coords
</script>

<style lang="postcss">
	div.map {
		width: 800px;
		height: 600px;
		}
</style>
```
