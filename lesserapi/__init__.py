if (__debug__):
    try:
        from .github import GithubScrape
        from .steam import SteamScrape
        from .steam.backup import GAME_CODES
        from .exceptions import NoneFilledPropertyException, NoneArgumentsInitialized, NonePublicArchiveRepositoryException, UserHasNoLocationException
        from .handlers.user_handler import UserHandler
        from .handlers.request_handler import RequestHandler
        from .utils import findGamesWithSameName
        from .utils.update import LesserApiUpdator
        from .core import __version__, __package__, __qualname__, __desc__, __annotations__
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe