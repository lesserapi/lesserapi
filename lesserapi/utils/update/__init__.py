from colorama import Fore
import subprocess, requests, platform
from ...core import __version__, __package__





class LesserApiUpdator[T: None]:
    """ Use this Class to update lesserapi Pacakge """
    
    def __repr__(self) -> str:
        super().__repr__()
        return """ Use this Class to update lesserapi Pacakge """
    
    @staticmethod
    def check_for_updates() -> T:
        get_version: requests.Response = requests.get(url='https://raw.githubusercontent.com/lesserapi/lesserapi/master/version.txt').text
        
        if (int(str(get_version).split(sep='.')[2]) > int(__version__.split(sep='.')[2])):
            print(f'{Fore.YELLOW}Your {__package__} version is : {Fore.BLUE}{__version__}, {Fore.WHITE}There is a new update for your Package Available: {Fore.GREEN}{get_version}{Fore.WHITE}')
        else:
            print(f'{Fore.WHITE}Your {__package__} is up to date')
    
    @staticmethod
    def update() -> T:
        __PLATFORM: str = platform.platform()
        
        if (__PLATFORM.startswith('Windows')):
            subprocess.call(['py', '-m', 'pip', 'install', '--upgrade', __package__])
            
        elif (__PLATFORM.startswith('Linux')):
            subprocess.call(['python', '-m', 'pip', 'install', '--upgrade', __package__])