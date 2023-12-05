from ..steam.backup import GAME_CODES



def findGamesWithSameName[TProtectedString: str, TProtectedListString: list[str]](name: TProtectedString) -> TProtectedListString:
    games: TProtectedListString = []
    
    for game in GAME_CODES.keys():
        if (str(game).startswith(name)):
            games.append(game)
        continue
        
    return games