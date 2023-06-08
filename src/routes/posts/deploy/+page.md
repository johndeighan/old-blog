Deploy to the Internet
======================

Create the file `src/routes/+layout.server.coffee`:

```coffee
export prerender = true
```

That will cause all of our pages to be rendered at build time,
which is what the adapter-static requires.
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

