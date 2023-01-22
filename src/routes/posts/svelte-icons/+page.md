How to use icons in svelte
==========================

Import the `svelte-icons` package:

```bash
$ npm install svelte-icons
```

Search this page to find an icon:
`svelte-icons.vercel.app`

When you click on an icon, the import statement that you
need will be placed in your clipboard.

Go to the file where you want to use the icon and
paste the import statement into the `<script>` section.

The import statement will look something like:

```js
import FaAccessibleIcon from 'svelte-icons/fa/FaAccessibleIcon.svelte'
```

You can now use the imported name as a svelte component, e.g.:

```html
<FaAccessibleIcon/>
```