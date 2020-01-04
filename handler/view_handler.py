from view.canvas_view import CanvasView
from view.zoom_view import ZoomView
from model.view_model import ViewModel

class ViewHander:

    def resize_window():
        ViewHander.__update()

    def initialize():
        ViewHander.__update()

    def __update():
        ViewModel.set_canvas_window_size(CanvasView.get_size())
        ViewModel.set_zoom_window_size(ZoomView.get_size())
