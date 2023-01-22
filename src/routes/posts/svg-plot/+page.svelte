<h1>Plotting with SVG</h1>

<SVGPlot {hPlot} {lPoints} {scaler}/>

<script>
	import {getPtScaler} from './GraphLib.js';
	import SVGPlot from './SVGPlot.svelte';

	let width = 700;
	let height = 300;
	let hPlot = {width, height};

	let lPoints = [
		[  0,   0],
		[ 50,  50],
		[100, 100],
		[150, 150],
		[200, 200],
		];

	let scaler = getPtScaler(width, height, lPoints);
</script>
