Deploy to surge.sh
==================

NOTE: surge.sh can only be used for static web sites.
If you're using svelte, that means using @sveltejs/adapter-static.

You can use the `surge` command to deploy files to the
Internet. Their web site is at `https://surge.sh`. But you
don't need to use their web site at all. It's enough to install
the `surge` command using npm, then employing the `surge`
command. The first time you use it, you'll be asked for your
email address and to provide a password. It's free to use,
though your bandwidth is limited, so if you ever anticipate
a large amount of traffic to your web site, you'll need to
pay to increase that bandwidth limit. But for what we're going
to do, it's ideal.

Install the command with:

```bash
$ npm install -D surge
```

Deploy to the Internet
----------------------

Run surge to deploy your app to the Internet:

```bash
$ npx surge <folder>
```

`<folder>` is your static site folder and will
normally be named `build` or `dist`.

When prompted, enter your email address and a password.
If you have an existing surge account, use that. Otherwise,
a new, free, account is set up for you.

Note that we've specified the project to upload.
If you're prompted for the project, make sure you use that.

When prompted for a domain, surge will suggest one,
but you can change that in place - use your left arrow key to position
the cursor, backspace to delete existing characters, and normal keys
to edit the name. Just make sure it ends with
`.surge.sh`. If the name is already in use, you will
be told that and allowed to try again with another name.
For the purpose of this example, we'll use `jd-stories.surge.sh`.
NOTE: You will not be able to use that name for your project
because I'm using it! Try using your initials
in place of mine (jd).

I will refer to the domain you used as **<domain>** in the
following

When done, your web site will be on the Internet!

try entering the URL http://<domain> or https://<domain> in
your browser and check it out! The first, non-SSL URL should
actually redirect to the second SSL URL.

Modify package.json by adding key under scripts:

```javascript
"deploy": "npm run build && surge <folder> --domain https://<domain>"
```

Be sure to 1) replace <domain> with your domain, and 2) add a
comma to the end of the preceding line - JSON requires that
keys be separated by a comma and (unfortunately) that the last
line in a set of keys does NOT have a trailing comma.

Try making a change to your home page, i.e. the file
`src/routes/+page.svelte`,
then re-deploying. For example, add the line:

```html
<p>by me!</p>

The web page running the development server (if you still have
it running), should show the change immediately. To deploy that
version to the Internet, execute the command:

```bash
$ npm run deploy
```

which will re-build your project, then deploy it to surge's
servers. Try the URL `https://<domain>` in your browser. If
you already had that page open in your browser, you can just
refresh the page. Pages deployed to the Internet won't
automatically update when changes are made the way they do
when you're developing.

Normally, you wouldn't deploy the new web page without first
testing it with the development and preview server, and committing
all of your code to git. However, in
this case the change was very simple, and I wanted to show how
simple deploying a new web page can be.

From this point on, we will make all changes locally. Just
remember that when the web site works as you intend and you
want that version of the web site on the Internet, you can
simply execute:

```bash
$ npm run deploy
```
