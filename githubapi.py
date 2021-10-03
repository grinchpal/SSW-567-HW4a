import requests
import json

def my_function(uname):
    #uname = input("Enter your username: ")
    url = f"https://api.github.com/users/{uname}/repos"
    user_data = requests.get(url).json()
    if len(user_data) == 0:
        print("user " + uname + " doesn't have any public repos")
    elif type(user_data) is dict and user_data['message'] == "Not Found":
        print("user " + uname + " doesn't exist")
    else:
        for repos in user_data:
            repoData = [repos['name'],0]
            commitUrl = f"https://api.github.com/repos/{uname}/{repos['name']}/commits"
            commit_data = requests.get(commitUrl).json()
            for commits in commit_data:
                repoData[1] = repoData[1]+1
            print("user " + uname + " has the following repos:")
            print("Repo: " + repoData[0] + " Number of commits: " + str(repoData[1]))

my_function("test20")
my_function(";aksjdf;kajsd;fkj")
my_function("richkempinski")