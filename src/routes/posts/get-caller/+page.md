Getting a function's caller in JavaScript
=========================================

Hint: It's not easy

To get a function's caller in JavaScript, you'll need to:

1. Create an Error object. Apparently, in some older
	browsers you need to actually throw an exception,
	then catch it. Fortunately, I only work with
	modern browsers.

2. Access the `stack` property of the Error object.
	It is a long string with each line having information
	about one stack frame.

3. Parse that string. Its format varies across
	browsers, and most disappointing is that instead of
	having access to the information itself, you can only
	get this string, which must then be parsed to get
	the information in it.

4. There is a default limit of 10 stack frames. If you
	anticipate having more than that, you'll need to
	modify the limit.

I've written a library, installable via npm, that will
get you the information you need. However, since there's
no standard being followed here, this library only works
with V8 based browsers (Chrome and Edge), and also for nodejs since it's
since it's based on the V8 engine. Install it with:

```bash
npm install @jdeighan/base-utils
```

CAVEAT: I'm currently working on this functionality. So, until
you can get at least version 1.0.11 of this library, what's
described on this page won't work.

After that, you can import 3 useful functions:

```js
import {
	getV8Stack, getMyDirectCaller, getMyOutsideCaller,
	} from '@jdeighan/base-utils/v8-stack'
```

`getV8Stack()` will get you the entire call stack. It will
include functions called within the library itself. You can
pass a maxDepth as an integer - the default value is Infitity.
Unless you need the entire call stack, it's generally better
to use one of the following 2 functions.

`getMyDirectCaller()` will get you the stack frame for the
function that called the function containing the call to this
function. It might or might not be in the same file as the
function containing the call to `getMyDirectCaller()`.

`getMyOutsideCaller()` will get you the stack frame for the
most recent function that resulted in a function being
invoked that exists in the same source file as the function
that contains the call to `getMyOutsideCaller()`. Let me
illustrate why that's useful:

I have a logging library that allows you to call various
logging functions, e.g.:

`LOG <something>` to just log out a string

`LOGVALUE <label>, <value>` to log out an arbitrary
	data structure along with a label

`LOGTAML <label>, <value>` to log out a nicer formatted
	complex data structure

In that library, there's also a function named `PUTSTR()`.
Calls to the functions above ultimately result in calls to
`PUTSTR()` which actually outputs text to the logs. What
I'd like to do is to have the logs stored locally in the
library, but with attached information letting me know from
which outside JavaScript file that call originated. So, e.g.,
in PUTSTR() I can ask for information about the caller, but
I don't want to know the direct caller, which will be another
function in the logging library, but the next function in
the call stack that is NOT the logging library. With
`getMyOutsideCaller()` I can do that.

Rather than listing out the fields available in the data
structure returned by `getMyDirectCaller()` or
`getMyOutsideCaller()`, and in the array returned by
`getV8Stack()`, I'll just show it to you. The fields should
be self-explanatory:

```js
{
   "type": "function",
   "source": "/C:/Users/johnd/base-utils/test/temp.js",
   "funcName": "func1",
   "depth": 3
   "isAsync": false,
   "hFile": {
      "root": "/",
      "dir": "/C:/Users/johnd/base-utils/test",
      "base": "temp.js",
      "ext": ".js",
      "name": "temp",
      "lineNum": 20,
      "colNum": 10
   },
}
```

type can be 'function', 'method' or 'file'
keys 'source' and 'hFile' will always be there
if type is 'method', there will also be an 'objName' key
