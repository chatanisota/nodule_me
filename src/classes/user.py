from classes.color import Color

class User:

    __user_id = 0
    __user_name = "nanasi"
    __color = Color.red()
    WRITTING_ID = -1
    WRITTINGS_ID = -2
    SUSPENDED_ID = -3

    def __init__(self, user_id, user_name, color):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__color = color

    def get_name(self):
        return self.__user_name

    def get_id(self):
        return self.__user_id

    def get_color(self):
        return self.__color

    @staticmethod
    def prefab_writting_user():
        user = User(User.WRITTING_ID, "", Color.red())
        return user

    @staticmethod
    def prefab_writtings_user():
        user = User(User.WRITTINGS_ID, "", Color.orange())
        return user

    @staticmethod
    def prefab_suspended_user():
        user = User(User.SUSPENDED_ID, "", Color.red())
        return user
