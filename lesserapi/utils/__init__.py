from typing import Union
from ..steam.backup import GAME_CODES




def findGamesWithSameName[TProtectedString: Union[str, None], TProtectedListString: Union[list[str], list[None], None]](name: TProtectedString) -> TProtectedListString:
    games: TProtectedListString = []
    
    for game in GAME_CODES.keys():
        if (str(game).startswith(name)):
            games.append(game)
        continue
        
    return games