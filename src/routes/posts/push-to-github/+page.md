Push project to GitHub
======================

1. Create a GitHub account on github.com
2. Install the GitHub CLI
3. `cd` to the directory containing the project
4. Open a plain CMD shell (improves prompt visibility)
4. In the CMD shell, execute the following:

```bash
$ gh repo create
	- select Push an existing local repository to GitHub
	- Path to local repository: enter '.' (the default)
	- Repository name: accept default (current directory name)
	- Description: enter a description
	- Visibility: public
	- Add a remote? Yes
	- What should the new remote be called? origin
	- Would you like to push commits from the current branch to "origin"? Yes
```

NOTE: My bash shell fails to display most of the prompts
If that happens to you, I suggest using a different shell,
even the CMD shell, to make sure you see the prompts.

OUTPUT from using CMD shell:

```text
C:\Users\johnd>gh repo create
? What would you like to do? Push an existing local repository to GitHub
? Path to local repository (.) blog

? Path to local repository blog
? Repository name (blog)

? Repository name blog
? Description (blog) My personal blog

? Description My personal blog
? Visibility Public
✓ Created repository johndeighan/blog on GitHub
? Add a remote? Yes
? What should the new remote be called? (origin)

? What should the new remote be called? origin
✓ Added remote https://github.com/johndeighan/blog.git
? Would you like to push commits from the current branch to "origin"? Yes
Enumerating objects: 111, done.
Counting objects: 100% (111/111), done.
Delta compression using up to 8 threads
Compressing objects: 100% (92/92), done.
Writing objects: 100% (111/111), 89.17 KiB | 3.18 MiB/s, done.
Total 111 (delta 19), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (19/19), done.
To https://github.com/johndeighan/blog.git
 * [new branch]      HEAD -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
←[0;32m✓←[0m Pushed commits to https://github.com/johndeighan/blog.git

```
