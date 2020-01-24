from classes.label import Label
from research.research import Research

#MAIN
file_path = argv[1]
labels = Research.get_labels(file_path)
Research.calc_volume(labels)
