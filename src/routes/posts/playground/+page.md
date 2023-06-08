Set Up a Playground
===================

Create a standard web project with CoffeeScript, then:

```bash
$ npm install playground-elements
$ npm install -D coffeescript npm-run-all @web/dev-server
```

Create the file `web-dev-server.config.coffee` in your root folder:

```coffee
export default {
	port: 80
	watch: false
	nodeResolve: true
	rootDir: '.'
	}
```

Change the "scripts" section in `package.json` to:

```json
	"scripts": {
		"coffee:watch": "npx coffee -c -w .",
		"serve": "npx web-dev-server --config web-dev-server.config.js",
		"start": "cls && npx coffee -c . && run-p coffee:watch serve",
		"dev":   "npm start",
		"test":  "echo \"Error: no test specified\" && exit 1"
	},
```
Create file `index.html` in your root folder:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" href="/favicon.png" />
		<script
  			type="module"
			src="/node_modules/playground-elements/playground-ide.js">
		</script>
		<style>
			:root {
				/* see https://github.com/google/playground-elements/blob/main/README.md */
				--playground-code-background: white;
		  		--playground-code-font-size: 18px;
				}
			playground-ide {
				height: 100%;
				}
		</style>
	</head>
	<body>
		<playground-ide editable-file-system line-numbers resizable project-src="src/files.json">
		</playground-ide>
	</body>
</html>
```

