Adding executable scripts to a library
======================================

In your project's root directory, create a
directory named `bin`

Inside the `bin` folder, add the file
`<script name>` with no file extension:

```js
#!/usr/bin/env node

<JavaScript code>
```

Using executable scripts in a project
=====================================

When project A installs library B locally,
and library B includes an executable script,
the script will be copied to project A's
`node_modules/.bin` folder. After that, you
can run the script while cd'd to project A's
root folder with:

```bash
$ npx <script name>
```
