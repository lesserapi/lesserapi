if (__debug__):
    try:
        from typing import Literal

    except ModuleNotFoundError.__doc__ as mnfe:
        raise mnfe


class UserHandler:
    """ Base User Handler for Handling Users to the target URL by initializing the Arguments. """
    def __init__(self, username: str) -> Literal[None]:
        super(UserHandler, self).__init__()
        self.__username = username

    @property
    def username(self) -> str:
        return self.__username

    def serialize(self,
                  get_branch: bool = False,
                  get_repos: bool = False,
                  get_repos_v2: bool = False,
                  get_repos_v2_index: int = 1,
                  get_achievements: bool = False,
                  _: bool = False,
                  repo_name: str = None,
                  branch_name: str = None,
                  following: bool = False,
                  follower: bool = False,
                  stars: bool = False,
                  watchers: bool = False,
                  branches_count: bool = False,
                  steam_prof_id: bool = False,
                  steam_prof_code: bool = False,
                  steam_awards_prof_id: bool = False,
                  steam_awards_prof_code: bool = False,
                  steam_badges_prof_id: bool = False,
                  steam_badges_prof_code: bool = False,
        ) -> str:
        if (get_repos):
            return f'https://github.com/{self.username}?tab=repositories'
        if (get_repos_v2):
            return f'https://github.com/{self.username}?page={get_repos_v2_index}&tab=repositories'
        if (get_branch):
            return f'https://github.com/{self.username}/{repo_name}/commits/{branch_name}'
        if (get_achievements):
            return f'https://github.com/{self.username}?tab=achievements'
        if (following):
            return f'https://github.com/{self.username}?tab=following'
        if (follower):
            return f'https://github.com/{self.username}?tab=followers'
        if (stars):
            return f'https://github.com/{self.username}?tab=stars'
        if (watchers):
            return f'https://github.com/{self.username}/{repo_name}/watchers'
        if (branches_count):
            return f'https://github.com/{self.username}/{repo_name}/branches/all'
        if (_):
            return f'https://github.com/{self.username}/{repo_name}'
        if (steam_prof_id):
            return f'https://steamcommunity.com/id/{self.username}'
        if (steam_prof_code):
            return f'https://steamcommunity.com/profiles/{self.username}'
        if (steam_awards_prof_id):
            return f'https://steamcommunity.com/id/{self.username}/awards'
        if (steam_awards_prof_code):
            return f'https://steamcommunity.com/profiles/{self.username}/awards'
        if (steam_badges_prof_id):
            return f'https://steamcommunity.com/id/{self.username}/badges'
        if (steam_badges_prof_code):
            return f'https://steamcommunity.com/profiles/{self.username}/badges'

        return f'https://github.com/{self.username}'
