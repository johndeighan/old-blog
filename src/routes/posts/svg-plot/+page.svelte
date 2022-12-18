<h1>Plotting with SVG</h1>

<SVGPlot {hPlot} {lPoints} {scaler}/>

<script>
	import SVGPlot from './SVGPlot.svelte';
	import {getScaler} from './GraphLib.js';

	let width = 700;
	let height = 300;
	let hPlot = {width, height};

	let lPoints = [
		[  0,   0],    // lower left
		[ 50,  50],
		[100, 100],   // mid point
		[150, 150],
		[200, 200],  // upper right
		];

	let scaler = getScaler(width, height, lPoints);
</script>
