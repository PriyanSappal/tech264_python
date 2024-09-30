# Learn Git - Stage 1 

## Creating your first Git Repo

You need to make a directory within the folder of your choice: 

```bash
cd 'OneDrive - Sparta Global'/Documents/Git/
mkdir tech264-test-git
cd tech264-test-git
```
#

To initialise a new git repo:

```bash
git init
```
#


Create the README.md file:
 
```bash
touch README.md
```
#
Modify the file
 
Add file to stage:
 
```bash
git add README.md
```
 #
Commit changes:
 
```bash
git commit -m "Added README file with some text"
```
 #
Modify the file again
 
Add file to stage:
 
```bash
git add README.md
```
#
Commit changes:
 
```bash
git commit -m "Second time commit"
```
#
Check the changes:
 
```bash
git checkout 351463fa9951f24fa708e19d1e727927bb0e71e4
```
```bash
git log
```


#
This shows the difference between the commits:
```bash
git diff e59a746 8990f90
```
#

Where you are currently is the head
``` bash
git checkout HEAD~1 -- <filename>
```
This would go to the previous commit from the master.
 
## In more detail:

# Git Commit Guide

This guide provides step-by-step instructions on how to commit changes in Git and how to use `HEAD~1` to reference the previous commit.

## Table of Contents
- [1. Initial Setup](#1-initial-setup)
- [2. Making Changes](#2-making-changes)
- [3. Staging Changes](#3-staging-changes)
- [4. Committing Changes](#4-committing-changes)
- [5. Understanding HEAD~1](#5-understanding-head1)
- [6. Example Usage of HEAD~1](#6-example-usage-of-head1)

## 1. Initial Setup
Before committing changes, ensure you have a Git repository initialized. If you don't have one, create a new repository:

```bash
git init my-repo
cd my-repo
```

**Note:** If you are starting a new project, make sure to replace `my-repo` with your desired project name.

## 2. Making Changes
Edit files in your project as needed. For example, you can create or modify a file called `README.md`:

```bash
echo "# My Project" > README.md
```

**Note:** You can use any text editor to edit files instead of the `echo` command.

## 3. Staging Changes
Before committing, you need to stage the changes you want to include in the commit. Use the following command:

```bash
git add README.md
```

You can stage all modified files using:

```bash
git add .
```

**Note:** Always review which files you are staging using `git status` before committing.

## 4. Committing Changes
Once your changes are staged, you can commit them with a descriptive message:

```bash
git commit -m "Add README.md file"
```

**Note:** Write clear commit messages to describe what changes were made and why.

## 5. Understanding HEAD~1
- `HEAD` refers to the latest commit in your current branch.
- `HEAD~1` refers to the commit before the latest one (the previous commit).

You can use `HEAD~1` to reference the last commit when performing operations such as reverting changes or comparing differences.

**Note:** Understanding `HEAD` and its relatives (`HEAD~2`, `HEAD~3`, etc.) helps in navigating your commit history.

## 6. Example Usage of HEAD~1

### Viewing the Previous Commit
To see the changes in the previous commit, you can use:

```bash
git show HEAD~1
```

**Note:** This will display the commit message, author information, and changes made in that commit.

### Reverting to the Previous Commit
If you want to revert your last commit and keep the changes in your working directory, you can use:

```bash
git reset HEAD~1
```

**Note:** This command will unstage the last commit but keep your changes, allowing you to modify them before committing again.

### Comparing the Latest Commit with the Previous One
To compare the latest commit with the previous commit:

```bash
git diff HEAD~1 HEAD
```

**Note:** This command shows you the differences between the most recent commit and the one before it, helping you understand what has changed.

## Conclusion
This guide provides the basic commands to commit changes in Git and how to utilize `HEAD~1` to reference previous commits. Practice these commands to become familiar with Git version control!

## Git Hub linking
1) First you need to make a remote repo which is made by first using the cd command in git bash to be on the relevant folder.
2) The below code will initialise that folder as a new git repo
``` bash
git init 
```
3) To track these files and stage them use:
```bash
git add .
```
4) To commit the changes to the local repo:
```bash
git commit . -m "{insert concise message}"
```
5) To link this with github you will need to go through the following git bash commands:
```bash
git remote add origin <github account>
git branch -M main 
git push -u origin main
```
* Links your local repo to the GitHub repository.
* Renames your current branch to main.
* Pushes your main branch to GitHub and sets it as the default for future pushes/pulls.

### What are some things that we should ignore?
* Sensitive (passwords, personal files etc.)
* Large files/folders that don't need to be pushed 
* Build folders (/bin, /out, etc)
* Hidden system files. 

* SOLUTION: .gitignore