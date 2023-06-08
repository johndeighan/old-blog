Custom Elements with Lit
========================

Set up a Svelte project that uses CoffeeScript, then:

```bash
$ npm install -D lit redefine-custom-elements
```

Define the custom element
-------------------------

Put this file in `src/lib/MyCustomElement.coffee`:

```coffeescript
# --- MyCustomElement.coffee

import 'redefine-custom-elements'
import {LitElement, html, css} from 'lit'

# ---------------------------------------------------------------------------

export class MyCustomElement extends LitElement

	# --- Names of properties to watch for changes
	@properties = {
		name: undefined
		version: undefined
		completed: undefined
		}

	@styles = css"""
		.completed {
			text-decoration-line: line-through;
			color: #777;
			}
		"""

	constructor: () ->
		super()
		@name = 'John'
		@completed = false
		@message = 'Hello, World!'

	render: () ->
		return html"""
			<p>
				Hello, #{@name}
			</p>
			<p>
				Name: <input value=#{@name} @input=#{@changeName}>
			</p>
			<p>
				<input type="checkbox" ?checked=#{@msgHidden} @click=#{@toggle}>
				Completed
			</p>
			<p class=#{if @completed then 'completed' else ''}>
				#{@message}
			</p>
			<pre>completed is #{@completed}</pre>
			"""

	toggle: (event) ->
		if @completed
			@completed = false
		else
			@completed = true

	changeName: (event) ->
		@name = event.target.value
```

Then, use it in your `routes/+page.svelte`:

```svelte
<h1>Custom Elements with Lit 3</h1>

<my-custom-element/>

<script lang="coffee">
	import 'redefine-custom-elements'
	import {MyCustomElement} from '$lib/MyCustomElement.js'

	customElements.define('my-custom-element', MyCustomElement);
</script>
```
