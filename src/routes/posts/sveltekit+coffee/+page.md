Set up CoffeeScript for SvelteKit
=================================

First, create a SvelteKit project:

```bash
$ npm create svelte@latest myapp
$ cd myapp
$ mkdir src/lib src/test
$ npm install
$ npm run dev -- --open
```

Create a Skeleton Project with no add-ons whatsoever.

Change the file `src/routes/+page.svelte to:

```svelte
<h1>Hello</h1>
```

Notice that the web page updates immediately in the browser.

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

Install the coffeescript npm package globally and locally:

```bash
$ npm install -g coffeescript
$ npm install -D coffeescript
```

I believe it's also possible to only install coffeescript locally.
Since that's not how I do it, I'm a bit afraid
to tell you to do that since I haven't tested doing it that way.
My best guess is that you would have to change some of the
scripts in your `package.json` file from what I describe, possibly
utilizing the `npx` command since your system would not have the
`coffee` command available.

To allow running 2 or more commands concurrently, install the
`npm-run-all` package:

```bash
$ npm install -D npm-run-all
```

Next, you should make some changes to your `package.json` file:

1. The `name` should be unique in both the GitHub and npm
	systems. The way I ensure that is to use a name like
	`@<GitHub User Name>/<Descriptive Name>`. For example, I'm
	using the name `@jdeighan/sveltekit-coffee`. You should,
	of course, use your own GitHub user name - or anything else
	that you're sure won't cause a name conflict if you try to
	add your project to GitHub, npm or any other site you use to
	store your source code.

2. I prefer starting the version number at 1.0.0, but never
	releasing any version that's broken. It doesn't matter if
	the functionality is extremely limited as long as it correctly
	does what your README.md file says that it does.

3. If your `package.json` file includes the setting
	`"private": true`, you might want to remove that if you
	want your project to be accessible to the general public.
	There is a license field that can be added if you want to
	add some restrictions to the use of your project. I personally
	add the setting `"license": "MIT",`.

4. Make sure the setting `"type": "module"` is there. SvelteKit
	normally adds it automatically. It allows you to use ES6
	syntax, which I always do. Among other things, it allows
	you to use ES6 import and export statements.

5. Do not, under any circumstances, make any changes in sections
	named `dependencies` or `devDependencies`. The `npm` command
	manages these automatically.

6. Make the following change to the `"scripts"` section:

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
		"coffee": "coffee --compile --watch .",
		"vite:dev": "vite dev",
		"dev": "run-p coffee vite:dev",
		"build": "coffee -c . && vite build",
		"preview": "vite preview"
	},
```

I can't anticipate how future versions of SvelteKit might
set up the initial `"scripts"` section, which is why I
included my original one. If they change it, you'll need to
use your own judgement on the needed changes. But keep in mind:

1. I've added a `coffee` script to compile any `*.coffee` files
	in the project to `*.js` files. However, I want the coffee
	command to keep watching for further changes, i.e. the
	command does not terminate. That's why the `dev` command
	needs to use the `run-p` command (added when you installed
	the npm-run-all package) to run that command concurrently
	with the `vite:dev` command, which also does not terminate.

To test things out, we're going to convert 2 config files to
CoffeeScript files, plus create a library file containing
utility functions that we'll utilize from our web page.

The current contents of the file `vite.config.js` is:

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

The current contents of the file `svelte.config.js is:

```js
import adapter from '@sveltejs/adapter-auto';

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
If you use TypeScript, you'll want to keep it.

The CoffeeScript version of that is:

```coffee
import adapter from '@sveltejs/adapter-auto'

export default {
	kit: {
		adapter: adapter()
		}
	}
```

Next, we'll add a library of utility functions. Add this file
as `src/lib/utils.coffee`:

```coffee
export translate = (str, lang) =>

	switch str.toLowerCase()
		when 'hello'
			if (lang == 'zh') then return '你好'
			if (lang == 'es') then return 'Hola'
			if (lang == 'hi') then return 'नमस्ते'
		when 'what is your name', 'what is your name?'
			if (lang == 'zh') then return '你叫什么名字？'
			if (lang == 'es') then return '¿Cómo te llamas?'
			if (lang == 'hi') then return 'तुम्हारा नाम क्या हे?'
		when 'good morning'
			if (lang == 'zh') then return '早上好'
			if (lang == 'es') then return 'Buenos días'
			if (lang == 'hi') then return 'शुभ प्रभात'
		when 'good afternoon'
			if (lang == 'zh') then return '下午好'
			if (lang == 'es') then return 'Buenas tardes'
			if (lang == 'hi') then return 'नमस्कार'
		when 'good evening'
			if (lang == 'zh') then return '晚上好'
			if (lang == 'es') then return 'Buenas noches'
			if (lang == 'hi') then return 'सुसंध्या'
		when 'happy birthday'
			if (lang == 'zh') then return '生日快乐'
			if (lang == 'es') then return 'Feliz cumpleaños'
			if (lang == 'hi') then return 'जन्मदिन की शुभकामनाएं'
		when 'merry christmas'
			if (lang == 'zh') then return '圣诞节快乐'
			if (lang == 'es') then return 'Feliz navidad'
			if (lang == 'hi') then return 'क्रिसमस की बधाई'
		when 'happy new year'
			if (lang == 'zh') then return '新年快乐'
			if (lang == 'es') then return 'Feliz año nuevo'
			if (lang == 'hi') then return 'नए साल की शुभकामनाएँ'
		when 'today is my birthday'
			if (lang == 'zh') then return '今天是我的生日'
			if (lang == 'es') then return 'Hoy es mi cumpleaños'
			if (lang == 'hi') then return 'आज मेरा जन्मदिन हे'
		when 'today is christmas'
			if (lang == 'zh') then return '今天是圣诞节'
			if (lang == 'es') then return 'Hoy es navidad'
			if (lang == 'hi') then return 'आज क्रिसमस है'
		when 'today is new year\'s day'
			if (lang == 'zh') then return '今天是元旦'
			if (lang == 'es') then return 'Hoy es el día de año nuevo'
			if (lang == 'hi') then return 'आज नववर्ष का दिन है'
		when 'none of the preceding'
			if (lang == 'zh') then return '以上都不是'
			if (lang == 'es') then return 'Ninguno de los anteriores'
			if (lang == 'hi') then return 'पूर्व में से कोई नहीं'
		when 'none of the above'
			if (lang == 'zh') then return '以上都不是'
			if (lang == 'es') then return 'Ninguno de los anteriores'
			if (lang == 'hi') then return 'इनमे से कोई भी नहीं'
	return str
```

This implements a simple function named `translate()` that will
translate a few common English phrases to either Chinese or
Spanish.

Test it out
-----------

Remove the files `svelte.config.js` and `vite.config.js`. They
should be re-generated when we run our project. In general,
it's not necessary to remove any `*.js` files - they are just
overwritten by the CoffeeScript compiler. However, we're testing
things out and this will allow us to easily check if they
are created.

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
<div>
	<button on:click={() => lang='en'} class:select={lang=='en'}>
		I speak English
	</button>
	<button on:click={() => lang='es'} class:select={lang=='es'}>
		Yo hablo español
	</button>
	<button on:click={() => lang='zh'} class:select={lang=='zh'}>
		我说中文
	</button>
	<button on:click={() => lang='hi'} class:select={lang=='hi'}>
		मैं हिंदी बोलते हैं
	</button>
</div>

<div>
	<button on:click={() => today='birthday'} class:select={today=='birthday'}>
		{translate('Today is my birthday', lang)}
	</button>
	<button on:click={() => today='christmas'} class:select={today=='christmas'}>
		{translate('Today is Christmas', lang)}
	</button>
	<button on:click={() => today='new year'} class:select={today=='new year'}>
		{translate('Today is New Year\'s Day', lang)}
	</button>
	<button on:click={() => today=''} class:select={today==''}>
		{translate('None of the preceding', lang)}
	</button>
</div>

<h1>{translate('Hello', lang)}</h1>

{#if hour < 12}
	<h1>{translate('Good Morning', lang)}</h1>
{:else if hour < 18}
	<h1>{translate('Good Afternoon', lang)}</h1>
{:else}
	<h1>{translate('Good Evening', lang)}</h1>
{/if}

{#if today == 'birthday'}
	<h1>{translate('Happy Birthday', lang)}</h1>
{:else if today == 'christmas'}
	<h1>{translate('Merry Christmas', lang)}</h1>
{:else if today == 'new year'}
	<h1>{translate('Happy New Year', lang)}</h1>
{/if}

<script>
	import {translate} from '$lib/utils.js';
	lang = 'es';
	today = '';
	hour = new Date().getHours();
</script>

<style>
	button {
		font-size: 18px;
		padding: 3px;
		margin: 3px;
		background-color: lightGreen;
		font-family: sans-serif;
		}
	button.select {
		background-image: linear-gradient(rgba(0, 0, 0, 0.2) 0 0);
		}
</style>
```

Now, you've got a cool web page that supports 4 languages:
English, Chinese, Spanish and Hindi, and greets you appropriately.

Note that so far, on a *.svelte page, inside `<script>` tags,
you must put JavaScript - not CoffeeScript. We'll fix that next.

Support CoffeeScript on Svelte pages
====================================

Install my svelte/CoffeeScript preprocessor:

```bash
$ npm install -D @jdeighan/svelte-preprocess
```

Now, change your `svelte.config.coffee` file to:

```coffee
import adapter from '@sveltejs/adapter-auto'
import {coffeePreProcessor} from '@jdeighan/svelte-preprocess/coffee'

export default {
	kit: {
		adapter: adapter()
		}
	preprocess: {
		script: coffeePreProcessor
		}
	}
````

After this change, you will be able to change the `<script>` section
of `src/routes/+page.svelte` to be:

```svelte
<script lang="coffee">
	import {translate} from '$lib/utils.js'
	lang = 'es'
	today = ''
	hour = new Date().getHours()
</script>
```

Deploy to the Internet
======================

Create the file `src/routes/+layout.server.coffee`:

```coffee
export prerender = true
```

Next, you have to install the "static adapter":

```bash
$ npm install -D @sveltejs/adapter-static@latest
```

Next, modify your `svelte.config.coffee` file to:

```coffee
import adapter from '@sveltejs/adapter-static'
import {coffeePreProcessor} from '@jdeighan/svelte-preprocess/coffee'

export default {
	kit: {
		adapter: adapter()
		}
	preprocess: {
		script: coffeePreProcessor
		}
	}
```

Only the first line was changed. You can now build your web site
as a set of static HTML pages with:

```bash
$ npm run build
```

This should create a directory named `build` in your project
directory. To deploy it to the Internet, run:

```bash
$ surge ./build
```

Lastly, we'll try out creating reactive statements and
reactive blocks. There are 2 types of reactive statements supported:

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

To test this, change your `src/+page.svelte` file to:

```svelte
<div>
	<button on:click={() => lang='en'} class:select={lang=='en'}>
		I speak English
	</button>
	<button on:click={() => lang='es'} class:select={lang=='es'}>
		Yo hablo español
	</button>
	<button on:click={() => lang='zh'} class:select={lang=='zh'}>
		我说中文
	</button>
	<button on:click={() => lang='hi'} class:select={lang=='hi'}>
		मैं हिंदी बोलते हैं
	</button>
</div>

<div>
	<label>
		{translate('What is your name?', lang)}
		<input bind:value={name}>
	</label>
</div>

<h1>{helloMessage}{name?' ':''}{name}, {todayMessage}</h1>

<div>
	<label>
		<input type="radio" bind:group={today} value="birthday">
		{translate('Today is my birthday', lang)}
	</label>
</div>
<div>
	<label>
		<input type="radio" bind:group={today} value="christmas">
		{translate('Today is Christmas', lang)}
	</label>
</div>
<div>
	<label>
		<input type="radio" bind:group={today} value="new year">
		{translate('Today is New Year\'s Day', lang)}
	</label>
</div>
<div>
	<label>
		<input type="radio" bind:group={today} value="">
		{translate('None of the above', lang)}
	</label>
</div>

<h1>{dateMessageEx}</h1>

<script lang="coffee">
	import {translate} from '$lib/utils.js'
	lang = 'es'
	name = ''
	today = ''
	hour = new Date().getHours()

	#reactive helloMessage = translate('Hello', lang)

	$:
		switch today
			when 'birthday'
				dateMessage = translate('Happy Birthday', lang)
			when 'christmas'
				dateMessage = translate('Merry Christmas', lang)
			when 'new year'
				dateMessage = translate('Happy New Year', lang)
			else
				dateMessage = ''

	$: dateMessageEx = if dateMessage then dateMessage + '!' else ''

	#reactive
		if (hour < 12)
			todayMessage = translate('Good Morning', lang)
		else if (hour < 18)
			todayMessage = translate('Good Afternoon', lang)
		else
			todayMessage = translate('Good Evening', lang)

</script>

<style>
	div {
		font-size: 18px;
		margin: 4px;
		}
	button {
		font-size: 18px;
		padding: 3px;
		margin: 3px;
		background-color: lightGreen;
		font-family: sans-serif;
		}
	button.select {
		background-image: linear-gradient(rgba(0, 0, 0, 0.2) 0 0);
		}
</style>
```

This tests both types of reactive statement and both types of
reactive block.

It did just occur to me that there is still something that I consider
a problem. In the markup (i.e. main HTML section), within curly braces
(i.e. `{` and `}`), I'm still forced to write JavaScript expressions,
not CoffeeScript expressions. For now, I'll leave it that way but
it's something to think about.
