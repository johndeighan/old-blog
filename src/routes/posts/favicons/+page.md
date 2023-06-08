Generate favicons
=================

First you need an SVG file (see `/posts/svg-edit`)
Place it in your `static/` folder. I named mine
`favicon.svg`.

```bash
$ npm install -D favicons
```

Create the file `src/bin/gen-favicons.coffee`:

```coffee
import favicons from 'favicons'
import fs from 'fs/promises'
import path from 'path'

# --- These are relative to the current working directory
src  = "static/favicon.svg"
dest = "static/favicons"     # should exist

# --- Configuration
hConfig = {
	path: "/favicons"
	appName: "My Great App"
	appShortName: "Great App"
	appDescription: "A great application"
	developerName: 'John Deighan'
	version: '1.0.0'
	icons: {
		android: true
		appleIcon: true
		appleStartup: true
		favicons: true
		windows: false
		yandex: false
		}
	files: {
		android: {
			manifestFileName: 'manifest.json'
			}
		}
	}

# --- Below is the processing.
{images, files, html} = await favicons(src, hConfig)

await Promise.all(
	images.map(
		(image) =>
			await fs.writeFile(path.join(dest, image.name), image.contents)
		)
	)

await Promise.all(
	files.map(
		(file) =>
			await fs.writeFile(path.join(dest, file.name), file.contents)
		)
	)

await fs.writeFile(path.join(dest, 'icons.html'), html.join("\n"))
```
