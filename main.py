from flask import Flask,request,render_template

import forms
import math

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario1.html")

@app.route("/distancia", methods=["GET","POST"])
def distancia():
    dis_puntos  =forms.distancia_form(request.form)
    resultado = 1
    if request.method == 'POST':
        PuntoX1= dis_puntos.PuntoX1.data
        PuntoY1= dis_puntos.PuntoY1.data
        PuntoX2= dis_puntos.PuntoX2.data
        PuntoY2= dis_puntos.PuntoY2.data
        raiz = math.sqrt((float(PuntoX2)-float(PuntoX1))**2+(float(PuntoY2)-float(PuntoY1))**2)
        resultado = raiz
        print(resultado)
    return render_template("distanciaDosPuntos.html", form=dis_puntos, resultado = resultado)


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