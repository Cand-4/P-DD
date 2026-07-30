from flask import Blueprint, render_template
from database import mysql

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente')
def catalogo():
    # abrimos la conexion y buscamos los postres
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM postres")
    lista_postres = cursor.fetchall()
    cursor.close()
    
    # enviamos esa lista al archivo HTML
    return render_template('cliente/catalogo.html', postres=lista_postres)