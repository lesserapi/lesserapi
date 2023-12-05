from lesserapi.steam.scraper import SteamScrape
from lesserapi.github.scraper import GithubScrape
from lesserapi.handlers.user_handler import UserHandler
from lesserapi.handlers.request_handler import RequestHandler




def main() -> None:
    request: RequestHandler = RequestHandler(
        url=UserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    steamScraper: SteamScrape = SteamScrape()
    
    scraper.startApi(log=False)
    steamScraper.startApi(log=False)
    
    print(scraper.followers)
    print(scraper.followings)
    print(scraper.biography)
    
    print(steamScraper.userMeta(profile_id='shervinbdndev', totalGames=True))
    print(steamScraper.userMeta(profile_id='shervinbdndev', totalAwards=True))
    print(steamScraper.userMeta(profile_id='shervinbdndev', totalGroupsJoined=True))
    



if (__name__ == "__main__"):
    main()