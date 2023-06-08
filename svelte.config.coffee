import adapter from '@sveltejs/adapter-static'
import {mdsvex} from 'mdsvex'
import {coffeePreProcessor} from '@jdeighan/svelte-utils/preprocessors'

export default {
	extensions: ['.svelte','.md']
	kit: {
		adapter: adapter()
		}
	preprocess: [
		mdsvex({
			extensions: ['.md']
			})
		script: coffeePreProcessor
		]
	}
