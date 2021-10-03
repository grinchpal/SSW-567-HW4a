import requests
import json

def my_function(uname):
    #uname = input("Enter your username: ")
    url = f"https://api.github.com/users/{uname}/repos"
    user_data = requests.get(url).json()
    output = "user " + uname + " has the following repos:"
    if len(user_data) == 0:
        return("user " + uname + " doesn't have any public repos")
    elif type(user_data) is dict and user_data['message'] == "Not Found":
        return("user " + uname + " doesn't exist")
    else:
        for repos in user_data:
            repoData = [repos['name'],0]
            commitUrl = f"https://api.github.com/repos/{uname}/{repos['name']}/commits"
            commit_data = requests.get(commitUrl).json()
            for commits in commit_data:
                repoData[1] = repoData[1]+1
            output = output + '\n' + "Repo: " + repoData[0] + " Number of commits: " + str(repoData[1])
            
         
        return(output)
