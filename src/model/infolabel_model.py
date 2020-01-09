
class InfolabelModel:


    __coordinate = (0,0)

    def get_coordinate(target_pos):
        InfolabelModel.__coordinate = target_pos

    def get_coordinate(target_pos):
        InfolabelModel.__coordinate = target_pos

    def get_text_in_pen():
        return " [PEN] LEFT click : add points."

    def get_text_in_pen_labeling():
        return " [PEN] LEFT click : add points. | RIGHT click: Connect point of start and end."

    def get_text_in_pen_labelings():
        return " [PEN] LEFT click : add points. | RIGHT click: Complete labeling nodule."

    def get_text_in_pinset():
        return " [PINSET] LEFT drag : move point highlghted."

    def get_text_in_eracer():
        return " [ERACER] LEFT click : delete point highlghted."

    def get_text_in_tube():
        return " [TUBE] LEFT click : insert point displayed."
