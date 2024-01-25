# 1. FSAP is the abbreviation of First Study AI Project

URL: ```https://github.com/FSAIP/nlp.git```


# 2. git command lines
## 2.1. Change directory to <repository>
``` cd <repository> ```

## 2.2. Create and check a branch
``` git branch <branch> 	        # create a new branch
    git checkout <branch>      	# change branch
    git branch                      # check currently using branch
```
## 2.3. add, commit & push
```
git add <file>   	        # add a file
git add -A                   	# add all changed files and deleted files
git commit -m "<comment>"         # commit
git push origin <branch or main>          # push to origin/branch
```

## 2.4. Copy a file from one branch to another
```
git checkout <paste_branch>
git checkout <copy_branch> <file_name> 
```

## 2.5. Delete a branch
```
git branch -d <branch>
```
