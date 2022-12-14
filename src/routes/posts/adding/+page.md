Adding a new blog post
======================

1. Add a new directory inside `src/routes/posts`
2. Add a file named `+page.md` or `+page.svelte` inside the new directory
3. In `routes/+page.svelte`, add a new `<BlogPost>` element
4. Test the blog site with `npm run dev -- --open`
5. Deploy the new page with `npm run deploy`

Deleting a blog post
====================

1. Remove `<BlogPost>` entry from  `routes/+page.svelte`
2. Remove directory inside `src/routes/post` for the post
4. Test the blog site with `npm run dev -- --open`
5. Deploy the new page with `npm run deploy`
