import adapter from '@sveltejs/adapter-static';
import {mdsvex} from 'mdsvex';

const config = {
	extensions: ['.svelte','.md'],
	kit: {
		adapter: adapter()
		},
	preprocess: [
		mdsvex({
			extensions: ['.md'],
			})
		],
	};

export default config;
