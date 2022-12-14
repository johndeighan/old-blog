<!-- svelte:head>
	<script src="https://unpkg.com/jquery@3.6.0/dist/jquery.js"/>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.js"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqPlot/1.0.9/jquery.jqplot.min.css">
</svelte:head -->

<div bind:this={plot}/>

<script>
	import {onMount} from 'svelte';
	import jQuery from 'jquery';
	export let title="Title", xlabel="X label", ylabel="Y label";
	export let hilite=false;

	let plot;

	onMount(() => {
		// --- We need to create the plot here
		console.log('starting...');
		jQuery.jqplot(plot, [[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]]);
		});
</script>

<style>
	div {
		width: 400px;
		height: 300px;
		background: lightGray;
		}
</style>
