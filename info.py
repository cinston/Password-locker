 class Info:
    """
    Class that generates new instances of users
    """

    pass
     def __init__(self, username, cred_app, cred_user, cred_pass):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.username = username
        self.info_app = info_app
        self.info_user = info_user
        self.info_pass = info_pass
    
    
    def save_cred(self):
        '''
        save_info method saves info objects into info_list
        '''

        Info.info_list.append(self)

     def delete_info(self):
        '''
        delete_info method deletes a saved info from the info_list
        '''

        Info.info_list.remove(self)  



 @classmethod
    def search_info(cls, user_search, app_search):
        '''
        Method that takes in an Appname and username and returns a info that matches.
        Args:
            username: Username to search for
            info_app: Appname to search
        Returns :
            Info that matches Username and Appname.
        '''

        for info in cls.info_list:
            if info.username == user_search and info.cred_app == app_search:
                return info      

#  @classmethod
#     def display_info(cls, user_search):
#         '''
#         method that returns the info list
#         '''
#         all_user_info =[]
#         for info in cls.info_list:
#             if info.username == user_search:
#                 all_user_info.append(info)
#         return all_user_info              