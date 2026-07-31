from flask import Blueprint, render_template, request, redirect
from database import mysql

cliente = Blueprint('cliente', __name__)

# mostrar el catalogo
@cliente.route('/cliente')
def catalogo():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM postres")
    lista_postres = cursor.fetchall()
    cursor.close()
    return render_template('cliente/catalogo.html', postres=lista_postres)

# pagina de pedido especifico del postre
@cliente.route('/pedido/<int:postre_id>')
def vista_pedido(postre_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM postres WHERE id = %s", (postre_id,))
    pastel_seleccionado = cursor.fetchone()
    cursor.close()
    
    return render_template('cliente/pedido.html', pastel=pastel_seleccionado)

# guarda el pedido en la base de datos de MySQL
@cliente.route('/pedido/guardar', methods=['POST'])
def guardar_pedido():
    postre_id = request.form.get('postre_id')
    cantidad = request.form.get('cantidad')
    fecha = request.form.get('fecha')
    direccion = request.form.get('direccion')
    
    # asignamos un id por defecto (ej. 1) mientras se desarrolla el login
    id_usuario = 1 
    
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO pedidos (usuario_id, postre_id, cantidad, fecha_entrega, direccion, estado)
        VALUES (%s, %s, %s, %s, %s, 'Pendiente')
    """, (id_usuario, postre_id, cantidad, fecha, direccion))
    mysql.connection.commit()
    cursor.close()
    
    # despues de pedir, lo enviamos de vuelta al catalogo
    return redirect('/cliente')