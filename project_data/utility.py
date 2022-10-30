import pickle
import json
import numpy as np

from project_data import configs

class Species_Recogn():
    def __init__(self, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def LoadModel(self):
        with open (configs.MODEL_FILE_PATH, "rb") as f:
            self.lmodel = pickle.load(f)

        with open (configs.JSON_FILE_PATH, "r") as f:
            self.json_file = json.load(f)

    def Predict_species(self):
        self.LoadModel()

        test_array = np.zeros(len(self.json_file["columns"]))

        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLengthCm
        test_array[3] = self.PetalWidthCm

        print("Predicting species for :", test_array)

        predicted_species = self.lmodel.predict([test_array])[0]
        print("predicted species is:", predicted_species)

        return predicted_species


if "__name__" == "main":
    SepalLengthCm = 6.1
    SepalWidthCm = 3
    PetalLengthCm = 4.6
    PetalWidthCm = 1.4

    pre_species = Species_Recogn(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    pre_species.Predict_species()
