import os

# Configuración de la conexión a la base de datos
DB_SERVER = 'localhost'
DB_NAME = 'InstitutoSalud'
DB_USERNAME = 'sa'
DB_PORT = '1433'
DB_PASSWORD = 'Chivita65.'

# Ruta hacia la carpeta que contiene el archivo odbc.ini
# Se cambió para hacer uso en MacOS
ODBC_SYSINI_FOLDER = '/opt/homebrew/etc/'


# Construcción de la cadena de conexión
# Se cambió para hacer uso en MacOS
## Ruta anteriormente configurada SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server'
SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"


# Configuración de Flask
DEBUG = True

# Configuración de SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuración de la variable de entorno ODBCSYSINI
os.environ['ODBCSYSINI'] = ODBC_SYSINI_FOLDER
