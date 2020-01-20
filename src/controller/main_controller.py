
class MainController:

    __main_dialog = None

    @staticmethod
    def set_main_dialog(ui):
        MainController.__main_dialog = ui

    @staticmethod
    def appear_main_dialog():
        MainController.__main_dialog.showMaximized()

    @staticmethod
    def hide_main_dialog():
        MainController.__main_dialog.showMinimized()
