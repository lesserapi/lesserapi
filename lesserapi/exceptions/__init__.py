class UserHasNoLocationException(Exception):
    """User Has no Location"""
    
class NonePublicArchiveRepositoryException(Exception):
    """This Repository is not Public Archive"""
    
class NoneFilledPropertyException(Exception):
    """User Has not filled this property"""
    
class NoneArgumentsInitialized(Exception):
    """No Arguments Initialized, Please fill the Argument you want to recieve in return"""