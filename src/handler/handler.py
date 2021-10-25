from controller.file_controller import FileController
from controller.canvas_controller import CanvasController
from controller.histogram_controller import HistogramController
from controller.index_controller import IndexController
from controller.image_controller import ImageController
from controller.map_controller import MapController
from controller.label_controller import LabelController
from controller.tool_controller import ToolController
from controller.user_controller import UserController
from controller.infolabel_controller import InfolabelController
from controller.hello_controller import HelloController
from controller.main_controller import MainController
from controller.message_dialog_controller import MessageDialogController
from controller.acm_controller import ACMController
from controller.cashe_controller import CasheController
from classes.tool import Tool


class Handler():

    @staticmethod
    def set_label_image(ui):
        CanvasController.set_label_image(ui)

    # Main
    @staticmethod
    def set_main_dialog(ui):
        MainController.set_main_dialog(ui)

    # メニューバー
    @staticmethod
    def set_button_open(ui):
        ui.clicked.connect(Handler.clicked_button_open)
        FileController.set_button_open(ui)

    @staticmethod
    def set_button_save(ui):
        ui.clicked.connect(Handler.clicked_button_save)
        FileController.set_button_save(ui)

    @staticmethod
    def set_button_save_as_new(ui):
        ui.clicked.connect(Handler.clicked_button_save_as_new)
        FileController.set_button_save_as_new(ui)

    # ユーザー
    def set_combo_box_user(ui):
        ui.currentIndexChanged.connect(Handler.currentIndexChanged_combo_box_user)
        UserController.set_combo_box_user(ui)

    # ヒストグラム
    @staticmethod
    def set_label_histogram(ui):
        HistogramController.set_label_histogram(ui)

    @staticmethod
    def set_slider_max_histogram(ui):
        ui.sliderMoved.connect(Handler.sliderMoved_slider_max_histogram)
        HistogramController.set_slider_max_histogram(ui)

    @staticmethod
    def set_slider_min_histogram(ui):
        ui.sliderMoved.connect(Handler.sliderMoved_slider_min_histogram)
        HistogramController.set_slider_min_histogram(ui)

    @staticmethod
    def set_spin_max_histogram(ui):
        ui.valueChanged.connect(Handler.valueChanged_spin_max_histogram)
        HistogramController.set_spin_max_histogram(ui)

    @staticmethod
    def set_spin_min_histogram(ui):
        ui.valueChanged.connect(Handler.valueChanged_spin_min_histogram)
        HistogramController.set_spin_min_histogram(ui)

    @staticmethod
    def set_slider_index(ui):
        ui.valueChanged.connect(Handler.sliderMoved_slider_index)
        IndexController.set_slider_index(ui)

    @staticmethod
    def set_spin_index(ui):
        ui.valueChanged.connect(Handler.valueChanged_spin_index)
        IndexController.set_spin_index(ui)

    @staticmethod
    def set_label_map(ui):
        MapController.set_label_map(ui)

    @staticmethod
    def set_button_zoom_up(ui):
        ui.clicked.connect(Handler.clicked_button_zoom_up)
        MapController.set_button_zoom_up(ui)

    @staticmethod
    def set_button_zoom_down(ui):
        ui.clicked.connect(Handler.clicked_button_zoom_down)
        MapController.set_button_zoom_up(ui)

    @staticmethod
    def set_button_zoom_default(ui):
        ui.clicked.connect(Handler.clicked_button_zoom_default)
        MapController.set_button_zoom_up(ui)

    @staticmethod
    def set_scroll_bar_x(ui):
        ui.valueChanged.connect(Handler.value_changed_scroll_bar_x)
        MapController.set_scroll_bar_x(ui)

    @staticmethod
    def set_scroll_bar_y(ui):
        ui.valueChanged.connect(Handler.value_changed_scroll_bar_y)
        MapController.set_scroll_bar_y(ui)

    # ラベル系
    @staticmethod
    def set_table_widget_labels(ui):
        ui.itemDoubleClicked.connect(Handler.itemDoubleClicked_table_widget_labels)
        ui.itemClicked.connect(Handler.itemClicked_table_widget_labels)
        ui.itemSelectionChanged.connect(Handler.itemSelectionChanged_table_widget_labels)
        LabelController.set_table_widget_labels(ui)

    @staticmethod
    def set_button_switch_solo_all(ui):
        ui.clicked.connect(Handler.clicked_button_switch_solo_all)
        LabelController.set_button_switch_solo_all(ui)

    @staticmethod
    def set_button_switch_my_everyone(ui):
        ui.clicked.connect(Handler.clicked_button_switch_my_everyone)
        LabelController.set_button_switch_my_everyone(ui)

    @staticmethod
    def set_button_delete_label(ui):
        ui.clicked.connect(Handler.clicked_button_delete_label)
        LabelController.set_button_delete_label(ui)

    @staticmethod
    def set_table_widget_writting(ui):
        ui.itemClicked.connect(Handler.itemClicked_table_widget_writting)
        ui.itemSelectionChanged.connect(Handler.itemSelectionChanged_table_widget_writting)
        LabelController.set_table_widget_writting(ui)

    @staticmethod
    def set_button_delete_writting(ui):
        ui.clicked.connect(Handler.clicked_button_delete_writting)
        LabelController.set_button_delete_writting(ui)

    @staticmethod
    def set_widget_writting(ui):
        LabelController.set_widget_writting(ui)

    #ツールバー
    @staticmethod
    def set_button_corsor(ui):
        ui.clicked.connect(Handler.clicked_button_corsor)
        ToolController.set_button_corsor(ui)

    @staticmethod
    def set_button_pen(ui):
        ui.clicked.connect(Handler.clicked_button_pen)
        ToolController.set_button_pen(ui)

    @staticmethod
    def set_button_pinset(ui):
        ui.clicked.connect(Handler.clicked_button_pinset)
        ToolController.set_button_pinset(ui)

    @staticmethod
    def set_button_eracer(ui):
        ui.clicked.connect(Handler.clicked_button_eracer)
        ToolController.set_button_eracer(ui)

    @staticmethod
    def set_button_tube(ui):
        ui.clicked.connect(Handler.clicked_button_tube)
        ToolController.set_button_tube(ui)

    @staticmethod
    def set_button_snake(ui):
        ui.clicked.connect(Handler.clicked_button_snake)
        ToolController.set_button_snake(ui)

    @staticmethod
    def set_button_levelset(ui):
        ui.clicked.connect(Handler.clicked_button_levelset)
        ToolController.set_button_levelset(ui)

    # ツールボックス
    @staticmethod
    def set_widget_levelset(ui):
        ToolController.set_widget_levelset(ui)

    @staticmethod
    def set_slider_levelset_iteration(ui):
        ui.valueChanged.connect(Handler.sliderMoved_slider_levelset_iteration)
        ACMController.set_slider_levelset_iteration(ui)

    @staticmethod
    def set_slider_levelset_alpha(ui):
        ui.valueChanged.connect(Handler.sliderMoved_slider_levelset_alpha)
        ACMController.set_slider_levelset_alpha(ui)

    @staticmethod
    def set_slider_levelset_lambda(ui):
        ui.valueChanged.connect(Handler.sliderMoved_slider_levelset_lambda)
        ACMController.set_slider_levelset_lambda(ui)

    @staticmethod
    def set_slider_levelset_epsilon(ui):
        ui.valueChanged.connect(Handler.sliderMoved_slider_levelset_epsilon)
        ACMController.set_slider_levelset_epsilon(ui)

    @staticmethod
    def set_slider_levelset_sigma(ui):
        ui.valueChanged.connect(Handler.sliderMoved_slider_levelset_sigma)
        ACMController.set_slider_levelset_sigma(ui)

    @staticmethod
    def set_label_levelset_iteration(ui):
        ACMController.set_label_levelset_iteration(ui)

    @staticmethod
    def set_label_levelset_alpha(ui):
        ACMController.set_label_levelset_alpha(ui)

    @staticmethod
    def set_label_levelset_lambda(ui):
        ACMController.set_label_levelset_lambda(ui)

    @staticmethod
    def set_label_levelset_epsilon(ui):
        ACMController.set_label_levelset_epsilon(ui)

    @staticmethod
    def set_label_levelset_sigma(ui):
        ACMController.set_label_levelset_sigma(ui)

    @staticmethod
    def set_button_levelset_ok(ui):
        ui.clicked.connect(Handler.clicked_button_levelset_ok)
        ACMController.set_button_levelset_ok(ui)

    @staticmethod
    def set_button_levelset_cansel(ui):
        ui.clicked.connect(Handler.clicked_button_levelset_cansel)
        ACMController.set_button_levelset_cansel(ui)


    # ACM関連
    @staticmethod
    def set_progress_bar_levelset(ui):
        ACMController.set_progress_bar_levelset(ui)

    @staticmethod
    def set_hander_completed_levelset():
        ACMController.set_hander_completed_levelset(Handler.completed_levelset)

    @staticmethod
    def set_hander_onesteped_levelset():
        ACMController.set_hander_onesteped_levelset(Handler.onesteped_levelset)


    # 下のラベル
    @staticmethod
    def set_label_info(ui):
        InfolabelController.set_label_info(ui)

    @staticmethod
    def set_text_edit_comments_writting(ui):
        LabelController.set_text_edit_comments(ui)

    @staticmethod
    def set_radio_buttons_writting(uis):
        LabelController.set_radio_buttons(uis)

    @staticmethod
    def set_combo_box_nodule_id_writting(ui):
        LabelController.set_combo_box_nodule_id(ui)

    @staticmethod
    def set_button_ok_writting(ui):
        ui.clicked.connect(Handler.clicked_button_ok_writting)

    # 最初のダイアログ
    @staticmethod
    def set_hello_dialog(ui):
        HelloController.set_hello_dialog(ui)

    @staticmethod
    def set_combo_box_user_hello(ui):
        HelloController.set_combo_box_user_hello(ui)

    @staticmethod
    def set_button_start_hello(ui):
        ui.clicked.connect(Handler.clicked_button_start_hello)


    # メッセージダイアログ
    @staticmethod
    def set_message_dialog(ui):
        MessageDialogController.set_message_dialog(ui)



    #----------------------------------------------------------------------
    # 実行部分
    #----------------------------------------------------------------------
    def initialize():
        MainController.hide_main_dialog()
        UserController.init_users()
        FileController.init_open()
        HelloController.show_hello_dialog()
        Handler.__repaint_from_image()

    # メニューバー
    @staticmethod
    def clicked_button_open():
        FileController.open()
        IndexController.change_image()
        Handler.__repaint_from_image()

    @staticmethod
    def clicked_button_save():
        FileController.save()

    @staticmethod
    def clicked_button_save_as_new():
        FileController.save_as_new()

    # ユーザー
    @staticmethod
    def currentIndexChanged_combo_box_user():
        UserController.changed_current_user()

    # ヒストグラム
    @staticmethod
    def sliderMoved_slider_max_histogram():
        HistogramController.change_max_slider()
        Handler.__repaint_from_histogram()

    @staticmethod
    def sliderMoved_slider_min_histogram():
        HistogramController.change_min_slider()
        Handler.__repaint_from_histogram()

    @staticmethod
    def valueChanged_spin_max_histogram():
        HistogramController.change_max_spin()
        Handler.__repaint_from_histogram()

    @staticmethod
    def valueChanged_spin_min_histogram():
        HistogramController.change_min_spin()
        Handler.__repaint_from_histogram()

    # インデックス
    @staticmethod
    def sliderMoved_slider_index():
        if(not LabelController.is_writting_label()):
            IndexController.change_slider()
        else:
            MessageDialogController.open("You are labeling in this slice now.\n Please finish them after you change z-index.")
        Handler.__repaint_from_index()

    @staticmethod
    def valueChanged_spin_index():
        if(not LabelController.is_writting_label()):
            IndexController.change_spin()
        else:
            MessageDialogController.open("You are labeling in this slice now.\n Please finish them after you change z-index.")
        Handler.__repaint_from_index()



    @staticmethod
    def resize_window():
        MapController.change_window()
        Handler.__repaint_from_zoom()



    #マップ画面内
    @staticmethod
    def zoom_view_press(x, y):
        MapController.drag_start(x, y)
        Handler.__repaint_from_zoom()

    @staticmethod
    def zoom_view_drag(x, y):
        MapController.drag(x, y)
        Handler.__repaint_from_zoom()

    @staticmethod
    def zoom_mouse_wheel(delta):
        MapController.wheel(delta)
        Handler.__repaint_from_zoom()

    #描写画面内
    @staticmethod
    def canvas_mouse_press(x, y):
        if(ToolController.get_tool() == Tool.CORSOR):
            pass
        elif(ToolController.get_tool() == Tool.PEN):
            pass
        elif(ToolController.get_tool() == Tool.PINSET):
            LabelController.pinset_press(x, y)
        elif(ToolController.get_tool() == Tool.ERACER):
            pass
        elif(ToolController.get_tool() == Tool.TUBE):
            pass
        elif(ToolController.get_tool() == Tool.SNAKE):
            ACMController.snake_press(x, y)
        elif(ToolController.get_tool() == Tool.LEVELSET):
            ACMController.levelset_press(x, y)

    @staticmethod
    def canvas_mouse_release(x, y):
        if(ToolController.get_tool() == Tool.CORSOR):
            pass
        elif(ToolController.get_tool() == Tool.PEN):
            LabelController.pen_add(x, y)
        elif(ToolController.get_tool() == Tool.PINSET):
            pass
        elif(ToolController.get_tool() == Tool.ERACER):
            LabelController.eracer_release(x, y)
        elif(ToolController.get_tool() == Tool.TUBE):
            LabelController.tube_add(x, y)
        elif(ToolController.get_tool() == Tool.SNAKE):
            ACMController.snake_release(x, y)
        elif(ToolController.get_tool() == Tool.LEVELSET):
            ACMController.levelset_release(x, y)
        Handler.__repaint_from_label()

    @staticmethod
    def canvas_mouse_move(x, y):
        if(ToolController.get_tool() == Tool.CORSOR):
            pass
        elif(ToolController.get_tool() == Tool.PEN):
            LabelController.pen_move(x, y)
        elif(ToolController.get_tool() == Tool.PINSET):
            LabelController.pinset_move(x, y)
        elif(ToolController.get_tool() == Tool.ERACER):
            LabelController.eracer_move(x, y)
        elif(ToolController.get_tool() == Tool.TUBE):
            LabelController.tube_move(x, y)
        elif(ToolController.get_tool() == Tool.SNAKE):
            pass
        elif(ToolController.get_tool() == Tool.LEVELSET):
            pass

        Handler.__repaint_from_corsor()

    @staticmethod
    def canvas_mouse_drag(x, y):
        if(ToolController.get_tool() == Tool.PINSET):
            LabelController.pinset_drag(x, y)
        elif(ToolController.get_tool() == Tool.SNAKE):
            ACMController.snake_drag(x, y)
        elif(ToolController.get_tool() == Tool.LEVELSET):
            ACMController.levelset_drag(x, y)
        Handler.__repaint_from_zoom()

    @staticmethod
    def canvas_right_mouse_press():
        if(LabelController.is_writting_label()):
            # ポイント付けの終了
            LabelController.pen_end()
        Handler.__repaint_from_label()

    @staticmethod
    def canvas_mouse_wheel(delta):
        MapController.wheel(delta)
        Handler.__repaint_from_zoom()

    @staticmethod
    def clicked_button_zoom_up():
        MapController.zoom_up()
        Handler.__repaint_from_zoom()

    @staticmethod
    def clicked_button_zoom_down():
        MapController.zoom_down()
        Handler.__repaint_from_zoom()

    @staticmethod
    def clicked_button_zoom_default():
        MapController.zoom_default()
        Handler.__repaint_from_zoom()

    @staticmethod
    def value_changed_scroll_bar_x():
        MapController.change_scroll_bar()
        Handler.__repaint_from_zoom()

    @staticmethod
    def value_changed_scroll_bar_y():
        MapController.change_scroll_bar()
        Handler.__repaint_from_zoom()

    @staticmethod
    def clicked_button_ok_writting():
        LabelController.regist_writting_labels()
        Handler.__repaint_from_label_regist_reduce()

    # ラベル関係
    @staticmethod
    def itemDoubleClicked_table_widget_labels(index):
        print("double clicked")
        print(index)

    @staticmethod
    def itemClicked_table_widget_labels(index):
        print("clicked")
        print(index)

    @staticmethod
    def itemSelectionChanged_table_widget_labels():
        if(LabelController.is_writting_label()):
            #ラベリング中
            MessageDialogController.open("You are labeling in this slice now.\n Please finish them after you change label.")
        else:
            Handler.__repaint_from_label()
            LabelController.move_to_current_table_label()
            Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_switch_solo_all():
        LabelController.switch_solo_all()
        Handler.__repaint_from_label_regist_reduce()

    @staticmethod
    def clicked_button_switch_my_everyone():
        LabelController.switch_my_everyone()
        Handler.__repaint_from_label_regist_reduce()

    @staticmethod
    def clicked_button_delete_label():
        LabelController.delete_current_table_label()
        Handler.__repaint_from_label_regist_reduce()

    @staticmethod
    def itemClicked_table_widget_writting(index):
        print("clicked")
        print(index)

    @staticmethod
    def itemSelectionChanged_table_widget_writting():
        if(LabelController.is_writting_label()):
            #ラベリング中
            MessageDialogController.open("You are labeling in this slice now.\n Please finish them after you change label.")
        else:
            Handler.__repaint_from_label()
            LabelController.move_to_current_table_writting()
            Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_delete_writting():
        LabelController.delete_current_table_writting()
        Handler.__repaint_from_label()

    #ツール関係
    @staticmethod
    def clicked_button_corsor():
        ToolController.change_tool(Tool.CORSOR)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_pen():
        ToolController.change_tool(Tool.PEN)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_pinset():
        ToolController.change_tool(Tool.PINSET)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_eracer():
        ToolController.change_tool(Tool.ERACER)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_tube():
        ToolController.change_tool(Tool.TUBE)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_snake():
        ToolController.change_tool(Tool.SNAKE)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    @staticmethod
    def clicked_button_levelset():
        ToolController.change_tool(Tool.LEVELSET)
        ToolController.update_tool()
        Handler.__repaint_from_index()

    # ツールボックス関係
    def sliderMoved_slider_levelset_iteration():
        ACMController.change_levelset_parameters()
        Handler.__repaint_from_corsor()

    def sliderMoved_slider_levelset_alpha():
        ACMController.change_levelset_parameters()
        Handler.__repaint_from_corsor()

    def sliderMoved_slider_levelset_lambda():
        ACMController.change_levelset_parameters()
        Handler.__repaint_from_corsor()

    def sliderMoved_slider_levelset_epsilon():
        ACMController.change_levelset_parameters()
        Handler.__repaint_from_corsor()

    def sliderMoved_slider_levelset_sigma():
        ACMController.change_levelset_parameters()
        Handler.__repaint_from_corsor()

    def clicked_button_levelset_ok():
        ACMController.levelset_regist()
        Handler.__repaint_from_label()

    def clicked_button_levelset_cansel():
        ACMController.levelset_cansel()
        Handler.__repaint_from_label()

    def completed_levelset():
        ACMController.levelset_completed()
        Handler.__repaint_from_label()

    def onesteped_levelset(json_str):
        ACMController.levelset_onesteped(json_str)
        Handler.__repaint_from_label()

    # 最初のダイアログ
    def clicked_button_start_hello():
        HelloController.start_hello()

    # 最初のダイアログ
    def clicked_button_start_hello():
        HelloController.start_hello()
        HelloController.close_hello_dialog()
        UserController.update_combo_box_user()
        MainController.appear_main_dialog()

    #private
    @staticmethod
    def __repaint_from_image():
        ImageController.update_from_image()
        HistogramController.update_from_image()
        CanvasController.update_from_zoom()
        MapController.update_from_zoom()
        ToolController.update_tool()
        LabelController.update_table_widget_labels()
        InfolabelController.update_infolabel()
        IndexController.update_index()
        CasheController.reset_cashe()

    @staticmethod
    def __repaint_from_index():
        ACMController.levelset_cansel()
        LabelController.writting_cansel()

        ImageController.update_from_image()
        HistogramController.update_from_image()
        CanvasController.update_from_zoom()
        MapController.update_from_zoom()
        ToolController.update_tool()
        if(LabelController.is_solo()):
            Handler.__repaint_from_label_regist_reduce()
        else:
            Handler.__repaint_from_label()
        InfolabelController.update_infolabel()
        IndexController.update_index()
        CasheController.reset_cashe()

    @staticmethod
    def __repaint_from_histogram():
        HistogramController.update_from_histogram()
        ImageController.update_from_histogram()
        CanvasController.update_from_zoom()
        MapController.update_from_zoom()
        InfolabelController.update_infolabel()
        CasheController.reset_cashe()

    @staticmethod
    def __repaint_from_zoom():
        CanvasController.update_from_zoom()
        MapController.update_from_zoom()
        InfolabelController.update_infolabel()
        CasheController.reset_cashe()

    @staticmethod
    def __repaint_from_label():
        CanvasController.update_from_maker()
        MapController.update_from_maker()
        LabelController.update_table_widget_labels_nochange_contents()
        ACMController.update_acm()
        InfolabelController.update_infolabel()
        CasheController.reset_cashe()

    @staticmethod
    # 増減するラベルの変更
    def __repaint_from_label_regist_reduce():
        CanvasController.update_from_maker()
        MapController.update_from_maker()
        LabelController.update_table_widget_labels()
        InfolabelController.update_infolabel()
        CasheController.reset_cashe()


    @staticmethod
    def __repaint_from_corsor():
        CanvasController.update_from_maker()
        MapController.update_from_maker()
        InfolabelController.update_infolabel()
        CasheController.reset_cashe()
