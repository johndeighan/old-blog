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

```bash
$ npm install -D vite svelte @sveltejs/kit @sveltejs/adapter-static
```

Your `package.json` file will now have a `devDependencies` section.
It may be slightly different than the one below (mainly in version
numbers). Do not modify anything in the `devDependencies` section, but
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

Install a favicon.ico or favicon.png file
-----------------------------------------

Find one, then place it in the `static/` directory. The web site
[here](URL 'https://www.favicon.cc/') will allow you to create a
custom icon.

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
	<body data-sveltekit-preload-data="hover">
		%sveltekit.body%
	</body>
</html>
```

Make sure that the favicon file extension in this file matches the
one in the actual file, i.e. in your `static` directory. Or for now,
you can simply remove the <link> element for the favicon file if you don't
want one.

Create a home page
------------------

Create the file `src/routes/+page.svelte`:

```svelte
<h1>Welcome</h1>
```

Test out the web site
---------------------

```bash
$ npm run dev -- --open
```

With the `-- --open` on the command line, a browser tab will automatically
be created and displayed. While you're developing your web site, if you
already have a browser tab open, you can just leave that off.

Set up source code management with git
--------------------------------------

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

Note that we're committing both the *.coffee and *.js files, even
though the *.js files are created from the original *.coffee files.
That's so that if a user of our project doesn't use, nor want to
use CoffeeScript, they can still use our project's *.js files.

We've also renamed the main branch to `main` instead of the default
`master`. That's considered politically correct these days.

You may also want to continue with some of the following additional steps:

1. [Enable using CoffeeScript everywhere](/posts/sveltekit+coffee#top)
2. Save your project to GitHub
3. Publish your project to npm
4. Enable using PostCSS


