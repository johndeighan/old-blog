SVG Cheat Sheet
===============

```html
<svg width=400 height=300>
	<line x1=5 y1=5 x2=20 y2=20/>
	<circle cx=200 cy=200 r=5/>
	<rect x=50 y=50 width=100 height=200 rx=25/>
	<polygon points="10,10 50,50 50,10"/>
	<polyline points="10,10 50,50 50,10"/>
	<path d="M 10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80"/>

	# --- Good for producing line graphs ---
	<g id="content">
		<rect x=150 y=150 width=100 height=200/>
	</g>
	<use xlink:href="#content" x=300 y=300 width=100 height=100/>

	<symbol id="myDot" width="10" height="10" viewBox="0 0 2 2">
		<circle cx="1" cy="1" r="1" />
	</symbol>
	<use href="#myDot" x=5 y=5/>

	<text x=50 y=50>
		This is text
	</text>

	# --- rotate 90 degrees around point (200,200)
	<text x=200 y=200 transform="rotate(90,200,200)">
		More text
	</text>

</svg>
```

`<path>` d parameter is a sequence of commands.

```css
<style>
	svg {
		border: 1px solid red;
		margin: 5px;
		}
	text {    /* same text properties as in HTML text */
		font-size: 24px;
		font-weight: bold;
		font-style: italic;
		text-decoration: line-through;
		}
	symbol {
		opacity: 50%;
		}
	rect {
		fill: blue;
		fill-opacity: 50%;
		stroke: black;
		stroke-width: 2px;
		stroke-dasharray: 5 2;
		stroke-opacity: 50%;
		}
	line {
		stroke: purple;
		stroke-width: 5px;
		stroke-linecap: round;  /* butt, round, square */
		}
	circle {
		stroke: black;
		fill: yellow;
		}
	polygon {
		fill: rgba(255,0,0,1);
		}
	polyline {
		fill: none;
		stroke: black;
		stroke-width: 2px;
		stroke-linejoin: miter; /* miter, round, bevel */
		}
	path {
		fill: none;
		stroke: black;
		stroke-width: 2px;
		}
</style>
```

