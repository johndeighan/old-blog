<h1>Plotting Data with jqPlot</h1>

<p>(if you don't see a graph, try refreshing the page)</p>

<JQPlot title = "Monthly Revenue & Profit"
        {hSeries} {hX} {hY} {hY2}
        />

<script>
	import JQPlot from './JQPlot.svelte';

	let hX = {
		label: "Month",
		format: "date",
		};
	let hY = {
		label: "Revenue",
		format: "$%'d",
		};
	let hY2 = {
		label: "Profit",
		format: "$%'d",
		};

	let lRevenue = [
		['2011-11-20', 800538],
		['2011-12-20', 804879],
		['2012-01-20', 847732],
		['2012-02-20', 795758],
		['2012-03-20', 835554],
		['2012-04-20', 844379],
		['2012-05-20', 828510],
		['2012-06-20', 753984],
		['2012-07-20', 807403],
		['2012-08-20', 755840],
		['2012-09-20', 775304],
		['2012-10-20', 781322],
		];
	let lProfit = [
		['2011-11-20', 192049],
		['2011-12-20', 188744],
		['2012-01-20', 197352],
		['2012-02-20', 190106],
		['2012-03-20', 193453],
		['2012-04-20', 197249],
		['2012-05-20', 205480],
		['2012-06-20', 177648],
		['2012-07-20', 193793],
		['2012-08-20', 183221],
		['2012-09-20', 192797],
		['2012-10-20', 182451],
		];

	let hSeries = {
		revenue: {
			hOptions: {
				xaxis: 'xaxis',
				yaxis: 'yaxis',
				},
			lData: lRevenue,
			},
		profit: {
			hOptions: {
				xaxis: 'xaxis',
				yaxis: 'y2axis',
				},
			lData: lProfit,
			},
		};
</script>

