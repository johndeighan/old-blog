Modernizr
=========

Install globally:

```bash
$ npm install -g modernizr
```

Create file `modernizr.config.json` in your root folder:

```json
{
	"minify": true,
	"options": [
		"setClasses"
		],
	"feature-detects": [
		"test/webrtc/getusermedia"
		]
	}
```

Build the modernizr.js library:

```bash
$ modernizr -c ./modernizr.config.json -d ./static/modernizr.js
```

Now, in JavaScript, you can test for availability of the
getUserMedia() function with:

```js
if Modernizr.getusermedia
	...code
else
	...code
```

