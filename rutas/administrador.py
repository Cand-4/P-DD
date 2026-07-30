from flask import Blueprint, render_template, request, redirect
from database import mysql

administrador = Blueprint('administrador', __name__)

# muestra la tabla con todos los postres actuales
@administrador.route('/administrador')
def panel_admin():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM postres")
    lista_postres = cursor.fetchall()
    cursor.close()
    return render_template('administrador/admin.html', postres=lista_postres)

# recibe datos del formulario web y los guardar en MySQL
@administrador.route('/administrador/guardar', methods=['POST'])
def guardar_postre():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')
    imagen = request.form.get('imagen') # aqui se recibe el nombre del archivo

    cursor = mysql.connection.cursor()
    try:
        cursor.execute("""
            INSERT INTO postres (nombre, descripcion, precio, imagen) 
            VALUES (%s, %s, %s, %s)
        """, (nombre, descripcion, precio, imagen))
        mysql.connection.commit()
    except Exception as e:
        # si el nombre está duplicado, cae aqui y no se rompe el sistema
        print("Error: El postre ya existe o hubo un problema ->", e)
        
    cursor.close()
    return redirect('/administrador')

# borra los postres con un boton
@administrador.route('/administrador/eliminar/<int:id>')
def eliminar_postre(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM postres WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/administrador')