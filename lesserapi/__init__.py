if (__debug__):
    try:
        from .steam import SteamScrape
        from .github import GithubScrape
        from .exceptions import *
        from .handlers import *
        from .core import __version__, __package__, __qualname__, __doc__
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe