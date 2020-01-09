from classes.user import User
from classes.color import Color

class UserModel:

    __current_user_index = 0

    __user_list = []

    @staticmethod
    def set_current_user_index(id):
        UserModel.__current_user_index = id

    @staticmethod
    def init_users():
        UserModel.__user_list = []
        UserModel.__current_user_index = 0
        UserModel.__user_list.append(User(0,"GUEST",Color.white()))

    @staticmethod
    def read_users():
        UserModel.__user_list.append(User(100,"User1",Color.aqua()))
        UserModel.__user_list.append(User(101,"User2",Color.green()))
        UserModel.__user_list.append(User(102,"User3",Color.lime()))
        UserModel.__user_list.append(User(103,"User4",Color.purple()))
        UserModel.__user_list.append(User(104,"User5",Color.fuchsia()))
        UserModel.__user_list.append(User(105,"User6",Color.yellow()))
        UserModel.__user_list.append(User(200,"Test1",Color.olive()))
        UserModel.__user_list.append(User(201,"Test2",Color.navy()))
        UserModel.__user_list.append(User(202,"Test3",Color.teal()))
        UserModel.__user_list.append(User(203,"Test4",Color.maroon()))


    @staticmethod
    def get_users_name():
        names = []
        for user in UserModel.__user_list:
            names.append(user.get_name())
        return names

    @staticmethod
    def get_current_user():
        return UserModel.__user_list[UserModel.__current_user_index]

    @staticmethod
    def get_current_user_id():
        user = UserModel.__user_list[UserModel.__current_user_index]
        return user.get_id()

    @staticmethod
    def get_current_user_index():
        return UserModel.__current_user_index


    @staticmethod
    def get_user_by_id(id):
        for user in UserModel.__user_list:
            if id == User.WRITTING_ID:
                return User.prefab_writting_user()
            if id == user.get_id():
                return user
        return None

    @staticmethod
    def get_user_color_by_id(id):
        user = UserModel.get_user_by_id(id)
        if(not user == None):
            return user.get_color()
        return Color.black()
