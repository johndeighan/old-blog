Creating a node server
======================

Install `adapter-node`:
```bash
$ npm install -D @sveltejs/adapter-node
```

In your svelte config file, import this adapter:
```js
import adapter from '@sveltejs/adapter-node';
```

Environment Variables
---------------------

Create the file `.env` in your project folder, containing
any environment variables used by the app.

These env vars will be read by svelte in dev and preview mode.

Install `dotenv`:
```bash
$ npm install dotenv
```



Build the server
----------------

Execute:
```bash
$ npm run build
```

This will create a node server in the folder `build`

Run the app
-----------

```bash
$ node -r dotenv/config build
```
