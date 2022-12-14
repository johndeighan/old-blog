CSS Grid
========

In the containing element's CSS, set up the grid areas:

```css
<containing element> {
	display: grid;
	grid-template-areas:
		"left top    right"
		"left middle right"
		"left bottom right"
		;
	grid-template-rows: auto 1fr auto;
	@media (max-width: 800px) {
		body {grid-template-columns: 0 100% 0;}
		}
	@media (min-width: 800px) {
		body {grid-template-columns: 1fr 800px 1fr;}
		}
	}
```

In the contained element's CSS, specify the area
that should hold the element:

```css
<contained element> {
	grid-area: middle;
	...etc.
	}
```
