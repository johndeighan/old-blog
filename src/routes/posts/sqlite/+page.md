Use SQLite from SvelteKit
=========================

For now, I'm going to keep things simple and access the
database from the main JavaScript thread. However,
that means that if you execute a long-running query,
responses to things like mouse clicks and key presses
will not work while the query is executing. Here is a
solution using a WebWorker to execute the query, which
runs in a separate thread and therefore does not suffer
from this problem:

`https://hartenfeller.dev/blog/sveltekit-offline-sqlite-1`

SQLite CLI Commands:
--------------------

`.tables` - list all tables in db
`.schema <table>` - display schema of given table
`.quit` - close SQLite CLI

Simple Setup
------------

First, set up a SvelteKit project with CoffeeScript

Install a SQLite lib:

```bash
$ npm install better-sqlite3
```

Create a SQLite database `src/<name>.db`, or download
the sample database `chinook.db` from
`https://www.sqlitetutorial.net/sqlite-sample-database/`
and put it in your `src/` folder.

Create a `*.coffee` file in your `src/lib` folder
to access the database, e.g.:

```coffee
```
