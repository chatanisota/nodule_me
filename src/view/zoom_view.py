from PyQt5.QtWidgets import QDialog, QLabel
from handler.handler import Handler

class ZoomView(QLabel):

    __instance = None

    def __init__(self, parent=None):
        super(ZoomView, self).__init__(parent)

        if ZoomView.__instance == None:
            ZoomView.__instance = self

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        Handler.zoom_view_press(x, y)

    def mouseMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        Handler.zoom_view_drag(x, y)

    def wheelEvent(self, event):
        Handler.zoom_mouse_wheel(event.angleDelta().y())

    @staticmethod
    def get_size():
        qrect = ZoomView.__instance.frameGeometry()
        return (qrect.width(), qrect.height())
