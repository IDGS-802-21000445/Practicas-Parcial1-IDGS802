from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class distancia_form(Form):
    PuntoX1 = StringField("Punto X1")
    PuntoY1 = StringField("Punto Y1")
    PuntoX2 = StringField("Punto X2")
    PuntoY2 = StringField("Punto Y2")

