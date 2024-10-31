# Basic Interaction with GitHub

There are various remote repository hosting sites:

[GitHub](https://github.com/)

[BitBucket](https://bitbucket.org/product/)

[GitLab](https://about.gitlab.com/)


Follow the workflow at https://github.com/join  to set up a free account, username, and password. After that, [these steps](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) will help you create a brand new repository on GitHub.

Some useful commands for getting started:

| Comando       | Explicación                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------|
| `git clone URL` | https://git-scm.com/docs/git-clone                   |
| `git push`    | https://git-scm.com/docs/git-push            |
| `git pull`    | https://git-scm.com/docs/git-pull|

This can be useful for keeping your local workspace up to date.

- https://help.github.com/en/articles/caching-your-github-password-in-git

- https://help.github.com/en/articles/generating-an-ssh-key
  

# Git Remotes

You’ve learned about what a remote is, working with remotes, fetching new changes, and updating the local repository. Use this study guide as an easy reference of Git commands for working with remotes. This study guide gives a brief explanation of these useful commands along with a link to the Git documentation for each command. Keeping study guides like this one easily accessible can help you code more efficiently.

## Commands

| Command                  | Explanation                                                                                                      |
|--------------------------|------------------------------------------------------------------------------------------------------------------|
| `git remote`             | `$ git remote` allows you to manage the set of repositories or “remotes” whose branches you track.              |
| `git remote -v`          | `$ git remote -v` is similar to `$ git remote`, but adding `-v` shows more information such as the remote URL.  |
| `git remote show <name>` | `$ git remote show <name>` shows some information about a single remote repo.                                   |
| `git remote update`      | `$ git remote update` fetches updates for remotes or remote groups.                                             |
| `git fetch`              | `$ git fetch` can download objects and refs from a single repo, a single URL, or from several repositories at once. |
| `git branch -r`          | `$ git branch -r` lists remote branches and can be combined with other branch arguments to manage remote branches. |



