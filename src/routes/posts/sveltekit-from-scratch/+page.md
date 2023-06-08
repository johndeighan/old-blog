SvelteKit from scratch
======================

Start a new project:

```bash
$ mkdir myapp
$ cd myapp
$ mkdir static test src src/routes src/lib
```

Create a bare `package.json` file. Use whatever indentation
character(s) you prefer on the 2nd line. It will be preserved.
I prefer using a TAB character:

```json
{
	}
```

Next, install some needed packages by executing:

```bash
$ npm install -D vite svelte @sveltejs/kit @sveltejs/adapter-auto @sveltejs/adapter-static
```

You need to install an **adapter** to (eventually) deploy your app
to the Internet. We've installed 2 common adapters here. You'll need
to choose between them, though you can easily change it later.
For now, just use this rule: if your app will require
access to a database, you'll need to use `adapter-auto`. If, on the other
hand, you use only data which is inside your app, you can use
`apapter-static`, which will prerender all of your web pages, allowing
the server on which you host your app to only serve static files.

Your `package.json` file will now have a `devDependencies` section.
Do not modify anything in the `devDependencies` section, but
add these sections above the `devDependencies` section:

```json
	"name": "@jdeighan/myapp",
	"version": "1.0.0",
	"type": "module",
	"author": "John Deighan",
	"license": "MIT",
	"scripts": {
		"dev": "vite dev",
		"build": "vite build",
		"preview": "vite preview"
		},
```

NOTE:

1. You can name your project whatever you want. To make sure
	the name is unique, I use the convention '@' + my GitHub
	user name + '/' + a descriptive name.

2. `author` should, of course, be your name

3. I like the MIT license. You might want to look up the meaning
	of various software licenses on the Internet.

Create a vite config file
-------------------------

Name it `vite.config.js`, put in root directory:

```coffeescript
import {sveltekit} from '@sveltejs/kit/vite';

export default {
	plugins: [sveltekit()]
	};
```

Create a svelte config file
-------------------------

Name it `svelte.config.js`, put in root directory:

```coffeescript
import adapter from '@sveltejs/adapter-static';

export default {
	kit: {
		adapter: adapter()
		}
	};
```

But you'll have to use the adapter that you chose above in
the import statement.

Install a favicon file
-----------------------------------------

Find one, then place it in the `static/` directory. The web site
[here](https://www.favicon.cc/) will allow you to create a
custom icon. This is not absolutely necessary, but will prevent
an error message in your browser's console when debugging. Note the
file extension of the favicon - the file is commonly named `favicon.ico`,
`favicon.png` or `favicon.svg`, but other extensions are possible.

Create the file `src/app.html`
------------------------------

Put it in your `src/` directory:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<link rel="icon" href="%sveltekit.assets%/favicon.ico" />
		<meta name="viewport" content="width=device-width" />
		%sveltekit.head%
	</head>
	<body>
		<div>
			%sveltekit.body%
		</div>
	</body>
</html>
```

Change the file extension of the linked favicon file to match the
file extension of the file you used above.

Create a home page
------------------

Create the file `src/routes/+page.svelte`:

```svelte
<h1>Home Page</h1>
```

If you are using `adapter-static`, the create the file
`src/routes/+layout.js`. If you're using `adapter-auto`,
skip this step:

```js
export const prerender = true;
```

This is necessary because we're using `adapter-static` and this
tells svelte that all pages should be pre-rendered.

Test out the web site
---------------------

```bash
$ npm run dev -- --open
```

With the `-- --open` on the command line, a browser tab will automatically
be created and displayed. While you're developing your web site, if you
already have a browser tab open, you can just leave that off.

You should try modifying your `src/routes/+page.svelte` file. For now,
restrict yourself to entering plain HTML. You'll notice that when you
make a change and save the file, your web page updates immediately.

Set up source code management with git
--------------------------------------

Either stop the dev server for now or open a new tab in your
shell (I use Microsoft Terminal. You can use a CMD shell, bash shell,
or whichever shell you prefer.

Create the file `.gitignore` in your root directory:

```text
.DS_Store
node_modules
/build
/.svelte-kit
/package
.env
.env.*
!.env.example
vite.config.js.timestamp-*
vite.config.ts.timestamp-*
```

Create the file `.npmrc` in your root directory:

```text
engine-strict=true
loglevel=silent
```

Create the file `README.md` in your root directory:

```markdown
About this web site
===================

Describe your web site here
```

Execute these commands:

```bash
$ git init
$ git status
```

The 2nd command will show you the files that will be committed
to source code control. Because of the `.gitignore` file, this
should NOT include anything in the `node_modules` or `.svelte-kit`
folders. After verifying that, execute:

```bash
$ git add -A
$ git commit -m "initial commit"
$ git branch -M main
```

We've renamed the main branch to `main` instead of the default
`master`. That's considered politically correct these days.

You may also want to continue with some of the following additional steps:

1. [Set up global styles](/posts/sveltekit-global-styles#top)
2. [Enable using CoffeeScript everywhere](/posts/sveltekit+coffee#top)
3. Save your project to GitHub
4. Publish your project to npm
5. [Enable using PostCSS](/posts/postcss#top)


