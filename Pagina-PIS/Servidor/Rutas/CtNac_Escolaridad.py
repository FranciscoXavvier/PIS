from flask import Blueprint, jsonify, request
from Modelos.CtNac_Escolaridad import CtNac_Escolaridad
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_escolaridad = Blueprint('nac_escolaridad', __name__)

@bp_nac_escolaridad.route('/nacEscolaridad', methods=['GET'])
def obtener_escolaridades():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_escolaridad = CtNac_Escolaridad.query.filter_by(Clave=Clave).all()
        else:
            nac_escolaridad = CtNac_Escolaridad.query.all()

        escolaridad_dict = [escolaridad.to_dict() for escolaridad in nac_escolaridad]
        return jsonify({'Escolaridades': escolaridad_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500