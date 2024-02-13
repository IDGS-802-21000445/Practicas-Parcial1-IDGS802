from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField

class distancia_form(Form):
    PuntoX1 = StringField("Punto X1")
    PuntoY1 = StringField("Punto Y1")
    PuntoX2 = StringField("Punto X2")
    PuntoY2 = StringField("Punto Y2")


class colores_Form(Form):
    color1 = SelectField('Primera Banda', choices=[('negro', 'Negro'), ('marron', 'Marrón'), ('rojo', 'Rojo'), ('naranja', 'Naranja'), ('amarillo', 'Amarillo'), ('verde', 'Verde'), ('azul', 'Azul'), ('violeta', 'Violeta'), ('gris', 'Gris'), ('blanco', 'Blanco')])
    color2 = SelectField('Segunda Banda', choices=[('negro', 'Negro'), ('marron', 'Marrón'), ('rojo', 'Rojo'), ('naranja', 'Naranja'), ('amarillo', 'Amarillo'), ('verde', 'Verde'), ('azul', 'Azul'), ('violeta', 'Violeta'), ('gris', 'Gris'), ('blanco', 'Blanco')])
    color3 = SelectField('Tercera Banda', choices=[('negro', 'Negro'), ('marron', 'Marrón'), ('rojo', 'Rojo'), ('naranja', 'Naranja'), ('amarillo', 'Amarillo'), ('verde', 'Verde'), ('azul', 'Azul'), ('violeta', 'Violeta'), ('gris', 'Gris'), ('blanco', 'Blanco')])

    color4 = RadioField('Tolerancia', choices=[
        ('dorado', 'Dorado'),
        ('plateado', 'Plateado')
    ])
        

