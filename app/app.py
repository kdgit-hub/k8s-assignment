from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = ""
    color = ""
    if request.method == "POST":
        try:
            height_feet = float(request.form["height"])
            weight = float(request.form["weight"])
            height_m = height_feet * 0.3048  # convert feet to meters
            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
                color = "blue"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
                color = "green"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "orange"
            else:
                category = "Obese"
                color = "red"

        except Exception as e:
            bmi = "Invalid Input"
            color = "gray"
            category = str(e)
    return render_template("index.html", bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)