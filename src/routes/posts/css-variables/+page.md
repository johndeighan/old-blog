CSS Variables
=============

To create a CSS variable, use:

```css
:root {
	--graphWidth: 600px;
	--graphHeight: 300px;
	}
```

or you can scope the variables to particular
HTML elements by using regular selectors.

To use the variable in CSS, use:

```css
svg {
	width: var(--graphWidth);
	height: var(--graphHeight);
	}
```

To calculate with CSS variables you can use
the CSS calc() function:

```css
svg {
	width: calc(var(--graphWidth) - var(--buffer));
	}
```
