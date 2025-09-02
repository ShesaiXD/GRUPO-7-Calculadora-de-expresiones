from flask import Flask, render_template, request
from calculadora import evaluar_expresion

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    error = None

    if request.method == "POST":
        expresion = request.form.get("expresion")

        try:
            resultado = evaluar_expresion(expresion)
        except ValueError as e:
            error = str(e)

    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(debug=True)
