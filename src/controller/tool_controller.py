from model.tool_model import ToolModel
from classes.tool import Tool

class ToolController:

    __button_corsor = None
    __button_pen = None
    __button_pinset = None
    __button_eracer = None
    __button_tube = None
    __button_snake = None
    __button_levelset = None
    __widget_levelset = None

    def set_button_corsor(ui):
        ToolController.__button_corsor = ui

    def set_button_pen(ui):
        ToolController.__button_pen = ui

    def set_button_pinset(ui):
        ToolController.__button_pinset = ui

    def set_button_eracer(ui):
        ToolController.__button_eracer = ui

    def set_button_tube(ui):
        ToolController.__button_tube = ui

    def set_button_snake(ui):
        ToolController.__button_snake = ui

    def set_button_levelset(ui):
        ToolController.__button_levelset = ui

    def set_widget_levelset(ui):
        ToolController.__widget_levelset = ui

    def change_tool(tool):
        ToolModel.change_tool(tool)

    def update_tool():
        tool = ToolModel.get_tool()
        ToolController.__button_corsor.setEnabled(True)
        ToolController.__button_pen.setEnabled(True)
        ToolController.__button_pinset.setEnabled(True)
        ToolController.__button_eracer.setEnabled(True)
        ToolController.__button_tube.setEnabled(True)
        ToolController.__button_snake.setEnabled(True)
        ToolController.__button_levelset.setEnabled(True)
        ToolController.__widget_levelset.setMinimumSize(0,0)
        if(tool == Tool.CORSOR):
            ToolController.__button_corsor.setEnabled(False)
        elif(tool == Tool.PEN):
            ToolController.__button_pen.setEnabled(False)
        elif(tool == Tool.PINSET):
            ToolController.__button_pinset.setEnabled(False)
        elif(tool == Tool.ERACER):
            ToolController.__button_eracer.setEnabled(False)
        elif(tool == Tool.TUBE):
            ToolController.__button_tube.setEnabled(False)
        elif(tool == Tool.SNAKE):
            ToolController.__button_snake.setEnabled(False)
        elif(tool == Tool.LEVELSET):
            ToolController.__button_levelset.setEnabled(False)
            ToolController.__widget_levelset.setMinimumSize(0,150)


    def get_tool():
        return ToolModel.get_tool()
