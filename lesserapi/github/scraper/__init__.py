if (__debug__):
    try:
        import re
        import sys
        import bs4
        import requests
        from colorama.ansi import Fore
        from colorama.initialise import init
        from typing import Literal, Union, Any
        from ..handlers.user_handler import GithubUserHandler
        from ..handlers.request_handler import GithubRequestHandler
        from ..exceptions import UserHasNoLocationException, NonePublicArchiveRepositoryException, NoneFilledPropertyException
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe
    
    






class GithubScrape:
    def __init__(self, data: GithubRequestHandler) -> Literal[None]:
        super(GithubScrape, self).__init__()
        self.__data = data
        self.__json_data = {}
        
    @property
    def fullname(self) -> Union[str, None]:
        try:
            self.__json_data['fullname'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'p-name vcard-fullname d-block overflow-hidden',
                }
            ).text.strip()
        except:
            self.json_data['fullname'] = None
        
        return self.json_data['fullname']
    
    @property
    def followers(self) -> Union[int, None]:
        try:
            self.__json_data['followers'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'text-bold color-fg-default',
                }
            ).text
        except:
            self.json_data['followers'] = None
        
        return self.json_data['followers']
    
    @property
    def followings(self) -> Union[int, None]:
        try:
            self.__json_data['followings'] = re.search(
                pattern=r'\d+',
                string=str(bs4.BeautifulSoup(
                    markup=self.__data,
                    features='html5lib',
                ).find_all(
                    name='span',
                    attrs={
                        'class': 'text-bold color-fg-default',
                    }
                )[1]),
            ).group()
        except:
            self.json_data['followings'] = None
        
        return self.json_data['followings']
    
    @property
    def biography(self) -> Union[Any, str, None]:
        try:
            self.__json_data['biography'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'
                }
            ).text
        except:
            self.json_data['biography'] = NoneFilledPropertyException.__doc__
        
        return self.json_data['biography']
    
    @property
    def location(self) -> Union[Any, str, None]:
        try:
            self.__json_data['location'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'p-label',
                }
            ).text
        except:
            self.__json_data['location'] = UserHasNoLocationException.__doc__
        
        return self.json_data['location']
    
    @property
    def website(self) -> Union[Any, str, None]:
        try:
            self.__json_data['website'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='a',
                attrs={
                    'class': 'Link--primary',
                }
            ).text
        except:
            self.json_data['website'] = NoneFilledPropertyException.__doc__
        
        return self.json_data['website']
    
    @property
    def totalRepositories(self) -> Union[int, None]:
        try:
            self.__json_data['totalRepositories'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'Counter',
                    'data-view-component': 'true',
                }
            ).text
        except:
            self.json_data['totalRepositories'] = None
        
        return self.json_data['totalRepositories']
    
    @property
    def totalStarsGiven(self) -> Union[int, None]:
        try:
            self.__json_data['totalStarsGiven'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='svg',
                attrs={
                    'class': 'octicon octicon-star UnderlineNav-octicon hide-sm',
                }
            ).find_next(
                name='span',
            ).get_text()
        except:
            self.json_data['totalStarsGiven'] = None
        
        return self.json_data['totalStarsGiven']
    
    def repositoriesNames(self, username: str, ftl: bool = False) -> Union[list[str], list[None]]:
        names: list = []
        
        try:
            for element in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(get_repos=True)).sendGetRequest(content=True), features='html5lib').find(name='h3', attrs={'class': 'wb-break-all'}).find_all_next(name='a', attrs={'itemprop': 'name codeRepository'}):
                names.append(str(element).replace('href', '').replace('itemprop="name codeRepository', '').replace(f'<a ="/{username}/', '').replace('</a>', '').replace('">', '').replace('"', '').split(sep=' ')[0])
            
            self.json_data['repositoriesNames'] = names
        except:
            self.json_data['repositoriesNames'] = None
        
        if (ftl):
            return names[::-1]
        
        return names
    
    def repositoryDescription(self, username:str, repo_name: str, reverse: bool = False) -> Union[str, None]:
        try:
            self.__json_data['repositoryDescription'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username,).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='p',
                attrs={
                    'class': 'f4 my-3',
                },
            ).text.strip()
        except:
            self.json_data['repositoryDescription'] = None
        
        if (reverse):
            return self.json_data['repositoryDescription'][::-1]
        
        return self.json_data['repositoryDescription']
    
    def isRepositoryPublicArchive(self, username: str, repo_name: str) -> Union[str, bool, None]:
        status: bool = False
        
        try:
            self.__json_data['isRepositoryPublicArchive'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username,).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'Label Label--attention v-align-middle mr-1',
                },
            )
        
            if (self.__json_data['isRepositoryPublicArchive'].get_text(strip=True) == 'Public archive'):
                status = True
                return status
            else:
                return NonePublicArchiveRepositoryException.__doc__
        except:
            status = False
            return status
        
    def repositoryUsedLanguages(self, username: str, repo_name: str) -> Union[list[str], list[None]]:
        langs: list[str] = []
        
        try:
            for lang in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True), features='html5lib').find(name='ul', attrs={'class': 'list-style-none'}).find_all_next(name='span', attrs={'class': 'color-fg-default text-bold mr-1'}):
                langs.append(lang.text)
        except:
            langs = [None]
            
        return langs
    
    def userHasReadMe(self, username: str) -> bool:
        self.__json_data['userHasReadMe'] = requests.get(url=f'https://github.com/{username}/{username}')
        
        if (self.__json_data['userHasReadMe'].status_code == 200):
            return True
        
        return False
    
    def userAchievements(self, username: str) -> Union[list[str], list[None]]:
        achievements: list[str] = []
        
        try:
            for achievement in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(get_achievements=True)).sendGetRequest(content=True), features='html5lib').find(name='div', attrs={'class': 'd-flex flex-wrap p-3'}).find_all_next(name='h3', attrs={'class': 'f4 ws-normal'}):
                achievements.append(achievement.text)
        except:
            achievements = [None]
            
        return achievements
    
    def checkRepositoryStars(self, username: str, repo_name: str) -> Union[int, None]:
        try:
            self.__json_data['checkRepositoryStars'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='svg',
                attrs={
                    'class': 'octicon octicon-star mr-2',
                }
            ).find_next(
                name='strong',
            ).get_text()
        except:
            self.json_data['checkRepositoryStars'] = None
        
        return self.json_data['checkRepositoryStars']
    
    def repositoryLastCommitDateOnBranch(self, username: str, repo_name: str, branch_name: str) -> Union[str, None]:
        try:
            self.__json_data['repositoryLastCommitDateOnBranch'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(
                    get_branch=True,
                    branch_name=branch_name,
                    get_repos=True,
                    repo_name=repo_name,
                )).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='relative-time',
                attrs={
                    'class': 'no-wrap',
                }
            ).get_text()
        except:
            self.json_data['repositoryLastCommitDateOnBranch'] = None
        
        return self.json_data['repositoryLastCommitDateOnBranch']
    
    def repositoryCommitsDatesOnBranch(self, username: str, repo_name: str, branch_name: str) -> Union[list[str], list[None]]:
        commits: list[str] = []
        
        try:
            for commit in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(get_branch=True, branch_name=branch_name, repo_name=repo_name)).sendGetRequest(content=True), features='html5lib').find_all(name='h2', attrs={'class': 'f5 text-normal'}):
                commits.append(str(commit).replace('<h2 class="f5 text-normal">Commits on ', '').replace('</h2>', ''))
        except:
            commits = [None]
                
        return commits
    
    def repositoryBranchesCount(self, username: str, repo_name: str) -> Union[int, None]:
        try:
            self.__json_data['repositoryBranchesCount'] = int(
                bs4.BeautifulSoup(
                    markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                    features='html5lib',
                ).find(
                    name='div',
                    attrs={
                        'class': 'flex-self-center flex-self-stretch d-none flex-items-center lh-condensed-ultra d-lg-flex',
                    }
                ).find(
                    name='strong'
                ).get_text()
            )
        except:
            self.json_data['repositoryBranchesCount'] = None   
            
        return self.json_data['repositoryBranchesCount']
    
    def currentRepositoryIsForkedFromAnotherRepository(self, username: str, repo_name: str) -> bool:
        try:
            self.__json_data['currentRepositoryIsForkedFromAnotherRepository'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'text-small lh-condensed-ultra no-wrap mt-1',
                }
            ).get_text().strip()
            
            if (self.json_data['currentRepositoryIsForkedFromAnotherRepository'][0:11] == 'forked from'):
                return True
            
            return False
        
        except:
            return False
    
    def repositoryHasLicense(self, username: str, repo_name: str) -> bool:
        try:
            self.__json_data['repositoryHasLicense'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='h3',
                attrs={
                    'class': 'sr-only',
                }
            ).get_text().strip()
            
            if (self.json_data['repositoryHasLicense'] == 'License'):
                return True
            
            return False
        
        except:
            return False
    
    def repositoryLicenseType(self, username: str, repo_name: str) -> Union[str, None]:
        try:
            self.__json_data['repositoryLicenseType'] = bs4.BeautifulSoup(
                markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='a',
                attrs={
                    'class': 'Link--muted',
                }
            ).get_text().strip()
            
        except:
            self.json_data['repositoryLicenseType'] = None
                
        return self.json_data['repositoryLicenseType']
    
    ##############################
    #   Method in Beta Version   #
    ##############################
    def listRepositoryWatchers(self, username: str, repo_name: str) -> Union[list[str], list[None]]:
        watchers: list[str] = []
        
        try:
            for watcher in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(watchers=True, repo_name=repo_name)).sendGetRequest(content=True), features='html5lib').find(name='ol', attrs={'class': 'd-block d-md-flex flex-wrap gutter list-style-none'}).find_all(name='a', attrs={'data-octo-click': 'hovercard-link-click'}):
                watchers.append(watcher.get_text())
        except:
            watchers = [None]
            
        return watchers
    
    def listRepositoryBranches(self, username: str, repo_name: str) -> Union[list[str], list[None]]:
        branches: list[str] = []
        
        try:
            for branch in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(branches_count=True, repo_name=repo_name)).sendGetRequest(content=True), features='html5lib').find_all(name='a', attrs={'class': 'branch-name css-truncate-target v-align-baseline width-fit mr-2 Details-content--shown'}):
                branches.append(branch.get_text())
        except:
            branches = [None]
            
        return branches
    
    def listFollowings(self, username: str) -> Union[list[str], list[None]]:
        followings: list[str] = []
        
        try:
            for following in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(following=True)).sendGetRequest(content=True), features='html5lib').find(name='div', attrs={'class': 'position-relative'}).find_all_next(name='span', attrs={'class': 'Link--secondary'}):
                followings.append(following.get_text())
        except:
            followings = [None]
        
        return followings
    
    def listFollowers(self, username: str) -> Union[list[str], list[None]]:
        followers: list[str] = []
        
        try:
            for follower in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(follower=True)).sendGetRequest(content=True), features='html5lib').find(name='div', attrs={'class': 'position-relative'}).find_all_next(name='span', attrs={'class': 'Link--secondary'}):
                followers.append(follower.get_text())
        except:
            followers = [None]
        
        return followers
    
    ##############################
    #   Method in Beta Version   #
    ##############################
    def starsGivenRepositoriesNames(self, username: str) -> Union[list[str], list[None]]:
        sgrns: list[str] = []
        
        try:
            for sgrn in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(stars=True)).sendGetRequest(content=True), features='html5lib').find(name='div', attrs={'class': 'position-relative'}).find_all_next(name='div', attrs={'class': 'd-inline-block mb-1'}):
                sgrns.append(sgrn.get_text().strip())
        except:
            sgrns = [None]
        
        return sgrns
    
    def MinMaxRepositoryStarsByPageIndex(self, username: str, page_index: int, show_min: bool = False , show_max: bool = False) -> Union[int, list[int]]:
        list_stars: list[int] = []
        
        try:
            for stars in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize(get_repos_v2=True, get_repos_v2_index=page_index)).sendGetRequest(content=True), features='html5lib').find_all(name='div', attrs={'class': 'f6 color-fg-muted mt-2'}):
                list_stars.append(int(str(stars.find('a', {'class': 'Link--muted mr-3'}).get_text()).strip()))
    
        except:
            list_stars = [None]
        
        if (show_min):
            return min(list_stars)
        
        if (show_max):
            return max(list_stars)
            
        return [min(list_stars), max(list_stars)]
    
    def userOrganizations(self, username: str) -> Union[list[str], list[None]]:
        orgs: list[str] = []
        
        try:
            for org in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize()).sendGetRequest(content=True), features='html5lib').find_all(name='img', attrs={'height': '32', 'width': '32', 'class': 'avatar',}):
                orgs.append(org.get_attribute_list(key='alt')[0])
                
        except:
            orgs = [None]
            
        return orgs
    
    def userOrganizationsPictures(self, username: str) -> Union[list[str], list[None]]:
        orgsPics: list[str] = []
        
        try:
            for org in bs4.BeautifulSoup(markup=GithubRequestHandler(url=GithubUserHandler(username=username).serialize()).sendGetRequest(content=True), features='html5lib').find_all(name='img', attrs={'height': '32', 'width': '32', 'class': 'avatar',}):
                orgsPics.append(org.get_attribute_list(key='src')[0])
                
        except:
            orgsPics = [None]
            
        return orgsPics
    
    @property
    def isPro(self) -> bool:
        try:
            self.__json_data['isPro'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'title': 'Label: Pro',
                    'class': 'Label Label--purple text-uppercase',
                }
            ).get_text(strip=True)
            
            if (self.json_data['isPro'] == 'Pro'):
                self.json_data['isPro'] = True
            
        except:
            self.json_data['isPro'] = False
            
        return self.json_data['isPro']
    
    @property
    def lastYearContributions(self) -> Union[int, None]:
        try:
            self.__json_data['lastYearContributions'] = int(
                str(
                    bs4.BeautifulSoup(
                        markup=self.__data,
                        features='html5lib',
                    ).find(
                        name='h2',
                        attrs={
                            'class': 'f4 text-normal mb-2',
                        }
                    ).text.strip()
                ).split(sep=' ')[0]
            )
        except:
            self.json_data['lastYearContributions'] = None
        
        return self.json_data['lastYearContributions']
    
    @property
    def profilePictureUrl(self) -> Union[str, None]:
        try:
            self.__json_data['profilePictureUrl'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='img',
                attrs={
                    'class': 'avatar avatar-user width-full border color-bg-default',
                }
            ).get_attribute_list(key='src')[0]
        except:
            self.json_data['profilePictureUrl'] = None
        
        return self.json_data['profilePictureUrl']
        
    @property
    def json_data(self) -> dict[str, Any]:
        return self.__json_data
    
    def startApi(self, log: bool = True) -> Literal[None]:
        if (int(list(sys.version_info)[1]) >= 11):
            if (log):
                init()
                print(f'{Fore.GREEN}Api Started Successfully{Fore.WHITE}')
            
            self.__json_data = {
                'fullname': self.fullname,
                'followers': self.followers,
                'followings': self.followings,
                'biography': self.biography,
                'location': self.location,
                'website': self.website,
                'isPro': self.isPro,
                'totalRepositories': self.totalRepositories,
                'totalStarsGiven': self.totalStarsGiven,
                'lastYearContributions': self.lastYearContributions,
                'profilePictureUrl': self.profilePictureUrl,
            }
        else:
            print(f"{Fore.YELLOW}Your Current Python Interpereter version is {Fore.CYAN}{sys.version.split(sep=' ')[0]}\n{Fore.YELLOW}This Package implemented for Python Version {Fore.GREEN}3.11\n{Fore.YELLOW}If you want to Use this Package, you have to update your interpreter{Fore.WHITE}")
            sys.exit(0)