<nav>
	<a href="/">Home</a>
	<a href="/about">About</a>
	<a href="/contact">Contact</a>
	<a href="/posts">Blog Posts</a>
</nav>

<main>
  <slot/>
</main>

<footer>
	Programmed by John Deighan
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
		padding: 3px;
		}

	nav {
		grid-area: top;
		}
	nav a {
		text-decoration: none;
		padding: 12px 14px;
		display: inline-block;
		}
	nav a:hover {
		color: white;
		}

	footer {
		grid-area: bottom;
		}
</style>
