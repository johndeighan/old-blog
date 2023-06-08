npm bin files
=============

In your `package.json` file, you can have a 'bin' key.
For example:

```json
	"bin": {
		"hello": "./src/bin/sayHello.js"
		},
```

NOTE: The file `./src/bin/sayHello.js` should have this as
its first line:

```text
#!/usr/bin/env node
```

A command named `hello` will become available. You can execute it with:

```bash
$ npx hello
```

(if the package is installed globally, omit the `npx`)

In addition, if your file is a CoffeeScript file, you can use this
`package.json` file:

```json
	"bin": {
		"hello": "./src/bin/sayHello.js",
		"goodbye": "./src/bin/sayGoodBye.coffee"
		},
```

The file `./src/bin/sayGoodBye.coffee` should have this as
its first line:

```text
#!/usr/bin/env coffee
```

The file can now be executed with:

```bash
$ npx goodbye
```
