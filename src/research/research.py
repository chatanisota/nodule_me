from classes.label import Label
import json
import numpy as np

class Research:

    @staticmethod
    def get_file_data(file_path):
        with open(file_path) as f:
            file_data = json.load(f)
        return file_data

    @staticmethod
    def get_labels(file_data):

        labels_json = file_data["nodule_me"]["labels"]
        labels = []
        for label_json in labels_json:
            label = Label()
            label.set_json(label_json)
            labels.append(label)
        return labels

    @staticmethod
    def get_pixel_spacing(file_data):
        pixel_spacing = file_data["PixelSpacing"]
        return pixel_spacing

    @staticmethod
    def get_slice_thickness(file_data):
        slice_thickness = file_data["SliceThickness"]
        return slice_thickness

    @staticmethod
    def calc_volume(labels, pixel_spacing, slice_thickness):
        volumes = {}
        nodule_ids = []
        #pixel_spacing = [1,1]

        for label in labels:
            volume = 0
            nodule_id = label.get_nodule_id()
            if(nodule_id in nodule_ids):
                volume = volumes[str(nodule_id)]
            else:
                nodule_ids.append(nodule_id)
            points = label.get_points()
            x = points[:,0]
            y = points[:,1]
            x = np.append(x,points[0,0])
            y = np.append(y,points[0,1])
            x = x * pixel_spacing[0]
            y = y * pixel_spacing[1]

            S = 0
            # S = Σ|x_i*y_i+1-x_i+1*y_i|
            for i in range(len(points)):
                S += x[i]*y[i+1]-x[i+1]*y[i]
            S = abs(S)/2
            volume += S * slice_thickness
            volumes[str(nodule_id)] = volume

        return volumes
