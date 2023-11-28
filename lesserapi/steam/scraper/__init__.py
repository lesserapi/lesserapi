if (__debug__):
    try:
        import re, sys, bs4
        from colorama.ansi import Fore
        from colorama.initialise import init
        from typing import Literal, Union, Any
        from ...handlers.user_handler import UserHandler
        from ...handlers.request_handler import RequestHandler
        from ...exceptions import NoneArgumentsInitialized
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe
    
    






class SteamScrape:
    """ Use This class to Gather and Identify Users on Steam Platform. """
    def __init__(self) -> Literal[None]:
        super(SteamScrape, self).__init__()
        self.__json_data = {}
        
    def displayName(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try:
            self.__json_data['displayName'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'actual_persona_name',
                }
            ).text
            
        except:
            self.json_data['displayName'] = None
        
        return self.json_data['displayName']
    
    def location(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try: 
            self.__json_data['location'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'header_real_name ellipsis',
                }
            ).text
        
        except:
            self.json_data['location'] = None
            
        return str(''.join(str(self.json_data['location']).split())).replace(profile_id if profile_id is not None else profile_code, '')
    
    def biography(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try:
            self.__json_data['biography'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'profile_summary',
                }
            ).text
        
        except:
            self.json_data['biography'] = None
            
        return self.json_data['biography']
    
    def biography(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try:
            self.__json_data['biography'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'profile_summary',
                }
            ).text
        
        except:
            self.json_data['biography'] = None
            
        return self.json_data['biography']
    
    def accountLevel(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try:
            self.__json_data['accountLevel'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'friendPlayerLevelNum',
                }
            ).text
        
        except:
            self.json_data['accountLevel'] = None
            
        return self.json_data['accountLevel']
    
    def userStatus(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try:
            self.__json_data['userStatus'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'profile_in_game_header',
                }
            ).text
        
        except:
            self.json_data['userStatus'] = None
            
        return self.json_data['userStatus']
    
    def userMeta(
        self,
        profile_id: Union[str, None] = None,
        profile_code: Union[str, None] = None,
        totalAwards: bool = False,
        totalBadges: bool = False,
        totalGames: bool = False,
        totalScreenShots: bool = False,
        totalVideosUploaded: bool = False,
        totalReviews: bool = False,
        totalGroupsJoined: bool = False,
        totalFriends: bool = False,
        ) -> Union[str, None]:
        tags: list[str] = []
        
        try:
            for tag in bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find_all(
                name='span',
                attrs={
                    'class': 'profile_count_link_total',
                }
            ):
                tags.append(tag.get_text(strip=True))
        
        except:
            tags = [None]
            
        if (totalAwards):
            return tags[0]
        
        elif (totalBadges):
            return tags[1]
        
        elif (totalGames):
            return tags[2]
        
        elif (totalScreenShots):
            return tags[4]
        
        elif (totalVideosUploaded):
            return tags[5]
        
        elif (totalReviews):
            return tags[6]
        
        elif (totalGroupsJoined):
            return tags[7]
        
        elif (totalFriends):
            return tags[8]
        
        return NoneArgumentsInitialized.__doc__
    
    def recentActivity(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[str, None]:
        try:
            self.__json_data['recentActivity'] = bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'recentgame_quicklinks recentgame_recentplaytime',
                }
            ).get_text(strip=True)
        
        except:
            self.json_data['recentActivity'] = None
            
        return self.json_data['recentActivity']
    
    def last3GamesPlayedMeta(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None, names: bool = False, info: bool = False) -> Union[list[str], None]:
        games_names: list[str] = []
        games_info: list[str] = []
        
        try:
            for game in bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find_all(
                name='div',
                attrs={
                    'class': 'game_name',
                }
            ):
                games_names.append(game.get_text(strip=True))
                
            for game in bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_prof_id=True if profile_id is not None else False,
                        steam_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find_all(
                name='div',
                attrs={
                    'class': 'game_info_details',
                }
            ):
                games_info.append(game.get_text(strip=True))
        
        except:
            games_names = [None]
            games_info = [None]
            
        if (names):
            return games_names
        
        elif (info):
            return games_info
        
        else:
            return NoneArgumentsInitialized.__doc__
        
    def userAwardsMeta(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None, awards_recieved: bool = False, awards_given: bool = False) -> Union[str, None]:
        awards: list[str] = []
        
        try:
            for award in bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_awards_prof_id=True if profile_id is not None else False,
                        steam_awards_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find_all(
                name='div',
                attrs={
                    'class': 'profile_awards_header_subtitle',
                }
            ):
                awards.append(award.get_text(strip=True))
                
        except:
            awards = [None]
            
        if (awards_recieved):
            return awards[0]

        if (awards_given):
            return awards[1]
        
        else:
            return NoneArgumentsInitialized.__doc__
        
    def badges(self, profile_id: Union[str, None] = None, profile_code: Union[str, None] = None) -> Union[list[str], list[None]]:
        badges: list[str] = []
        
        try:
            for badge in bs4.BeautifulSoup(
                markup=RequestHandler(
                    url=UserHandler(
                        username=profile_id if profile_id is not None else profile_code,
                    ).serialize(
                        steam_badges_prof_id=True if profile_id is not None else False,
                        steam_badges_prof_code=True if profile_code is not None else False,
                    )
                ).sendGetRequest(content=True),
                features='html5lib',
            ).find_all(
                name='div',
                attrs={
                    'class': 'badge_title',
                }
            ):
                badges.append(str(badge.get_text(strip=True)).replace('View details', ''))
                
        except:
            badges = [None]
        
        return badges
        
    @property
    def json_data(self) -> dict[str, Any]:
        return self.__json_data
    
    def startApi(self, log: bool = True) -> Literal[None]:
        if (int(list(sys.version_info)[1]) >= 11):
            if (log):
                init()
                print(f'{Fore.GREEN}Api Started Successfully{Fore.WHITE}')
            
            self.__json_data = {}
        else:
            print(f"{Fore.YELLOW}Your Current Python Interpereter version is {Fore.CYAN}{sys.version.split(sep=' ')[0]}\n{Fore.YELLOW}This Package implemented for Python Version {Fore.GREEN}3.11\n{Fore.YELLOW}If you want to Use this Package, you have to update your interpreter{Fore.WHITE}")
            sys.exit(0)