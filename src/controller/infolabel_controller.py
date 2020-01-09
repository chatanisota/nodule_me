from model.infolabel_model import InfolabelModel
from model.label_model import LabelModel
from model.tool_model import ToolModel
from classes.tool import Tool

class InfolabelController:

    __label_info = None

    def set_label_info(ui):
        InfolabelController.__label_info = ui

    def update_infolabel():
        text = LabelModel.get_cursor_point_for_infolabel()
        if(text==None):
            text = " "
        tool = ToolModel.get_tool()
        if(tool == Tool.PEN):
            if(LabelModel.is_writting_label()):
                text += InfolabelModel.get_text_in_pen_labeling()
            elif(LabelModel.is_writting_labels()):
                text += InfolabelModel.get_text_in_pen_labelings()
            else:
                text += InfolabelModel.get_text_in_pen()
        elif(tool == Tool.PINSET):
            text += InfolabelModel.get_text_in_pinset()
        elif(tool == Tool.ERACER):
            text += InfolabelModel.get_text_in_eracer()
        else:
            text += InfolabelModel.get_text_in_eracer()
        InfolabelController.__label_info.setText(text)
