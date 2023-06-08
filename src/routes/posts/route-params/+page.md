SvelteKit Route Parameters
==========================

In your `src/routes` folder, create a folder named `[page]`.
You can use any name you like (it should be descriptive), but
since I'm going to simulate creating pages like 'Home', 'About',
'Contact', 'Help', etc. to demo a menu system, my page will
be representing pages in an app.

Inside your new folder, create 2 files:

`+page.js`

```js
export const load = ({params}) => {

	let title = params.page
		.toLowerCase()
		.replace(/\b\w/g, (c) => c.toUpperCase())
		+ ' Page';
	return {
		title,
		content: `This is your ${title}`,
		}
	}
```

This exports a **load function**. The information in the returned
hash is available on the page that follows:

`+page.svelte`

```svelte
<h1>{title}</h1>

<p>{content}</p>

<script>
	export let data;
	let title, content;
	$: {
		title = data.title;
		content = data.content;
		}
</script>
```

The `data` set in the load function is available here in the
object named `data` (it must be exported). To simplify things,
we unpack that into variables named `title` and `content`, but
that must be done in a reactive block so that the variables are
recalculated every time the variable named `data` changes value.
