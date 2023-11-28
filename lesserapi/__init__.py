if (__debug__):
    try:
        # Github Api
        from .github import GithubScrape, GithubUserHandler, GithubRequestHandler
        
        from .core import __version__, __package__, __qualname__, __doc__
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe