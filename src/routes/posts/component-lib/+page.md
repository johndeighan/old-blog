Create a Svelte Component Library
=================================

First, create a SvelteKit project:

```bash
$ npm create svelte@latest components
$ cd components
$ npm install
$ git init && git add -A && git commit -m "initial commit"
$ npm run dev -- --open
```

1. Choose `Library Skeleton Project`
2. Choose TypeScript (it seems to be needed for packaging)
2. No ESLint, Prettier, etc.

Change file `src/routes/+page.svelte` to:

```svelte
<h1>My Components</h1>
```

Note the immediate change to the web page.

Make project name unique
------------------------

In your `package.json` file, is a `name` key, set to
the name of your project. You should make it unique by
pre-pending your GitHub name, e.g.:

```js
	"name": "@jdeighan/components",
```

that way, when you publish the project to npm, the name
will be almost guaranteed to be unique.

At the same time, I would change the version number
to "1.0.0" - I don't support any version numbers below
that.

Add a Button component
----------------------

Add the file `Button.svelte` to your src/lib folder:

```svelte
<button>
	<slot/>
</button>

<style>
	button {
		font-size: 18pt;
		font-family: sans-serif;
		background-color: lightBlue;
		}
</style>
```

Add import and export to `src/lib/index.js`:

```js
import Button from './Button.svelte';

export {Button};
```

Change the file `src/routes/+page.svelte` to:

```svelte
<h1>My Components</h1>

<Button>
	Press me
</Button>

<script>
	import {Button} from '$lib/index.js';
</script>
```

The button on your web page will:

1. have a light blue background
2. have 18 point text
3. use a sans-serif font (the header will have serifs)
4. pressing it won't do anything - we'll work on that later

Build and Deploy the component library
--------------------------------------

Build your library with:

```bash
$ npm run build
```

This will create a directory named `package` containing all
of the files that need to be published. You can publish that
to npm via:

```bash
$ npm publish ./package
```

Using the component library
---------------------------

You can then use the components in any other project you
have by simply installing the component library:

```bash
$ npm install @jdeighan/components
```

Then inside any svelte file:

```svelte
<Button>
	Click me
</Button>

<script>
	import {Button} from '@jdeighan/components';
</script>
