supabase
========

Create SvelteKit Project
------------------------

Follow instructions at [CoffeeScript from scratch](/posts/sveltekit-from-scratch#top)

Set up CoffeeScript
-------------------

Follow instructions at [Enable using CoffeeScript everywhere](/posts/sveltekit+coffee#top)

Set up supabase database
------------------------

 1. Create an account at supabase.com or log in if you have one
 2. Create a new project named 'todo'
 3. On the left, click on 'Table Editor'
 4. Click on 'Create a new table'
 5. Name the table 'todos'
 6. Turn off RLS for this project (you should normally use it)
 7. Keep the columns id and created_at
 8. Define additional columns:
	task: Text not nullable
	isCompleted: bool not nullable, default false
 9. Click on 'Save'
10. Click on '+ Insert row', add a couple of tasks

Set up access to supabase
-------------------------

Execute the following in your home directory:

```bash
$ npx apply supabase-community/svelte-supabase --no-ssh
$ npm install @supabase/supabase-js@latest
```

The first command does a lot of nice things for us, but unfortunately, it
installs an older version of supabase-js. The second statement installs
a newer version.

This will create a `.env` file in your project directory. You will
need to fill in some values in that file. For security reasons, you should:

1. Make sure that your `.gitignore` file contains `.env` on a line by
	itself. That way, your `.env` file, which contains things that you need
	to keep private, won't ever end up on a public server, e.g. GitHub.

2. Never put any keys you get from the `supabase.com` web site, any
	password, or anything else that you want to keep private, anywhere
	BUT your `.env` file.

Go back to supabase.com and:

1. Click on 'Settings' (gear icon), then 'API'
2. Copy the project URL into the `.env` file (`<your-supabase-url>`)
3. Copy the public key into the `.env` file (`your-supabase-public-key>`)
4. Copy the private key into the `.env` file (`your-supabase-private-key>`)
5. Copy the JWT secret into the `.env` file (`your-supabase-jwt-secret>`)
6. Restart the dev server if it's running because you changed the `.env` file.

Display the To Do List
----------------------

Create the file `src/lib/db.coffee`:

```coffeescript
import {createClient} from '@supabase/supabase-js'

db = createClient(
	import.meta.env.VITE_SUPABASE_URL,
	import.meta.env.VITE_SUPABASE_ANON_KEY,
	)

# ---------------------------------------------------------------------------

export getAllToDos = ()

	{data} = await db.from('todos').select('*')
	return data || []
```

All database operations that we'll use in our app will appear as
functions in this file. We don't export the database connection itself
in order to enforce that constraint. You can remove the file `src/lib.db.js`
if you wish since it will be overwritten anyway.

Create file `_page.server.coffee` in your `routes` folder:

```coffeescript
import {getAllToDos} from '$lib/db.js';

# ---------------------------------------------------------------------------

export load = () =>

	try
		lToDos = await getAllToDos()
		return {
			lToDos
			errorMsg: ''
			}
	catch error
		return {
			lToDos: []
			errorMsg: error.message
			}
```

Note that we're naming this file with a leading underscore. The JavaScript file
that it produces will need to have a leading '+' sign, not an underscore.
But if we name the `*.coffee` file with a leading '+' sign, Svelte will think
that it's a file it needs to render. So, we'll need to arrange that `*.js` files
with a leading underscore will need to be renamed. We can do that in our
`package.json` file with the following 2 changes:

add this script to the `scripts` section:

```json
		"rename": " mv ./src/routes/_page.server.js ./src/routes/+page.server.js",
```

and change the `dev` script to:

```json
		"dev": "npx coffee --compile . && npm run rename && run-p coffee:watch vite:dev",
```

Lastly, change your `src/routes/+page.svelte` to:

```svelte
<h1>Supabase To Do List</h1>

{#if data.errorMsg}
	<p class="error">ERROR: {data.errorMsg}</p>
{:else}
	{#each data.lToDos as {task,isComplete}}
		<div>
			<input type="checkbox" checked={isComplete}/>
			<input value={task}/>
			<button>Del</button>
		</div>
	{:else}
		<p>No To-Dos yet</p>
	{/each}
{/if}

<script>
	export let data;
</script>

<style>
	div {
		margin: 3px;
		}
	p.error {
		color: red;
		}
</style>
```

You can now execute the command `npm run dev` and see your todos appear
on your home page.

Make each to-do a component
---------------------------

