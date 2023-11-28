from lesserapi.github.scraper import GithubScrape
from lesserapi.github.handlers.user_handler import GithubUserHandler
from lesserapi.github.handlers.request_handler import GithubRequestHandler




def main():
    request: GithubRequestHandler = GithubRequestHandler(
        url=GithubUserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    
    scraper: GithubScrape = GithubScrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.followers)
    print(scraper.followings)
    print(scraper.biography)
    



if (__name__ == "__main__"):
    main()