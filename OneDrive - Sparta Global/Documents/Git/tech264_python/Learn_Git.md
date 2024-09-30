# Learn Git - Stage 1 

## Creating your first Git Repo

You need to make a directory within the folder of your choice: 

```bash
cd 'OneDrive - Sparta Global'/Documents/Git/
mkdir tech264-test-git
cd tech264-test-git
```


```bash
git init
```
To initialise a new git repo

Create the README.md file:
 
```bash
touch README.md
```
 
Modify the file
 
Add file to stage:
 
```bash
git add README.md
```
 
Commit changes:
 
```bash
git commit -m "Added README file with some text"
```
 
Modify the file again
 
Add file to stage:
 
```bash
git add README.md
```
 
Commit changes:
 
```bash
git commit -m "Second time commit"
```
 
Check the changes:
 
```bash
git checkout 351463fa9951f24fa708e19d1e727927bb0e71e4
```
```bash
git log
```
has context menu