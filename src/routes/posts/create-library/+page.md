Create npm installable library
==============================

Make sure `nodejs` and `git` are installed globally.
Make sure the npm package `ava` is installed globally.

```bash
$ mkdir newlib
$ cd newlib
$ mkdir src test
$ npm init -y
$ npm install -D coffeescript
```

Change your `package.json` file to:

```json
{
	"name": "@jdeighan/newlib",
	"version": "1.0.0",
	"type": "module",
	"description": "A collection of svelte preprocess functions",
	"engines": {
		"node": ">=12.0.0"
	},
	"exports": {
		"./package.json": "./package.json"
	},
	"scripts": {
		"build": "cls && coffee -c .",
		"test": "npm run build && ava ./test/*.test.js && git status"
	},
	"keywords": [
		"coffeescript",
		"svelte"
	],
	"author": "John Deighan",
	"license": "MIT",
	"devDependencies": {
		"coffeescript": "^2.7.0"
	}
}
```

NOTE: In the 'name' field, I've pre-pended the name of my new
library ('newlib') with my GitHub user name and a '/' character.
You should use your GitHub user name (or something else to guarantee
that the name will be unique). CoffeeScript should already be
installed, so it will appear in the 'devDependencies' section,
which you should NOT modify.

Add a library file
------------------

So far, we just have an empty library. Next, let's add a library
file along with some unit tests and make it importable by
users of the library.

Add this file to the `src/` folder:

```coffee
# utils.coffee

export centeredText = (text, width) =>

	totSpaces = width - text.length
	numLeft = Math.floor(totSpaces / 2)
	numRight = totSpaces = numLeft
	return spaces(numLeft) + text + spaces(numRight)
```

This library exports just a single, simple function. Hopefully,
your library will be a bit more complex.

Next, we'll edit the `package.json` file to add this library as
an export. Change the 'exports' section to:

```json
	"exports": {
		"./utils": "./src/utils.js",
		"./package.json": "./package.json"
	},
```

You'll notice that even though we manually only edit the *.coffee
file, we export the "*.js" file so that users of our library do
not need to install CoffeeScript to use our library.

Whenever we add a new source file to our library, we need to add
a corresponding unit test. Normally, if a library is named
`newlib.coffee`, the corresponding unit test is named
`newlib.test.coffee` and placed in the `test/` folder.

We will use `ava` for unit testing, so next we need to
install that package:

```bash
$ npm install -D ava
```

Then, add this unit test file, named `utils.test.coffee`
to the `test/` folder:

```coffee
# utils.test.coffee

import test from 'ava'
import {centeredText} from '@jdeighan/newlib/utils'

test "center text", (t) =>
	t.is(centeredText('hello', 11), '   hello   ')
```

Notice how you import your library in exactly the same way that
a user of your library would import it, using the name of your
project, followed by the sub-path from the `exports` section of
your `pacakge.json` file.

You can now run your unit test with this command:

```bash
$ npm run test
```

Initialize Git in your folder
-----------------------------

Make sure that your project folder is the "current directory".

```bash
$ git init
```

Create a `.gitignore` file:

```text
logs/
node_modules/
typings/
*.tsbuildinfo
.npm

# dotenv environment variables file
.env
.env.test

test/temp*.*
```

Enter the command `git status` and make sure that neither the
node_modules folder nor anything inside it appears as something
to be committed. Once you verify that, execute these commands:

```bash
$ git add -A
$ git commit -m "initial commit"
$ git branch -m "main"
```

Current best practices say that you should name your main branch `main`
and not the default `master`.

Store the library on GitHub
---------------------------

Follow the directions [HERE](/posts/push-to-github)

Publish the library to npm
-------------------------

1. Make sure you have an npm account
2. Log in to your npm account

Then:

```bash
$ npm publish
```
