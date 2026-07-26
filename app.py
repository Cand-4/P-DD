from flask import Flask
from database import mysql

from rutas.acceso import acceso
from rutas.administrador import administrador
from rutas.cliente import cliente
app = Flask(__name__)

# Configuración de MySQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "renta_vehiculos"

# Clave para sesiones que se utilizará más adelante
app.secret_key = "123456"

# Inicializar MySQL
mysql.init_app(app)

#Registrar Blueprints
app.register_blueprint(acceso)
app.register_blueprint(administrador)
app.register_blueprint(cliente)

if __name__ == "__main__":
    app.run(debug=True)
