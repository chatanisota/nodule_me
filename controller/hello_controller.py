from model.user_model import UserModel
from PyQt5 import QtCore

class HelloController:

    __hello_dialog = None
    __combo_box_user_hello = None

    @staticmethod
    def set_hello_dialog(ui):
        HelloController.__hello_dialog = ui
        HelloController.__hello_dialog.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint)

    @staticmethod
    def set_combo_box_user(ui):
        UserController.__combo_box_user = ui

    @staticmethod
    def set_combo_box_user_hello(ui):
        HelloController.__combo_box_user_hello = ui

    @staticmethod
    def start_hello():
        UserModel.set_current_user_index(HelloController.__combo_box_user_hello.currentIndex())

    @staticmethod
    def show_hello_dialog():
        HelloController.__hello_dialog.show()
        HelloController.__combo_box_user_hello.clear()
        HelloController.__combo_box_user_hello.addItems(UserModel.get_users_name())

    @staticmethod
    def close_hello_dialog():
        HelloController.__hello_dialog.accept()
