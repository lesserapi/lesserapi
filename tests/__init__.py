from lesserapi.steam.scraper import SteamScrape
from lesserapi.github.scraper import GithubScrape
from lesserapi.handlers.user_handler import UserHandler
from lesserapi.handlers.request_handler import RequestHandler




def main():
    request: RequestHandler = RequestHandler(
        url=UserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.followers)
    print(scraper.followings)
    print(scraper.biography)
    



if (__name__ == "__main__"):
    main()