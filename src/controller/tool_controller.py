from model.tool_model import ToolModel
from classes.tool import Tool

class ToolController:

    __button_pen = None
    __button_pinset = None
    __button_eracer = None
    __button_tube = None

    def set_button_pen(ui):
        ToolController.__button_pen = ui

    def set_button_pinset(ui):
        ToolController.__button_pinset = ui

    def set_button_eracer(ui):
        ToolController.__button_eracer = ui

    def set_button_tube(ui):
        ToolController.__button_tube = ui

    def change_tool(tool):
        ToolModel.change_tool(tool)

    def update_tool():
        tool = ToolModel.get_tool()
        ToolController.__button_pen.setEnabled(True)
        ToolController.__button_pinset.setEnabled(True)
        ToolController.__button_eracer.setEnabled(True)
        ToolController.__button_tube.setEnabled(True)
        if(tool == Tool.PEN):
            ToolController.__button_pen.setEnabled(False)
        elif(tool == Tool.PINSET):
            ToolController.__button_pinset.setEnabled(False)
        elif(tool == Tool.ERACER):
            ToolController.__button_eracer.setEnabled(False)
        elif(tool == Tool.TUBE):
            ToolController.__button_tube.setEnabled(False)

    def get_tool():
        return ToolModel.get_tool()
