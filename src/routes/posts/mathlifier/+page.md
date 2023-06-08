Math in Svelte with mathlifier
==============================

Install:

```bash
$ npm install mathlifier
```
In Svelte:

```svelte
<p>Displays as: {@html math(formula)}</p>

<script>
	import {math, display} from 'mathlifier';

	formula = '\\sqrt{a+b+c}';
</script>
```

[See LaTeX math](/posts/latex-math#top) for LaTeX syntax
