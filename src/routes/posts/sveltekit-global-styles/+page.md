SvelteKit Global Styles
=======================

The best way to have global styles in SvelteKit is to have a
file named `global.css` and place it in your `src/lib`
folder. In SvelteKit you can directly import a CSS file. You
can do that in your `src/routes/+layout.svelte` file. For
example, here is a sample `global.css` file:

```css
:root {
	--bkg-color: GhostWhite;
	--text-color: Black;
	--menu-bkg-color: #09CABE;
	--menu-text-color: Black;
	height: 100vh;
	width: 100vw;
	margin: 0;
	padding: 0;
	}
html, body {
	height: 100vh;
	width: 100vw;
	margin: 0;
	padding: 0;
	}
* {
	box-sizing: border-box;
	}
```
This is a great place to **reset** CSS properties, and to
define CSS variables. To import that in your layout file,
create the file `src/routes/+layout.svelte`:

```js
<slot/>

<script>
	import '$lib/global.css'
</script>
```

If this `+layout.svelte` file is your only layout file,
it will apply to your entire web site, so this is all
you need. If, however, you have layout files that override
your main layout file, you'll have to remember to import
your global style file there also.
