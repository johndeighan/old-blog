<h1>Covid-19 Statistics</h1>
<p>
	Data from <a href="https://disease.sh">https://disease.sh</a>.
	(multiple sources, including Johns Hopkins, New York Times, Apple,
	various governments, etc.)
	" / 1M" means "per one million people"
</p>

{#await promise}
	<p>...waiting</p>
{:then lData}
	<table border="1">
	<tr>
		<th colspan="2"></th>
		<th colspan="2">Just Today</th>
		<th colspan="3">Over the Pandemic</th>
	</tr>
	<tr>
		<th>Country</th>
		<th>Population</th>
		<th>Cases</th>
		<th>Deaths</th>
		<th>Cases / 1M</th>
		<th>Deaths / 1M</th>
		<th>Total Deaths</th>
	</tr>
	{#each lData as h}
		<tr>
			<td>{mapCountry(h.country)}</td>
			<td class="number">{h.population}</td>
			<td class="number">{h.todayCases}</td>
			<td class="number">{h.todayDeaths}</td>
			<td class="number">{h.casesPerOneMillion}</td>
			<td class="number">{h.deathsPerOneMillion}</td>
			<td class="number">{h.deaths}</td>
		</tr>
	{/each}
	</table>

	<!-- pre>{JSON.stringify(lData, null, 3)}</pre -->
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}

<script>
	const mapCountry = (country) => {
		switch (country) {
			case 'Syrian Arab Republic':
				return 'Syria';
			case 'Lao People\'s Democratic Republic':
				return 'Lao PDR';
			case 'Libyan Arab Jamahiriya':
				return 'Libya';
			case 'Saint Vincent and the Grenadines':
				return 'St. Vincent';
			case 'Falkland Islands (Malvinas)':
				return 'Falkland Islands';
			case 'Holy See (Vatican City State)':
				return 'Vatican City';
			default:
				return country;
			}
		}

	async function getData() {
		const url = 'https://disease.sh/v3/covid-19/countries'
		const resp = await fetch(url);
		const lData = await resp.json();
		lData.sort((a,b) => {
			if (a.population > b.population) {
				return -1;
				}
			else {
				return 1;
				}
			});

		if (resp.ok) {
			return lData;
			}
		else {
			throw new Error('failed');
			}
		}

	let promise = getData();
</script>

<style>
	.number {
		text-align: right;
		}
</style>
