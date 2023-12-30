# restapi-boilerplate
A boilerplate repo for django restapi

Ideally, you may follow these steps to start a Django Rest Framework project, with Docker, nginx, including image media.


# Get the repository
Clone the repository:
```
git clone https://github.com/hamdiozdemir/restapi-boilerplate.git
```
get into it and start working
```
cd restapi-boilerplate
```

# connect your new repo
Remove boilerplate from remote and connect the new one
*mMake sure that you re starting a new repo. You might loose your previous work.*
```
git remote remove origin
git remote add origin <your_new_repo_url>
git rebase origin/main
```
# ready to push your new repo
Now you can push your codes to github
```
git add .
git commit -m "hello new project"
git push origin main
```
