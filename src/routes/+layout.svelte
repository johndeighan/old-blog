<nav>
	<a href="/">Home</a>
	<a href="/about">About</a>
	<a href="/contact">Contact</a>
</nav>

<main>
  <slot/>
</main>

<footer>
	Built with SvelteKit!
</footer>

<style>
	main {
		grid-area: middle;
		padding: 15px 5px;
		overflow: auto;    /* scroll bars appear with large content */
		background-color: var(--bkg-color);
		color: var(--text-color);
		}
	nav, footer {
		background-color: var(--menu-bkg-color);
		color: var(--menu-text-color);
		text-align: center;
		margin: 0;
		padding: 5px 0;
		}
	nav {
		grid-area: top;
		}
	nav a {
		color: var(--menu-text-color);
		text-decoration: none;
		padding: 0 8px;
		display: inline-block;
		}
	nav a:hover {
		color: white;
		}
	footer {
		grid-area: bottom;
		}
</style>
