<h1 align='center' style="font-size:5rem"><b>lesserapi</b></h1>
<p align='center'><b>Version 1.1.18</b></p>
<p align='center'><b>Written with Python 3.11.3</b></p>
<div align="center">
    <div align="center">
        <img src="https://img.shields.io/github/license/lesserapi/lesserapi.svg"></img>
    </div>
    <img src="https://img.shields.io/github/forks/lesserapi/lesserapi.svg"></img>
    <img src="https://img.shields.io/github/stars/lesserapi/lesserapi.svg"></img>
    <img src="https://img.shields.io/github/watchers/lesserapi/lesserapi.svg"></img>
    <img src="https://img.shields.io/github/issues-pr/lesserapi/lesserapi.svg"></img>
    <img src="https://img.shields.io/github/issues-pr-closed/lesserapi/lesserapi.svg"></img>
    <img src="https://img.shields.io/github/downloads/lesserapi/lesserapi/total.svg"></img>
</div>
<br>
<div align="center">
    <img style="display:block;margin-left:auto;margin-right:auto;width:70%;" src="https://github-readme-stats.vercel.app/api/pin/?username=lesserapi&repo=lesserapi&theme=dracula"></img>
</div>
<br>
<h3 align='center'>Ready To Use</h3>
<h3 align='center'>Developed by Shervin Badanara (shervinbdndev) on Github</h3>
<div align="center">
    <img src="https://forthebadge.com/images/badges/made-with-python.svg"></img>
</div>
<br>
<hr>
<br>
<h2 align='center'><b>Language and technologies used in This Project</h2>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></img>
<img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white"></img>
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"></img>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"></img>
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></img>
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></img>
<img src="https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"></img>
<img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white"></img>

<br>
<h2 align='center'><b>WorkSpace</h2>
<img src="https://img.shields.io/badge/Intel-Core_i5_10600K-0071C5?style=for-the-badge&logo=intel&logoColor=white"></img>
<img src="https://img.shields.io/badge/NVIDIA-RTX2060 OC-76B900?style=for-the-badge&logo=nvidia&logoColor=white"></img>
<img src="https://img.shields.io/badge/Windows11-0078D6?style=for-the-badge&logo=windows&logoColor=white"></img>


<hr>


<br><br><br>
<h1 align='left'><b>Update Your Interpreter</b></h1>

# Windows / CMD

```python
py -m pip install --upgrade pip
```

# Linux / Terminal

```python
python -m pip install --upgrade pip
```
<br>

<hr>
<br><br><br>
<h1 align='left'><b>Installation</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install lesserapi
```
<h2 align='left'>or</h2>

```python
py -m pip install lesserapi
```

<br><br><br>
<h1 align='left'><b>Update Library</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install -U lesserapi
```

<h2 align='left'>or</h2>

```python
py -m pip install --upgrade lesserapi
```

<br><br><br>

> [!WARNING]
> This Package Only can run in Python 3.11.3 or above.

<hr>
<br>
<h1 align='left'><b>Usage</b></h1>

<br>

<details>

<summary style="font-size:2rem">Github</summary>

```python
from lesserapi.github.scraper import GithubScrape # Scraper Class
from lesserapi.github.handlers.user_handler import GithubUserHandler # User Handler Class
from lesserapi.github.handlers.request_handler import GithubRequestHandler # Request Handler Class


def main():

    # UserHandler serializes the value you given to the username param
    # RequestHandler gets the Serialized data then sends a GET request to github servers and saves the page content in request variable

    request: GithubRequestHandler = GithubRequestHandler(
        url=GithubUserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    

    # Scrape gets the variable as an arg

    scraper: GithubScrape = GithubScrape(data=request)

    # then we start using API by calling the startApi method
    
    scraper.startApi(log=False) # log param is for safety, the default value is True but you can change it
    

    # After all of these steps now you're free to use the API

    print(scraper.followers)
    print(scraper.followings)
    print(scraper.biography)
    
    print(scraper.json_data) # get full json data of user



if (__name__ == "__main__"):
    main()



```

<br><br><br>

# New Addons & Changes on Version 1.1.3

- ### Now you can Access User's Repositories Names.

```py

from lesserapi.github.scraper import GithubScrape
from lesserapi.github.handlers.user_handler import GithubUserHandler
from lesserapi.github.handlers.request_handler import GithubRequestHandler




def main():
    request: GithubRequestHandler = GithubRequestHandler(
        url=GithubUserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)

    # Then your free to use the new method to get User's Repositories names
    
    print(scraper.repositoriesNames(username='shervinbdndev'))

    # ftl (first to last) is a new option that you can use to show the repositories from the first created to the last one

    print(scraper.repositoriesNames(username='shervinbdndev', ftl=True)) # default value is False

    # Also you can select the repository by index like below

    print(scraper.repositoriesNames(username='shervinbdndev')[3]) # for example I want the 4th repository (It starts from 0 btw)



if (__name__ == "__main__"):
    main()



```

<br><br><br>

# New Addons & Changes on Version 1.1.4

## Now you can Access

- ### User's Total Stars Given.
- ### User's Profile Picture Url.
- ### Check Repository Star Count.

```python

from lesserapi.github.scraper import GithubScrape
from lesserapi.github.handlers.user_handler import GithubUserHandler
from lesserapi.github.handlers.request_handler import GithubRequestHandler



def main():
    request: GithubRequestHandler = GithubRequestHandler(
        url=GithubUserHandler(username='shervinbdndev').serialize()
    ).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.totalStarsGiven) # total stars given
    
    print(scraper.profilePictureUrl) # profile picture url

    # now using this new method you lets you check users repository's star count

    print(scraper.checkRepositoryStars(
        username='shervinbdndev', # user's username
        repo_name='Quizino', # repository's name
    ))




if (__name__ == "__main__"):
    main()

```

<br><br><br>

# New Addons & Changes on Version 1.1.5

## Now you can Access

- ### User's Last Year Contributions.
- ### Check if User's Repository is Public Archive.
- ### Check if User has README.md.
- ### Get Repository's Used Languages.
- ### Get User's Unlocked Achievements.


```python


from lesserapi.github.scraper import GithubScrape
from lesserapi.github.handlers.user_handler import GithubUserHandler
from lesserapi.github.handlers.request_handler import GithubRequestHandler




def main():
    user: GithubUserHandler = GithubUserHandler(username='shervinbdndev').serialize() # user instance
    
    request: GithubRequestHandler = GithubRequestHandler(url=user).sendGetRequest(content=True) # send request by RequestHandler
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.lastYearContributions) # last year contributions
    
    print(scraper.isRepositoryPublicArchive(username='shervinbdndev', repo_name='Quizino')) # check if repository is public archive => returns True or False
    
    print(scraper.userHasReadMe(username='shervinbdndev')) # check if user has README.md

    print(scraper.repositoryUsedLanguages(username='shervinbdndev', repo_name='lesserapi')) # get repository's used languages (also you can select by index)

    print(scraper.userAchievements(username='shervinbdndev')) # get user's achievements (also you can select by index)
    



if (__name__ == "__main__"):
    main()


```

<br><br><br>

# New Addons & Changes on Version 1.1.9

## Now you can Access

- ### List of User's Followings.
- ### List of User's Followers.
- ### Check Last Commit date of Repository with selected Branch.
- ### Check all Commit Dates of a Repository.
- ### Count the Repository Branches.
- ### Check if a Repository is froked from another Repository.
- ### Check if Repository has a LICENSE.
- ### Check the Repository's License Type.
- ### List Repository's Branches.
<br><br>

## +2 Beta Methods

- ### Get all Stars that the User has given to the Repositories.
- ### List all of the Watchers of a Repository.


```python


from lesserapi.github.scraper import GithubScrape
from lesserapi.github.handlers.user_handler import GithubUserHandler
from lesserapi.github.handlers.request_handler import GithubRequestHandler




def main():
    user: UserHandler = UserHandler(username='shervinbdndev').serialize()
    
    request: GithubRequestHandler = GithubRequestHandler(url=user).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.listFollowings(username='shervinbdndev')) # List of User's Followings
    print(scraper.listFollowers(username='shervinbdndev')) # List of User's Followings

    # This Method is in Beta version of itself
    # It doesn't show all User's Stars that given to Repositories
    # It only Lists The Repositories on the first page
    print(scraper.starsGivenRepositoriesNames(username='shervinbdndev'))

    # Last Commit date of Repository with selected Branch
    print(scraper.repositoryLastCommitDateOnBranch(username='shervinbdndev', repo_name='lesserapi', branch_name='master'))

    # Commits dates of Repository with selected Branch
    print(scraper.repositoryCommitsDatesOnBranch(username='shervinbdndev', repo_name='lesserapi', branch_name='master'))

    # Count of selected Repository Branches
    print(scraper.repositoryBranchesCount(username='shervinbdndev', repo_name='lesserapi'))

    # Check if current Repository is Forked from another Repository
    print(scraper.currentRepositoryIsForkedFromAnotherRepository(username='shervinbdndev', repo_name='lesserapi'))

    # Check if Repository has a LICENSE
    print(scraper.repositoryHasLicense(username='shervinbdndev', repo_name='lesserapi'))

    # Get License Type of a Repository
    print(scraper.repositoryLicenseType(username='shervinbdndev', repo_name='lesserapi'))

    # List of Repository Watchers
    # This Method is in Beta version of itself
    print(scraper.listRepositoryWatchers(username='shervinbdndev', repo_name='lesserapi'))

    # List of Repository Branches
    print(scraper.listRepositoryBranches(username='shervinbdndev', repo_name='lesserapi'))
    



if (__name__ == "__main__"):
    main()


```

<br><br><br>

# New Addons & Changes on Version 1.1.15

## Now you can Access

- ### Check if User is Pro or Not.
- ### User Organizations.
- ### User Organizations Pictures.

```python

from lesserapi.github.scraper import GithubScrape
from lesserapi.github.handlers.user_handler import GithubUserHandler
from lesserapi.github.handlers.request_handler import GithubRequestHandler



def main():
    user: UserHandler = UserHandler(username='shervinbdndev').serialize()
    
    request: GithubRequestHandler = GithubRequestHandler(url=user).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.isPro)
    print(scraper.userOrganizations(username='shervinbdndev'))
    print(scraper.userOrganizationsPictures(username='shervinbdndev'))



if (__name__ == "__main__"):
    main()

```



</details>

<details>

<summary style="font-size:2rem">Steam</summary>

# New Addons & Changes on Version 1.1.18

## Now you can Access Steam.
## Some Package Structure has changed.
## Using RequestHandler & UserHandler for gathering steam Users data, has Removed.

```python

from lesserapi.steam.scraper import SteamScrape




def main():
    scraper: SteamScrape = SteamScrape()
    
    scraper.startApi(log=True)
    
    # Here you can get the Data of User by 2 types of gathering info: 1-By Profile ID   2- By Profile Code
    # if user has no Profile ID, don't worry, you can use their Profile Code Instead.
    print(scraper.displayName(profile_id='shervinbdndev')) # if User has no Profile ID
    print(scraper.displayName(profile_code='76561198358095760')) # Use their Profile Code
    
    print(scraper.location(profile_id='shervinbdndev'))
    print(scraper.biography(profile_id='shervinbdndev'))
    print(scraper.accountLevel(profile_id='shervinbdndev'))
    print(scraper.userStatus(profile_id='shervinbdndev'))
    print(scraper.recentActivity(profile_id='shervinbdndev'))
    print(scraper.badges(profile_id='shervinbdndev'))
    print(scraper.userAwardsMeta(profile_id='shervinbdndev', awards_given=True))
    
    # By using this function, you can access some of the User's Meta Data such as these below:
    print(scraper.userMeta(profile_id='shervinbdndev', totalAwards=True))
    print(scraper.userMeta(profile_id='shervinbdndev', totalFriends=True))
    print(scraper.userMeta(profile_id='shervinbdndev', totalBadges=True))
    print(scraper.userMeta(profile_id='shervinbdndev', totalGames=True))
    print(scraper.userMeta(profile_id='shervinbdndev', totalGroupsJoined=True))
    print(scraper.userMeta(profile_id='shervinbdndev', totalReviews=True))
    print(scraper.userMeta(profile_id='shervinbdndev', totalVideosUploaded=True))
    
    # use can use both methods on gathering the user data.
    print(scraper.userMeta(profile_code='76561198358095760', totalAwards=True))
    print(scraper.userMeta(profile_code='76561198358095760', totalFriends=True))
    .
    .
    .
    
    # here's an Example of put User's last 3 games played into variables by using the function below:
    # Also do not forget that you can initialize the params
    games_names: list[str] = scraper.last3GamesPlayedMeta(profile_id='shervinbdndev', names=True)
    games_info: list[str] = scraper.last3GamesPlayedMeta(profile_id='shervinbdndev', info=True)

    # here you can create a dictionary with values of games and keys of User's game info
    toDictType: dict[str, str] = dict(zip(games_names, games_info))
    
    print(toDictType)
    
    
    # Output
    # {
    #     'Counter-Strike 2': '1,397 hrs on recordlast played on 27 Nov',
    #     'ELDEN RING': '254 hrs on recordlast played on 27 Nov',
    #     'Far Cry 4': '33 hrs on recordlast played on 27 Nov'
    # }
    



if (__name__ == "__main__"):
    main()

```

</details>

<details>

<summary style="font-size:2rem">Instagram</summary>

### Not Soon Cause of Filtering

</details>


<details>

<summary style="font-size:2rem">Aparat</summary>

### Soon


</details>

<br>
<br>
<br>



<h1 align='left'>Enjoy :)</h1>

<br>
<h3><b>Package Uploaded in PYPI :<a href="https://pypi.org/project/lesserapi/">Here</a></b></h3>