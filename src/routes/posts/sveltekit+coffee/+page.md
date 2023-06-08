Set up CoffeeScript for SvelteKit
=================================

First, you need a SvelteKit project. You can follow my
[instructions for setting up SvelteKit from scratch](/posts/sveltekit-from-scratch#top)
or you can use the standard installer [here](https://kit.svelte.dev/).

Enabling CoffeeScript for SvelteKit entails 2 major changes:

1. Whenever you need a JavaScript file, instead create a
	CoffeeScript file. Then ensure that whenever the project
	is built or run, all CoffeeScript files have been converted
	to JavaScript. The CoffeeScript file will remain as a
	`*.coffee` file, but in the same directory, there will be
	a corresponding *.js file.

2. Add a preprocessor to Svelte that will allow you to add
	a script section in a Svelte file as `<script lang="coffee">`
	and to put CoffeeScript code into the script section.
	A way will be provided to include reactive statements
	and blocks.

Step 1: Enabling `*.coffee` files
=================================

Install the coffeescript npm package, and npm-run-all
to allow running commands concurrently:

```bash
$ npm install -D coffeescript npm-run-all
```

Next, you should make some changes to your `package.json` file:

1. Make sure the setting `"type": "module"` is there. SvelteKit
	normally adds it automatically. It allows you to use ES6
	syntax, which I always do. Among other things, it allows
	you to use ES6 import and export statements.

2. Do not, under any circumstances, make any changes in sections
	named `dependencies` or `devDependencies`. The `npm` command
	manages these automatically.

3. Make the following change to the `"scripts"` section:

Mine, as initially set up by SvelteKit, was:

```json
	"scripts": {
		"dev": "vite dev",
		"build": "vite build",
		"preview": "vite preview"
	},
```

Change that to:

```json
	"scripts": {
		"coffee:watch": "npx coffee -c -w .",
		"vite:dev": "vite dev",
		"dev": "npx coffee -c . && run-p coffee:watch vite:dev",
		"build": "npx coffee -c . && vite build",
		"preview": "vite preview"
		},
```

I can't anticipate how future versions of SvelteKit might
set up the initial `"scripts"` section, which is why I included
my original one above. If they change it, you'll need to use
your own judgement on the needed changes. But keep in mind:

1. I've added a `coffee:watch` script to compile any `*.coffee`
	files in the project to `*.js` files. I want the coffee
	command to keep watching for further changes, i.e. the
	command does not terminate. That's why the `dev` command
	needs to use the `run-p` command (added when you installed
	the npm-run-all package) to run that command concurrently
	with the `vite:dev` command, which also does not terminate.

To test things out, we're going to convert 2 config files to
CoffeeScript files, plus create a library file containing
utility functions that we'll utilize from our web page.

The standard SvelteKit `vite.config.js` file is:

```js
import { sveltekit } from '@sveltejs/kit/vite';

const config = {
	plugins: [sveltekit()]
};

export default config;
```

The CoffeeScript version of that is:

```coffee
import {sveltekit} from '@sveltejs/kit/vite'

export default {
	plugins: [sveltekit()]
	}
```
Save that as `vite.config.coffee`.

The SvelteKit standard `svelte.config.js is:

```js
import adapter from '@sveltejs/adapter-static';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter()
	}
};

export default config;
```

NOTE: the comment containing `@type` is for TypeScript, which
I don't use. So, I'll remove it in the CoffeeScript version.
If you use TypeScript, you'll want to keep it. Also, if you
followed the `SvelteKit from scratch` instructions, you will
be using `adapter-static`. Just keep whichever adapter is
currently set up in this file.

The CoffeeScript version is:

```coffee
import adapter from '@sveltejs/adapter-static'

export default {
	kit: {
		adapter: adapter()
		}
	}
```

Make sure it's using the adapter that you chose earlier.

Save that as `svelte.config.coffee`.

A few notes about CoffeeScript. It uses indentation to indicate
program structure, so the indentation must be includes. You
can use either TAB characters (my preference) or spaces, but
you must be consistent. Because program struction is indicated
by indentation (as in the Python language), no semicolons are
required, though if you include them, it's OK. When defining
a literal object, the curly braces are not required, but I prefer
including them to make it clear what you're creating (without the
curly braces, CoffeeScript knows what you're creating from the
`<key>: <value` syntax of object properties). When defining
a literal object, if each `<key>: <value>` pair is on a separate
line, the commas at the end of each is also not required. Similar
rules apply when defining literal arrays.

You can now remove the `vite.config.js` and `svelte.config.js` files
because they will be regenerated from the corresponding `*.coffee`
files. This is not required, but we want to test that everything is
working properly.

Another thing that we'd like to test is automatic conversion of
`*.coffee` library files to `*.js` files. This next step is not
required, it just allows us to test this feature.

Add this file as `src/lib/utils.coffee`:

```coffee
export spaces = (n) =>

	return " ".repeat(n)

export centeredText = (text, width) =>

	totSpaces = width - text.length
	if (totSpaces <= 0)
		return text
	numLeft = Math.floor(totSpaces / 2)
	numRight = totSpaces - numLeft
	return spaces(numLeft) + text + spaces(numRight)
```

This implements a simple function named `centeredText()` that will
center a string within a field of a given width. We'll use it on
our Home Page within a `<pre>` tag, since whitespace is not
significant anywhere else in an HTML document.

Test it out
-----------

Stop your current development server with Ctrl-C if it's
still running. Then, re-run the development server with:

```bash
$ npm run dev
```

If your web page is still open in your browser, it will probably
refresh by itself. If not, just refresh it manually. If it's
not open, open a new tab and browse to `localhost:5173`.
You should now check that:

1. The files `svelte.config.js` and `vite.config.js` now exist
	in your project directory.

2. The file `utils.js` now exists in your `src/lib` directory.

3. If you make a change to `src/routes/+page.svelte`, the web
	page in the browser immediately updates.

Use the utility library
-----------------------

Change the file `src/routes/+page.svelte` to:

```svelte
<h1>Home Page</h1>

<pre>
{'='.repeat(42)}
{centeredText('A title', 42)}
{'='.repeat(42)}
</pre>

<script>
	import {centeredText} from '$lib/utils.js';
</script>
```

Note the following: The code inside the `<script>` section is still
JavaScript, not CoffeeScript. We'll fix that next. Also, note the use
of the `$lib` alias provided by Svelte for the directory `src/lib`.
You can find plenty of tutorials on Svelte itself, so I'm not going
to try to teach it to you, but note that in the markup, you can put
any JavaScript expression inside `{` and `}` and it will be interpreted
and the result placed on the web page.

You should see something like this, with the words 'Home Page' in
large, bold text:

```text
Home Page

==========================================
                 A title
==========================================
```

Support CoffeeScript on Svelte pages
====================================

Install the npm package @jdeighan/svelte-utils:

```bash
$ npm install -D @jdeighan/svelte-utils
```

Now, change your `svelte.config.coffee` file to:

```coffee
import adapter from '@sveltejs/adapter-static'
import {coffeePreProcessor} from '@jdeighan/svelte-utils/preprocessors'

export default {
	kit: {
		adapter: adapter()
		}
	preprocess: {
		script: coffeePreProcessor
		}
	}
````
Make sure the adapter matches the adapter you're using.

After this change, you will be able to change your
`src/routes/+page.svelte` file to:

```svelte
<h1>Home Page</h1>

<pre>
{'='.repeat(width)}
{centeredText('A title', width)}
{'='.repeat(width)}
</pre>

<script lang="coffee">
	import {centeredText} from '$lib/utils.js'
	width = 42
</script>
```

Note that without the `lang="coffee"`, you would get an error
message because the variable `width` is not declared. CoffeeScript
does not require, nor allow you to declare variables.

Reactive statements and blocks
------------------------------

There are 2 types of reactive statements supported:

```coffee
$: fullName = firstName + ' ' + lastName
```

and:

```coffee
#reactive fullName = firstName + ' ' + lastName
```

The first is intended to resemble a standard Svelte JavaScript reactive
statement, but in CoffeeScript format. The second is what I call a
`command`. In a syntax I'm currently working on, if the first
non-whitespace character on a line is '#', you might be looking at a
comment or you might be looking at a command. The difference depends
on the character immediately following the '#'. If it's a whitespace
character (including a newline, i.e. where the line ends at the '#'),
it's a comment. Otherwise, it's a command. But there is a limited set
of commands and I envision them all consisting of '#' followed by
an identifier.

There are 2 types of reactive blocks supported:

```coffee
$:
	x = 2 * y
	console.log "x becomes #{x}"
```

and:

```coffee
#reactive
	x = 2 * y
	console.log "x becomes #{x}"
```

The reactive block consists of all following lines that are indented
further than the initial line, except that a blank line does NOT
terminate the block.

Test it out
-----------

Change your `src/routes/+page.svelte` file to:

```svelte
<h1>Home Page</h1>

<input type="number" min="0" bind:value={width}/>

<pre>
{'='.repeat(width)}
{centeredText('A title', width)}
{'='.repeat(width)}
</pre>

<p>{message}</p>

<script lang="coffee">
	import {centeredText} from '$lib/utils.js'
	width = 42
	$: message = "The width is #{width}"
</script>
```

You can now change the width of the `<pre>` section dynamically,
and not only does the section itself update automatically, the message
that's printed also updates automatically thanks to the reactive
statement introduced by `$:`. You can try making additional changes
to the home page, including changing the reactive statement to a
reactive block, or replacing `$:` with `#reactive`.

It did just occur to me that there is still something that I consider
a problem. In the markup (i.e. main HTML section), within curly braces
(i.e. `{` and `}`), I'm still forced to write JavaScript expressions,
not CoffeeScript expressions. For now, I'll leave it that way but
it's something to think about.
