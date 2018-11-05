class User:
    """
    Class that generates new instances of users
    """

    user_list = []

 def __init__(self, username, password):
        """
        __init__ method that helps us define properties for our objects.
        """

        self.username = username
        self.password = password    

 def save_user(self):
        '''
        save_user method saves password objects into user_list
        '''

        User.user_list.append(self)
@classmethod
    def find_by_userpass(cls, username_search, password_search):
        '''
        Method that takes in a username/password and authenticates the user matching.
        Args:
            username_search: User name to authenticate.
            password_search: His password.
        Returns :
            Password of person that matches.
        '''

        for user in cls.user_list:
            if user.username == username_search and user.password == password_search:
                return user
