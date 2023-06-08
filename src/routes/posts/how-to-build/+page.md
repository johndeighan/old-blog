Create a blog using SvelteKit
=============================

My inspiration
--------------

was the web page at:

```url
https://joshcollinsworth.com/blog/build-static-sveltekit-markdown-blog
```

First, scaffold a SvelteKit app:

(Actually, FIRST, make sure you have NodeJS and Git installed)

```bash
$ npm create svelte@latest blog
```

1. Choose a Skeleton Project
2. No TypeScript, ESLint, Prettier, etc.

```bash
$ cd blog
$ mkdir src/lib
$ npm install
$ git init && git add -A && git commit -m "initial commit"
$ npm run dev -- --open
```

The last command starts the "development server". We will
keep the development server running throughout this
tutorial. To enter any commands from this point on,
open a second terminal window.

Edit the src/routes/+page.svelte file - it's your home page:

```html
<h1>My Blog Posts</h1>

<p>My blog posts will go here eventually</p>
```

Observe the immediate change to the web site

Add Pages
---------

Add some directories and files to the src/routes folder:
e.g. src/routes/about/+page.svelte:

```html
<h1>About my blog</h1>

<p>I'm learning Svelte and SvelteKit</p>
```

and src/routes/contact/+page.svelte:

```html
<h1>Contact me</h1>

<p>Via email: john.deighan@gmail.com</p>

FYI, I almost never check this email address, but
I'm not ready to publish the email address that I actually use.
```

You should now be able to browser to any of
these URLs and see the new pages:

```url
http://localhost:5173/
http://localhost:5173/about
http://localhost:5173/contact
```

What we really want is to have a menu at the top
of the page with links for:

1. Our Home Page
2. Our About Page
3. Our Contact Page

So, next, let's investigate svelte layouts.

Svelte Layouts
==============

A file named +layout.svelte in the src/routes/ folder will act
as a layout file. That is, when you visit a page like your
'about' page using a URL like: `localhost:5173/about`, the page
+layout.svelte will actually be served, but on that page there
is an HTML `<slot/>` element and that is where the contents of
`about/+page.svelte` will be placed. So, first, create this page
src/routes/+layout.svelte:

```html
<nav>
	A menu will go here
</nav>

<main>
  <slot/>
</main>

<footer>
	Built with SvelteKit!
</footer>
```

Now, look at your web site. You should see your header and
footer, from the layout file, with the requested page's
contents placed in between.

The "Holy Grail" layout
=======================

This refers to a layout with the following properties:

1. There is a menu at the top of the page that stays there
	and doesn't move as the web site is used. It stays there
	even if the current page has a lot of content and the user
	scrolls down to view information that wasn't initially
	visible.

2. There is a footer at the bottom of the page that stays
	there and doesn't move as the web site is used, even
	when scrolling down.

3. There's an area in between where your content appears.
	If it contains more content than the area can hold
	vertically, a scroll bar appears that allows you to
	scroll the contents so all of it can be viewed. Also,
	we're going to limit the width of this area to 800px.
	You can choose any value that works for you, but it's
	very difficult to read text if the content is too
	wide because your eye will find it difficult to find
	the beginning of the next line when you're finished
	reading a line.

This is easiest to achieve using CSS grid layout and media
queries. We'll keep it simple, and we'll only use CSS grid
layout at the top level of our web site. We'll also use
CSS variables to make it easy to change things like text
and background colors throughout the document by making
changes in just one place.

First, add the following `<style>` block to src/app.html,
somewhere in the `<head>` section (I put it at the end
of the `<head>` section):

```html
		<style>
			:root {
				--bkg-color: GhostWhite;
				--text-color: Black;
				--menu-bkg-color: #09CABE;
				--menu-text-color: White;
				}
			* {
				box-sizing: border-box;
				}
			html, body {
				height: 100vh;
				width: 100vw;
				margin: 0;
				padding: 0
				}
			body {
				font: 15px sans-serif;
				display: grid;
				grid-template-areas:
					"left top    right"
					"left middle right"
					"left bottom right"
					;
				grid-template-rows: auto 1fr auto;
				}

			/* NOTE: Using a CSS variable in place of '800px' doesn't work */

			@media (max-width: 800px) {
				body {
					grid-template-columns: 0 100% 0;
					}
				}

			@media (min-width: 800px) {
				body {
					grid-template-columns: 1fr 800px 1fr;
					}
				}
		</style>
```

Secondly, in src/app.html, add `id="svelte"` to the
`<div>` element inside the `<body>`:

```html
<div id="svelte">%svelte.body%</div>
```

Lastly, we need to use the grid areas set up in
this file inside the src/routes/+layout.svelte file.
Add this style block to the bottom of the layout file:

```html
<style>
	main {
		grid-area: middle;
		padding: 15px 5px;
		overflow: auto;    /* scroll bars appear with large content */
		background-color: var(--bkg-color);
		color: var(--text-color);
		}

	nav, footer {
		background-color: var(--menu-bkg-color);
		color: var(--menu-text-color);
		text-align: center;
		margin: 0;
		padding: 5px 0;
		}

	nav {
		grid-area: top;
		}
	nav a {
		color: var(--menu-text-color);
		text-decoration: none;
		padding: 0 8px;
		display: inline-block;
		}
	nav a:hover {
		color: white;
		}

	footer {
		grid-area: bottom;
		}
</style>
```

I've added background colors to the 3 areas to make it
easier to see where they are. You can change or remove
them if you like.

NOTE: When running the development server, when you make a
change to a file, the web page in your browser is automatically
updated. However, some things are not noticed by SvelteKit
and you'll need to stop and start the development server.
One of those things is any change to your src/app.html file.
Another is any change to your svelte.config.js file. At this
point, you should restart the development server and probably
refresh the web page.

A simple menu
=============

We'll enhance it later, but for now, let's just set up a
simple menu that will give us access to all of our pages.
Change the `<nav>` element of your src/routes/
+layout.svelte file to:

```html
<nav>
	<a href="/">Home</a>
	<a href="/about">About</a>
	<a href="/contact">Contact</a>
</nav>
```

Using markdown
==============

When authoring your actual blog posts, you'll find that
it's much easier if you use a language called `markdown`.
We'll enable using markdown, then I'll show how it's used.

First, install the `mdsvex` package:

```bash
$ npm install -D mdsvex
```

Next, modify your svelte.config.js file like so:

```javascript
import adapter from '@sveltejs/adapter-auto';
import {mdsvex} from 'mdsvex';

export default {
	extensions: ['.svelte','.md'],
	kit: {
		adapter: adapter()
		},
	preprocess: [
		mdsvex({
			extensions: ['.md'],
			})
		],
	};
```

NOTE: Whenever you change your svelte.config.js file,
you'll need to restart the development server. Open the
terminal window where it's running, enter Ctrl-C to
stop the server, then restart it with `npm run dev`.

That's all you need to do! Let's test it by changing
your `about` file to a markdown file.
Replace your src/routes/about/+page.svelte file with
this src/routes/about/+page.md file:

````markdown
About my blog
=============

I created this **blog** mainly to allow me to document
**all** of
the projects that I'm working on. My main goals are:

1. Learn SvelteKit
2. Use Immer
3. Learn CoffeeScript
3. Create a web site for learning Chinese
4. Develop a language to enhance CoffeeScript
5. Develop a language to enhance Svelte

(don't worry about the incorrect numbering. I did it
intentionally to show that markdown uses the numbers to
determine that it's dealing with a numbered list, but
markdown automatically substitutes consecutive numbers)

Code Blocks
-----------

Here is some sample JavaScript code:

```javascript
str = 'abc' + ' ' + 'xyz';
console.log(`str = '${str}'`);
```
````

Here are some things you'll want to know about markdown:

1. A main header is created by following the text of the
	header with a line of just '=' characters
2. A second level header is created by following the text
	of the header with a line of just '-' characters
3. To bold-face some text, surround the text with '**'
4. To create a numbered list, just prefix the text with
	and integer, followed by a '.' character and a space
	character
5. To create a block of code, add lines before and after
	the code block consisting of three back-quote characters.
	To indicate the language in the block, follow the initial
	3 back-quote characters by the name of the language.
	Available are `javascript`,`coffeescript`,`text`,`css`,
	`svelte` and many others.

If you want to get better syntax hilighting for your
code blocks, like the javascript block above, you can
to go `https://github.com/PrismJS/prism-themes` and
find a theme you like (I use prism-gruvbox-light.css).
To use it, copy the source code
for the theme, put it in a file named markdown.css in
your `static` folder, which is in your root folder, then
in your app.html file, add this to your `<head>` section:

```html
<link rel="stylesheet" href="%sveltekit.assets%/markdown.css" />
```

Add a Blog Post
===============

Our first blog post will be about a state management library
named `immer`. I want to use it because of how it will enable
me to debug problems with my data structures. The steps to
add a new blog post to our blog site are:

1. Add a new directory inside of `src/routes/posts`. The new
	directory's name will be used in the link on your `posts`
	web page, so it should be descriptive of what the post is
	about. Here, we'll simply name the directory `immer`.

2. Inside the new folder, create the file `+page.md`. It will
	contain the text of the post. Here, we'll start by just
	putting a top-level heading with the text 'immer is cool!'.

3. On the page at `src/routes/+page.svelte` (the home page),
	replace the paragraph saying "My blog posts will go here
	eventually" with:

```html
<ul>
	<li><a href="/posts/immer">immer</a></li>
</ul>
```

Time to put the web site on the Internet!
=========================================

We want to create a completely static web site. That means that
the web site never changes - well, at least until you add
content, rebuild it, then re-deploy it. There's no database
or pages that change dynamically while the web site is running.
That will enable us to put the web site on the Internet
at no cost.

Install SvelteKit's static adapter. This will allow you to
create a static web site to deploy to the Internet.

```bash
> npm install -D @sveltejs/adapter-static@latest
```

Configure the adapter by opening the file
`svelte.config.js` and changing `adapter-auto` to
`adapter-static`:

To create a static web site, you must tell svelte that all
pages will be pre-rendered. You can do that by adding the
following file `src/routes/+layout.server.js`:

```js
export const prerender = true;
```

You can now build your app as a static web site by executing:

```bash
> npm run build
```

After that, you should check that a folder named **build**
was created in your root folder. It contains your entire
app as a set of files. You can preview this version of
the app by executing:

```bash
> npm run preview -- --open
```

This will automatically open your web page in your browser.
It should look exactly the same as the version running the
development server.

Deploy to the Internet
----------------------

Run surge to deploy your app to the Internet:

```bash
> surge ./build
```

When prompted, enter your email address and a password.
If you have an existing surge account, use that. Otherwise,
a new, free, account is set up for you.

Note that we've specified the project to upload - ./build
If you're prompted for the project, make sure you use that.

When prompted for a domain, surge will suggest one,
but you can change that in place - use your left arrow key to position
the cursor, backspace to delete existing characters, and normal keys
to edit the name. Just make sure it ends with
`.surge.sh`. If the name is already in use, you will
be told that and allowed to try again with another name.
For the purpose of this example, we'll use `jd-blog.surge.sh`.
NOTE: You will not be able to use that name for your project
because I'm using it! Try using your initials
in place of mine (jd).

I will refer to the domain you used as **<domain>** in the
following

When done, your web site will be on the Internet!

try entering the URL http://<domain> or https://<domain> in
your browser and check it out! The first, non-SSL URL should
actually redirect to the second SSL URL.

Modify package.json by adding key under scripts:

```javascript
"deploy": "npm run build && surge ./build --domain https://<domain>"
```

Be sure to 1) replace <domain> with your domain, and 2) add a
comma to the end of the preceding line - JSON requires that
keys be separated by a comma and (unfortunately) that the last
line in a set of keys does NOT have a trailing comma.

Try making a change to your home page, i.e. the file `src/routes/+page.svelte`,
then re-deploying. For example, add the line

The web page running the development server (if you still have
it running), should show the change immediately. To deploy that
version to the Internet, execute the command:

```bash
> npm run deploy
```

which will re-build your project, then deploy it to surge's
servers. Try the URL `https://<domain>` in your browser. If
you already had that page open in your browser, you can just
refresh the page. Pages deployed to the Internet won't
automatically update when changes are made the way they do
when you're developing.

Normally, you wouldn't deploy the new web page without first
testing it with the development or preview server. However, in
this case the change was very simple, and I wanted to show how
simple deploying a new web page can be.

From this point on, we will make all changes locally. Just
remember that when the web site works as you intend and you
want that version of the web site on the Internet, you can
simply execute:

```bash
> npm run deploy
```

Create a svelte component
=========================

I've added a few more blog posts to the site. The instructions
for doing so are above, and I'm not going to go through the
additional blog posts I created at this point. But the home
page source code now looks like this:

```html
<h1>My Home Page</h1>

<ul>
	<li><a href="/posts/immer">immer</a></li>
	<li><a href="/posts/get-caller">get JavaScript call stack</a></li>
	<li><a href="/posts/ideas">Ideas</a></li>
</ul>
```

I'd like to style the links to look better, and possibly even work
better, but at this point I've already got 3 of them, and eventually
there will be many more. It would be better if we created a
**Svelte component** that encapsulated the styling of the post
links, along with how the links worked, then put 3 of those
components on the home page.

We'll create a file that defines the new component. That file will
live in the `src/routes` folder and be named `BlogPost.svelte`. Note
that since the file name doesn't start with a `+` character, SvelteKit
won't think that it's a web page. In fact, SvelteKit will completely
ignore the file unless we specifically import it, which we will do
on the home page itself. First, create the `BlogPost.svelte` file
and place it in the `src/routes` folder:

```svelte
{#if label}
	<a href="/posts/{name}">{label}</a>
{:else}
	<a class="capitalize" href="/posts/{name}">{name}</a>
{/if}

<script>
	export let name;
	export let label = '';
</script>

<style>
	a {
		text-decoration: none;
		display: block;
		padding: 3px 20px;
		font-size: 18px;
		}
	a.capitalize {
		text-transform: capitalize;
		}
</style>
```

Things to know:

1. A Svelte file is really just HTML, except that you can only
	have one `<script>` block and only one `<style>` block.
	I don't know why, but it's not under my control.
2. The strange syntax starting with `{#if label}` is a Svelte
	`if` block. It conditionally renders one of a set of HTML
	blocks. The intention here is to use a `label` as is if
	provided, but if no label is provided, we want to display
	the `name` provided, but capitalize the first letter.
3. To use the component, you supply **properties**, though they
	work just like the **attributes** that you use with HTML
	elements. In this case, the properties that you would supply
	are named `url` and `label`. In the component file, you indicate
	which properties it supports by exporting variables with those
	names inside a `<script>` block. Here, I've also provided
	default values for them, though that's not required.
4. In your HTML content (i.e. outside of the `<script>` or `<style>`
	blocks if they exist), you can put a name inside `{` and `}`
	and it will be replaced with the value of that variable. In fact,
	you can really put any valid JavaScript expression in there and
	the result of evaluating that expression will be used. This can
	be done for regular text content or for the value of HTML
	element attributes.
5. The CSS that you put inside a `<style>` block will ONLY apply
	to HTML elements in this file. Those styles will not bleed into
	other elements on your web site.

Having created this component, let's see how to use it. Change your
home page (at `src/routes/+page.svelte`) to:

```svelte
<h1>My Home Page</h1>

<BlogPost name='immer' label='immer'/>
<BlogPost name='get-caller' label='get JavaScript call stack'/>
<BlogPost name='ideas'/>

<script>
	import BlogPost from './BlogPost.svelte'
</script>
```

Things to know:

1. To use the `BlogPost` component, you need to import it inside
	a `<script>` block.
2. All JavaScript in a Svelte file is ES6 code, which is what
	allows you to use the `import` statement.
3. I prefer to start my Svelte files with the HTML content,
	followed by a `<script>` block if needed, followed by a
	`<style>` block if needed. Many other people prefer to put the
	`<script>` block first. I think that **content is king** and
	therefore should come first.

Create post "How I created this blog"
=====================================

So, I've created this file to describe how this blog was
created. However, I don't want to put it inside my project
directory because I anticipate deleting it and re-creating it
using these very instructions. So, it exists outside my project
directory. Still, I'd like the blog to include these instructions.
To accomplish that, I'll add a step to the build process that
copies the file from it's current location to the directory
that holds my blog posts. Then I can add a link to the home page
for it. To make that happen, make a change in the `package.json`
file for the script `build`:

```js
		"build": "cp ../README.md ./src/routes/posts/how-to-build/+page.svelte && vite build",
```

Math
====

```bash
$ npm install mathlifier
```

Enable CoffeeScript
===================

Follow blog instructions
