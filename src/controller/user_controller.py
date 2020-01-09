from model.user_model import UserModel

class UserController:

    __combo_box_user = None

    @staticmethod
    def set_combo_box_user(ui):
        UserController.__combo_box_user = ui

    @staticmethod
    def changed_current_user():
        UserModel.set_current_user_index(UserController.__combo_box_user.currentIndex())

    @staticmethod
    def init_users():
        UserModel.init_users()
        # ConfigModel
        UserModel.read_users()
        UserController.__combo_box_user.clear()
        UserController.__combo_box_user.addItems(UserModel.get_users_name())
        UserController.update_combo_box_user()

    @staticmethod
    def update_combo_box_user():
        UserController.__combo_box_user.blockSignals(True)
        UserController.__combo_box_user.setCurrentIndex(UserModel.get_current_user_index())
        UserController.__combo_box_user.blockSignals(False)
