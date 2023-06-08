<svelte:head>
	<link
		rel="stylesheet"
		href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css"
		integrity="sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0"
		crossorigin="anonymous"
	/>
</svelte:head>

<h1>LaTeX math</h1>
<p>Useful in Jupyter notebooks (cell type "markdown") and excalidraw</p>
<p>Inline formulas are delimited by $ ... $</p>
<p>Stand alone formulas are delimited by $$ ... $$</p>

{#each lExamples as {label, multiline, str, desc}}
	<hr>
	{#if multiline}
		<p>{label}:</p>
		<pre>{str}</pre>
	{:else}
		<p>{label}:  {str}</p>
	{/if}
	<p>Displays as: {@html math(str)}</p>
	{#if desc}
		{desc}
	{/if}
{/each}


<script>
	import {math, display} from 'mathlifier';

	let lExamples = [
		{
			label: 'Spacing between symbols',
			str: 'a b c \\; a \\; b \\; c',
			},
		{
			label: 'Greek Letters',
			str: '\\alpha \\beta \\gamma',
			},
		{
			label: 'Blackboard Font',
			str: '\\mathbb{R}, \\mathbb{Z}, \\mathbb{D}',
			},
		{
			label: 'Calligraphic Font',
			str: '\\mathcal{R}, \\mathcal{Z}, \\mathcal{D}',
			},
		{
			label: 'Hats over symbols',
			str: '\\hat{a}, \\hat{b}, \\hat{c}',
			desc: 'In addition to \\hat there is \\bar, \\dot, \\tilde, \\overrightarrow',
			},
		{
			label: 'Subscripts',
			str: 'x_1',
			},
		{
			label: 'Superscripts',
			str: 'x^2',
			},
		{
			label: 'Nabla (gradient)',
			str: '\\nabla f(x_0,y_0)',
			},
		{
			label: 'Fractions',
			str: '\\frac{a+b}{a-b}',
			},
		{
			label: 'Square root',
			str: '\\sqrt{a+b+c}',
			},
		{
			label: 'Sums with limits',
			str: '\\sum\\limits_{i=1}^{n}i^2',
			},
		{
			label: 'Products with limits',
			str: '\\prod\\limits_{i=1}^{n}i^2',
			},
		{
			label: 'Integral with limits',
			str: '\\int\\limits_{-\\infty}^{\\infty} f(x) dx',
			},
		{
			label: 'Misc',
			str: 'a \\equiv b, a \\approx b, a \\rightarrow \\infty',
			},
		{
			label: 'Large parens, brackets, braces',
			str: '\\left( \\frac{a+b}{a-b} \\right)',
			desc: 'You can substitute [] or {} for ()',
			},
		{
			label: 'Multiplication with a dot symbol',
			str: 'a \\cdot b',
			},
		{
			label: 'Multiplication with a cross symbol',
			str: 'a \\times b',
			},
		{
			label: 'Set union',
			str: 'A \\cup B',
			},
		{
			label: 'Set intersection',
			str: 'A \\cap B',
			},
		{
			label: 'Subset',
			str: 'A \\subset B',
			},
		{
			label: 'In set',
			str: 'a \\in A',
			},
		{
			label: 'Not in set',
			str: 'a \\notin A',
			},
		{
			label: 'Similarity',
			str: 'A \\sim B',
			},
		{
			label: 'Exists',
			str: '\\exists a:a>0',
			},
		{
			label: 'For all',
			str: '\\forall a:a>0',
			},
		{
			label: 'Matrix',
			multiline: true,
			str: "\\begin{pmatrix}\na & b & c \\\\\nd & e & f \\\\\n\\end{pmatrix}",
			},
		{
			label: 'Cases',
			multiline: true,
			str: "f(x)=\\begin{cases}\n\\frac{1}{b-a}, & x\\in[a,b] \\\\ \n 0, & x\\notin[a,b]\n\\end{cases}",
			}
		];
</script>

<style>
	h1 {
		color: black;
		}
</style>
