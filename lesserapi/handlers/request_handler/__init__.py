if (__debug__):
    try:
        import requests
        from typing import Literal, Union
    
    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe







class RequestHandler:
    """ Base Request Handler for Handling Requests. """
    def __init__(self, url: str) -> Literal[None]:
        super(RequestHandler, self).__init__()
        self.__url = url
        self.__data = None
        
    @property
    def url(self) -> str:
        return self.__url
        
    def sendGetRequest(self, content: bool = False, status_code = False) -> Union[int, bytes, Literal[None]]:
        try:
            self.__data = requests.get(url=self.url)
            
        except* requests.ConnectionError as ce:
            raise ce.__doc__
        
        except* requests.RequestException as re:
            raise re.__doc__
        
        if (content):
            return self.__data.content
        
        if (status_code):
            return self.__data.status_code
        
        return self.__data