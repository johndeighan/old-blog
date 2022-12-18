<svg {width} {height}>
	{#each lScaled as pt,i}
		<circle cx={pt[0]} cy={pt[1]} r="6" fill=black/>
		{#if i > 0}
			<line x1={lScaled[i-1][0]} y1={lScaled[i-1][1]} x2={pt[0]} y2={pt[1]} style="stroke:rgb(8, 112, 177);stroke-width:2" />
		{/if}
	{/each}
</svg>

<script>
	import {getScaledPoints} from './GraphLib.js';

	export let hPlot;    // describes the plot - width, height
	export let lPoints;  // data to be plotted [x, y]
	export let scaler;   // function to convert data pt => SVG pt

	let {width, height} = hPlot;
	let lScaled = getScaledPoints(lPoints, scaler);
</script>

<style>
	svg {
		background-color: lightBlue;
		border: 1px solid black;
		margin: 5px 40px;
		}
</style>
