Responsive Images
=================

```svelte
<div>
	<image href="some url"/>
	<image href="some url"/>
	<image href="some url"/>
	...etc.
</div>

<style>
	div {
		width: 100%;
		display: grid;
		gap: 1rem;
		grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
		}
</style>
