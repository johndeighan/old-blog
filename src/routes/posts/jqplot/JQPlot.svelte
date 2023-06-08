<svelte:head>
	<!-- script src="https://unpkg.com/jquery@3.6.0/dist/jquery.js"/ -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"/>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.js"/>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/plugins/jqplot.dateAxisRenderer.min.js"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.css">
</svelte:head>

<div id="revenueChart" style="width: 600px"/>

<script>
	import {onMount} from 'svelte';
	import {undef, nonEmpty} from '@jdeighan/base-utils'
	import {getPlotOptions} from '$lib/PlotUtils.js';

	export let title = "Title";
	export let hSeries;
	export let hX = {label: 'X Axis'};
	export let hY = {label: 'Y Axis'};
	export let hY2 = undef;

	onMount(() => {
		let [lData, hOptions] = getPlotOptions(title, hSeries, hX, hY, hY2);
		console.log('lData:', lData);
		console.log('hOptions:', hOptions);
		jQuery.jqplot('revenueChart', lData, hOptions);
		});
</script>

<style>
	div {
		background: lightGray;
		margin: auto;
		}
</style>
