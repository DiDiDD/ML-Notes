### Recursively remove all .pyc files and __pycache__ directories in the current directory.
```find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf```


### Remove .idea files from PHPStorm with git & .gitignore
```
git rm --cached .idea/
echo '.idea' >> .gitignore
git add .gitignore
git commit -m "Removed .idea files"
```

### Remove .DS_Store files from PHPStorm with git & .gitignore
```
git rm --cached .DS_Store/
echo '.DS_Store' >> .gitignore
git add .gitignore
git commit -m "Removed .DS_Store files"
```