from flask import Flask, request, render_template
from project_data import utility

app = Flask(__name__)

@app.route("/")
def HomeAPI():
    print("Home API:")

    return render_template("User_input.html")

@app.route("/result", methods = ["POST", "GET"])
def Result():
    if request.method == "POST":
        data = request.form
        SepalLengthCm = data["SepalLengthCm"]
        SepalWidthCm = data["SepalWidthCm"]
        PetalLengthCm = data["PetalLengthCm"]
        PetalWidthCm = data["PetalWidthCm"]

    species_find = utility.Species_Recogn(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    species = species_find.Predict_species()


    return render_template("home.html", species = species)
if __name__ == "__main__":
    app.run()