<section>
	<nav>
		<a href="/">Home</a>
		<a href="/about">About</a>
		<a href="/contact">Contact</a>
	</nav>

	<main>
	  <slot/>
	</main>

	<footer>
		<span>Built with SvelteKit!</span>
	</footer>
</section>

<style>
	section {
		height: 100vh;
		width: 100vw;
		font: 15px sans-serif;
		display: grid;
		grid-template-areas:
			"left top    right"
			"left middle right"
			"left bottom right"
			;
		grid-template-rows: auto 1fr auto;
		}

	/* NOTE: Using a CSS variable in place of '800px' doesn't work */

	@media (max-width: 800px) {
		section {grid-template-columns: 0 100% 0;}
		}
	@media (min-width: 800px) {
		section {grid-template-columns: 1fr 800px 1fr;}
		}

	nav {
		grid-area: top;
		}
	main {
		grid-area: middle;
		padding: 15px 5px;
		overflow: auto;    /* scroll bars appear with large content */
		background-color: var(--bkg-color);
		color: var(--text-color);
		}
	footer {
		grid-area: bottom;
		}
	nav, footer {
		display: flex;
		gap: 1rem;
		flex-wrap: wrap;
		color: var(--menu-text-color);
		background-color: var(--menu-bkg-color);
		margin: 0;
		padding: 5px 0;
		}
	nav a {
		color: var(--menu-text-color);
		text-decoration: none;
		padding: 0;
		}
	nav a:hover {
		color: white;
		}
</style>
