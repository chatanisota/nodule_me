
class ViewModel:

    __zoom_window_size = (0, 0)
    __canvas_window_size = (0, 0)

    def set_zoom_window_size(size):
        ViewModel.__zoom_window_size = size

    def get_zoom_window_size():
        return ViewModel.__zoom_window_size

    def set_canvas_window_size(size):
        ViewModel.__canvas_window_size = size

    def get_canvas_window_size():
        return ViewModel.__canvas_window_size
