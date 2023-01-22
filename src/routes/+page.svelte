<svelte:head>
	<title>My Blog Posts</title>
</svelte:head>
<h1>My Blog Posts</h1>

<BlogPost name='covid' label='Covid-19 Statistics'/>
<BlogPost name='adding' label='How to add a new blog post'/>
<BlogPost name='get-caller' label='get JavaScript call stack'/>
<BlogPost name='how-to-build' label="How to build this site"/>
<BlogPost name='cielo-to-do' label="Cielo To Do List"/>
<BlogPost name='svg-plot' label="Plotting Data with SVG"/>
<BlogPost name='jqplot' label="Plotting Data with jqPlot"/>
<BlogPost name='css-variables' label="CSS variables"/>
<BlogPost name='css-grid' label="CSS Grid"/>
<hr>
<BlogPost name='sveltekit-from-scratch' label='SvelteKit from scratch'/>
<BlogPost name='sveltekit+coffee' label="Set up CoffeeScript in SvelteKit"/>
<BlogPost name='push-to-github' label='Push project to GitHub'/>
<BlogPost name='postcss' label='Use PostCSS with Svelte'/>
<hr>
<BlogPost name='component-lib' label='Create a Svelte Compoment Library'/>
<BlogPost name='lighten-darken-color' label="Lighten or Darken CSS color"/>
<BlogPost name='get-set-css-var' label="Get or Set CSS Variable"/>
<BlogPost name='svelte-icons' label="Icons for Svelte"/>
<BlogPost name='create-library' label="Create an npm installable library"/>

<script>
	import BlogPost from './BlogPost.svelte'
</script>
