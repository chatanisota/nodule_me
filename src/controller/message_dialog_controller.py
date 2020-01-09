from classes.message_dialog import MessageDialog

class MessageDialogController:

    __message_dialog = None

    def set_message_dialog(ui):
        MessageDialogController.__message_dialog = ui

    def open(text):
        MessageDialog.open(MessageDialogController.__message_dialog, text)
