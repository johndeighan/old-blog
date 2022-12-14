{#if label}
	<a href="/posts/{name}">{label}</a>
{:else}
	<a class="capitalize" href="/posts/{name}">{name}</a>
{/if}

<script>
	export let name;
	export let label = '';
</script>

<style>
	a {
		text-decoration: none;
		display: block;
		padding: 3px 20px;
		font-size: 18px;
		}
	a.capitalize {
		text-transform: capitalize;
		}
</style>
