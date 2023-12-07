class UserHasNoLocationException(Exception):
    """User Has no Location"""
    
    def __repr__(self) -> str:
        super().__repr__()
        return """User Has no Location"""
    
class NonePublicArchiveRepositoryException(Exception):
    """This Repository is not Public Archive"""

    def __repr__(self) -> str:
        super().__repr__()
        return """This Repository is not Public Archive"""
    
class NoneFilledPropertyException(Exception):
    """User Has not filled this property"""

    def __repr__(self) -> str:
        super().__repr__()
        return """User Has not filled this property"""
    
class NoneArgumentsInitialized(Exception):
    """No Arguments Initialized, Please fill the Argument you want to recieve in return"""

    def __repr__(self) -> str:
        super().__repr__()
        return """No Arguments Initialized, Please fill the Argument you want to recieve in return"""