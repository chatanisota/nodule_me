from classes.label import Label
from research.research import Research
import sys

#MAIN
args = sys.argv
file_path = args[1]
file_data = Research.get_file_data(file_path)
labels = Research.get_labels(file_data)
pixel_spacing = Research.get_pixel_spacing(file_data)
slice_thickness = Research.get_slice_thickness(file_data)
print("FILE:           "+str(file_path))
print("labels num:     "+str(len(labels)))
print("pixel spacing:  "+str(pixel_spacing))
print("slice thickness:"+str(slice_thickness))
volume = Research.calc_volume(labels, pixel_spacing, slice_thickness)
print("volume:"+str(volume))
