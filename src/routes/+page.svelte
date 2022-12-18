<svelte:head>
	<title>My Blog Posts</title>
</svelte:head>
<h1>My Blog Posts</h1>

<BlogPost name='covid' label='Covid-19 Statistics'/>
<BlogPost name='adding' label='How to add a new blog post'/>
<BlogPost name='get-caller' label='get JavaScript call stack'/>
<BlogPost name='how-to-build' label="How to build this site"/>
<BlogPost name='cielo-to-do' label="Cielo To Do List"/>
<BlogPost name='svg-plot' label="Graphing Data with SVG"/>
<BlogPost name='jqplot' label="Graphing Data with jqPlot"/>
<BlogPost name='css-variables' label="CSS variables"/>
<BlogPost name='css-grid' label="CSS Grid"/>
<BlogPost name='push-to-github' label='Push project to GitHub'/>
<BlogPost name='component-lib' label='Create a Svelte Compoment Library'/>

<script>
	import BlogPost from './BlogPost.svelte'
</script>
