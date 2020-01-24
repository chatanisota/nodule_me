from classes.label import Label

class Research:

    @staticmethod
    def get_labels(file_path):
        with open(file_path) as f:
            df = json.load(f)

        labels_json = df["nodule_me"]["labels"]
        labels = []
        for label_json in labels_json:
            label = Label()
            label.set_json(label_json)
            labels.append(label)
        return labels

    @staticmethod
    def get_area(labels):
        volume = 0
        for label in labels:
            x = points[:,0]
            y = points[:,1]
            S = 0
            # S = Σ|x_i*y_i+1-x_i+1*y_i|
            for i in range(len(points)-1):
                S += x[i]*y[i+1]-x[i-1]*y[i]
            return abs(0)
