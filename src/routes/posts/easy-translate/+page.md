Enable easy language translation
================================

What we're going to do here is to utilize 2
unicode characters to delimit strings in our
markup that we want translated. These 2
characters are:

```text
«   Unicode 00AB
»   Unicode 00BB
```

The plan is to take any text enclosed within
these 2 quote marks, e.g.:

```html
<h1>«Hello, World!»</h1>
```

and convert that to:

```html
<h1>{translate('Hello, World!')}</h1>
```

Care will need to be taken so that if the enclosed
string contains any characters that need to be escaped,
e.g. single or double quotation marks, that they are
properly escaped in the output string.

NOTE: With this system in place, you'll be entering these 2
unicode characters often in your markup. To make that
painless, you'll want to set up your editor to emit these
characters with a keyboard combination. I'm not going
to cover that here. But I will suggest using the keyboard
combinations `Ctrl-<` and `Ctrl->` as being very intuitive.

Note that it is the responsibility of the user of this
feature to provide a working `translate()` function. In
our case, it will utilize the set language, which is stored
in the variable `lang`, and we'll need to ensure that if
that variable is changed, the translate() function is
re-executed.

To make this happen, we'll set up a svelte preprocessor.
You can find a description [here](https://svelte.dev/docs#compile-time-svelte-preprocess).

First, let's add a utility function that takes a string of any
length and searches for these characters. Add this function
to your `src/lib/utils.coffee` file:

```coffee
export mapForTranslation = (block) =>

	replacer = (match, str) =>
		return "{translate('#{str}')};

	return block.replace(/\u00AB(.*?)\u00BB/g, replacer)
```

You might have noticed that we're making no attempt to escape internal
quote characters. That's because we'll first set up unit tests for this
function, make sure it works in simple cases, then create unit tests
for more complex cases, which will fail, but allow us to fix the problem
in the mapForTranslation() function until the test passes.

Set up unit tests
=================

I use the `ava` package for unit testing, so we'll need to install
that globally first if you haven't already:

```bash
$ install -g ava
```

Next, install the npm package `@jdeighan/unit-tester`:

```bash
$ npm install -D @jdeighan/unit-tester
```

Next, we'll set up an `export` in our `package.json` file to allow
importing our `utils.js` library for use in our unit tests. Add this
section to your `package.json` file:

```json
	"exports": {
		"./utils": "./src/lib/utils.js",
		"./package.json": "./package.json"
	},

While you're in the `package.json` file, we also need to add
a script to invoke our unit tests. Add this script:

```json
		"test": "cls && coffee -c . && ava ./test/*.test.js"
```

I like to clear the screen first with the `cls` command, but
you can remove that if you want.

Now, we can put this unit test file into our `test` folder.
Name it `translate.test.coffee`:

```coffee
import {utest} from '@jdeighan/unit-tester'
import {mapForTranslation} from '@jdeighan/myapp/utils'

utest.equal 4, mapForTranslation("""
	<h1>«Hello, World!»</h1>
	"""), """
	<h1>{translate('Hello, World!')}</h1>
	"""
```

Now, when you run the command `npm test`, you will see that the
unit test passes:

```bash
$ npm test
 ✔ line 4
  ─

  1 test passed
```

The unit tests are identified by line number, so you don't have to
come up with a name for each test. As long as the line numbers
supplied are correct, it's easy to locate a failing unit test in
your unit test files. In fact, let's create a failing unit test now!
Add this test to your `test/translate.test.coffee` file:

```coffee
utest.equal 10, mapForTranslation("""
	<h1>«Hello, 'John'!»</h1>
	"""), """
	<h1>{translate('Hello, \\'John\\'!')}</h1>
	"""
```

It basically says that if a single quote (aka apostrophe) appears
between the special quote marks, it needs to be escaped in the
replacement string. Now, if we run out unit tests, we get:

```bash
$ npm test
  ✔ line 4
  ✖ line 10
  ─

  line 10

  Difference:

  - '<h1>{translate(\'Hello, \'John\'!\')}</h1>'
  + '<h1>{translate(\'Hello, \\\'John\\\'!\')}</h1>'

  › file:///node_modules/@jdeighan/unit-tester/src/UnitTester.js:222:29

  ─

  1 test failed
```

That's easily fixed in our mapForTranslation() function, which becomes:

```coffee
export mapForTranslation = (block) =>

	replacer = (match, str) =>
		str = str.replace(/'/g, "\\'")
		return "{translate('#{str}')}"

	return block.replace(/\u00AB(.*?)\u00BB/g, replacer)
```

Now, our unit tests both pass. Now, let's try using a string that spans
multiple lines and contains multiple strings to translate. Add this
unit test:

```coffee
utest.equal 16, mapForTranslation("""
	<h1>«Hello, 'John'!»</h1>
	<div>
		«Today is Christmas!»
	</div>
	<div>
		«Merry Christmas!»
	</div>
	"""), """
	<h1>{translate('Hello, \\'John\\'!')}</h1>
	<div>
		{translate('Today is Christmas!')}
	</div>
	<div>
		{translate('Merry Christmas!')}
	</div>
	"""
```

```bash
$ npm test
  ✔ line 4
  ✔ line 10
  ✔ line 16
  ─

  3 tests passed
```

That test also passes. Time to use the `mapToTranslation()` function
in a svelte preprocessor.

Place the following file, named `translatePreProcessor`, in the
`src/lib` folder:

```coffee
# translatePreProcessor.coffee

import {mapForTranslation} from './utils.js'
import {parse, walk} from 'svelte/compiler'

# ---------------------------------------------------------------------------

export translatePreProcessor = () =>

	return {
		markup: ({content, filename}) ->
			return {
				code: mapForTranslation(content)
				}
		}
```

Next, we'll actually use this preprocessor in the `svelte.config.coffee`
file:

```coffee
```

