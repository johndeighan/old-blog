Using PostCSS with Svelte
=========================

You should either have no `svelte.config.js` file, or
have a valid one

Execute:

```bash
npx svelte-add@latest postcss
```

This will:

1. Add postcss, postcss-load-config, svelte-preprocess
	and autoprefixer as dependencies in your
	`package.json` file

2. Create or modify your `svelte.config.js` file.

3. Create the file `src/app.postcss` to which you
	can add global styles (if you had an app.css file,
	it will be removed, but styles it contained will
	appear in the app.postcss file)

4. Create the file `postcss.config.cjs` for configuring PostCSS.

The first thing we'll do is to convert `postcss.config.cjs` to modern
(i.e. ES6) JavaScript syntax. Rename the file to `postcss.config.js` and
change its current contents:

```js
const autoprefixer = require("autoprefixer");

const config = {
  plugins: [autoprefixer],
};

module.exports = config;
```

to ES6 syntax:

```js
import autoprefixer from 'autoprefixer';

export default {
	plugins: [autoprefixer],
	};
```

Next, you must run `npm install` to install the new
dependencies.

You can now use PostCSS syntax in a svelte file by
using:

```html
<style lang="postcss">
	...styles
</style>

Install a PostCSS plugin
------------------------

Search for plugins on the page `https://www.postcss.parts/`
(e.g. postcss-preset-env and postcss-color-function)

1. Install the plugin, e.g.:

```
$ npm install -D postcss-preset-env postcss-color-function
```

In your `postcss.config.js` file, import and use the plugin, e.g.:

```js
import autoprefixer from 'autoprefixer';
import presetEnv from 'postcss-preset-env'
import colorFunction from 'postcss-color-function'

export default {
	plugins: [
		autoprefixer({}),
		presetEnv({stage: 1}),
		colorFunction({}),
		],
	};
```

Examples:
=========

This will now work in Svelte:

In the file `src/app.postcss`, define custom media queries
and some color variables

```css
@custom-media --narrow (width < 800px);
@custom-media --wide   (width >= 800px);

:root {
	--theme-color: green;
	--light-theme-color: color(green tint(50%));
	--dark-theme-color:  color(green shade(50%));
	}
```

Then in a `*.svelte` file, you can do this:

```svelte
<style lang="postcss">
	form {
		& button {
			background-color: var(--theme-color);
			border-radius: 5px;
			cursor: pointer;

			&:hover {
				background-color: var(--light-theme-color);
				}

			@media (--wide) {
				& {
					color: black;
					}
				}
			@media (--narrow) {
				& {
					color: white;
					}
				}
			}
		}
</style>
```

