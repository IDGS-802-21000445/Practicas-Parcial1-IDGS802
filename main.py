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

@app.route("/colores", methods=["GET","POST"])
def colores():
    valor_negativo = 1
    valor_positivo = 1
    valor_resistencia1 = valor_resistencia2 = valor_resistencia3 = ""
    colorHex_1 = colorHex_2 = colorHex_3 = colorHex_4 = ""
    valor = 1 
    colores_Form  =forms.colores_Form(request.form)
    if request.method == 'POST':
        color1= colores_Form.color1.data
        color2= colores_Form.color2.data
        color3= colores_Form.color3.data
        color4= colores_Form.color4.data
        print(color1,color2,color3,color4)

        banda1 = {"negro":0,"marron":1,"rojo" :2,"naranja":3,"amarillo":4,"verde":5,"azul":6,"violeta":7,"gris":8,"blanco":9}
        banda2 = {"negro":0,"marron":1,"rojo" :2,"naranja":3,"amarillo":4,"verde":5,"azul":6,"violeta":7,"gris":8,"blanco":9}
        banda3 = {"negro": 1, "marron": 10, "rojo": 100, "naranja": 1000, "amarillo": 10000, "verde": 100000, "azul": 1000000, "violeta": 100000000, "gris": 1000000000, "blanco": 10000000000}
        colores_hex = {"negro": "#000000", "marron": "#800000", "rojo": "#FF0000", "naranja": "#FFA500","amarillo": "#FFFF00", "verde": "#008000", "azul": "#0000FF", "violeta": "#EE82EE","gris": "#808080", "blanco": "#FFFFFF", "dorado": "#FFD700", "plateado": "#C0C0C0"}

       

        if color1 in banda1 and color1 in colores_hex:
            valor_resistencia1 = banda1[color1]
            colorHex_1 = colores_hex[color1]
            print ("color Hexadecimal" ,colorHex_1)
            print("color1 ", valor_resistencia1)
        if color2 in banda2 and color2 in colores_hex:
            valor_resistencia2 = banda2[color2]
            colorHex_2 = colores_hex[color2]
            print ("color Hexadecimal",colorHex_2)
            print("color2: ", valor_resistencia2)
        if color3 in banda3 and color3 in colores_hex:
            valor_resistencia3 = banda3[color3]
            colorHex_3 = colores_hex[color3]
            print("color hexadecimal",colorHex_3)
            print("color3", valor_resistencia3)    

        valor_concatenado = str(valor_resistencia1) + str(valor_resistencia2)
        print(valor_concatenado)
        valor = int(valor_concatenado) * valor_resistencia3
        print(valor)

        

        if color4 == "dorado" and color4 in colores_hex:
            valor_doraCal = valor * 0.05
            print(valor_doraCal)
            valor_positivo = valor + valor_doraCal
            print(valor_positivo)

            valor_negativo = valor - valor_doraCal
            print(valor_negativo)
            colorHex_4 = colores_hex[color4]
            print(colorHex_4)
        elif color4 == "plateado":
            valor_plataCal = valor * 0.10
            print(valor_plataCal)
            valor_positivo = valor + valor_plataCal
            print(valor_positivo)

            valor_negativo = valor - valor_plataCal
            print(valor_negativo)
            colorHex_4 = colores_hex[color4]
            print(colorHex_4)

        
    return render_template("colores_Resistencia.html", form=colores_Form, valor_positivo=valor_positivo, valor_negativo=valor_negativo,valor = valor, colorHex_1=colorHex_1, colorHex_2=colorHex_2, colorHex_3=colorHex_3, colorHex_4=colorHex_4)

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