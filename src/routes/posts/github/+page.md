GitHub setup
============

1. Create a GitHub repository using GitHub CLI

```bash
$ gh repo create <name> --public
```
`<name>` should not include your GitHub user name. It's a simple
name like 'hello'

2. Push a project to the GitHub repo:

- make sure you have a .gitignore file to exclude, e.g. the node_modules folder

```bash
$ cd <project directory>
$ git init
$ git remote add origin https://github.com/<gh-username>/<repo-name>
$ git add -A
$ git commit -m "initial commit"
$ git branch -M main
$ git push -u origin main
```
