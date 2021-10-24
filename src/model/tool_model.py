from classes.tool import Tool

class ToolModel:

    __tool_no = Tool.CORSOR

    def change_tool(no):
        ToolModel.__tool_no = no

    def get_tool():
        return ToolModel.__tool_no
