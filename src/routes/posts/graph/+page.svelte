<h1>A sample graph</h1>

<svg width={hGraph.width} height={hGraph.height}>
	<Xaxis {hGraph} {xScale} label={hData.xLabel} lTicks={lXticks}/>
	<Yaxis {hGraph} {yScale} label={hData.yLabel} lTicks={lYticks}/>
	{#each hData.lPoints as h}
		<circle cx={xScale(h.cases)}
		        cy={yScale(h.deaths)}
		        r="5"
		        fill="purple"
		        stroke="black"
		        />
	{/each}
</svg>

<script>
	import {getScale, adjustedData} from './GraphLib.js';
	import {hData} from './CovidData.js';
	import Xaxis from './Xaxis.svelte';
	import Yaxis from './Yaxis.svelte';

	let hGraph = {
		width: 700,
		height: 300,
		leftPad: 30,
		rightPad: 5,
		topPad: 5,
		bottomPad: 15,
		}

	let {lPoints, xRange, yRange} = hData

	let xScale = getScale(
		[xRange.min, hGraph.leftPad],
		[xRange.max, hGraph.width - hGraph.rightPad],
		)
	let yScale = getScale(
		[yRange.min, hGraph.height - hGraph.bottomPad],
		[yRange.max, hGraph.topPad],
		)

	let lXticks = [100000, 200000, 300000, 400000, 500000];
	let lYticks = [500, 1000, 1500, 2000, 2500, 3000, 3500];
</script>

<style>
	svg {
		background-color: rgb(217, 238, 225);
		margin: 5px 40px;
		}
</style>
