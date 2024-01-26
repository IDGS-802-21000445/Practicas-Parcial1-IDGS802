from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario1.html")


@app.route("/resultado", methods=["POST"])
def calcular():
    if request.method == "POST":
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")
        print(n1,n2)
        
        if operacion == "multiplicacion":
            resultado = n1 * n2
        elif operacion == "suma":
            resultado = n1 + n2
        elif operacion == "resta":
            resultado = n1 - n2
        elif operacion == "division":
            if n2 != 0:
                resultado = n1 / n2
            else:
                return "Error: División por cero"
        else:
            return "Operación no válida"
        
        return render_template("formulario1.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)