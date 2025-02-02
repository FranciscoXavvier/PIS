from flask import Blueprint, jsonify, request
from Modelos.CtNac_Lugar_Nacimiento import CtNac_Lugar_Nacimiento
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_lugar_nacimiento = Blueprint('nac_lugar_nacimiento', __name__)

@bp_nac_lugar_nacimiento.route('/nacLugarNacimiento', methods=['GET'])
def obtener_lugares_nacimiento():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_lugarNacimiento = CtNac_Lugar_Nacimiento.query.filter_by(Clave=Clave).all()
        else:
            nac_lugarNacimiento = CtNac_Lugar_Nacimiento.query.all()

        lugarNacimiento_dict = [lugarNacimiento.to_dict() for lugarNacimiento in nac_lugarNacimiento]
        return jsonify({'Lugares de nacimiento': lugarNacimiento_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500