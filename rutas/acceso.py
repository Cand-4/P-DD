from flask import Blueprint, render_template, request, redirect

acceso = Blueprint('acceso', __name__)

# ruta para mostrar la pantalla de Inicio de Sesión
@acceso.route('/')
def inicio():
    return render_template('acceso/index.html')

# procesa el botón ingresar
@acceso.route('/login', methods=['POST'])
def login():
    # aquí se validará el correo y contraseña con MySQL
    correo = request.form.get('correo')
    clave = request.form.get('clave')
    
    # Para avanzar entre pantallas, temporalmente
    return redirect('/cliente')