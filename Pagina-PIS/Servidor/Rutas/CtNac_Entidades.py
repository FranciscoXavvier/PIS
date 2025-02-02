from flask import Blueprint, jsonify, request
from Modelos.CtNac_Entidades import CtNac_Entidades
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_entidades = Blueprint('nac_entidades', __name__)

@bp_nac_entidades.route('/nacEntidades', methods=['GET'])
def obtener_entidades():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_entidades = CtNac_Entidades.query.filter_by(Clave=Clave).all()
        else:
            nac_entidades = CtNac_Entidades.query.all()

        entidades_dict = [entidades.to_dict() for entidades in nac_entidades]
        return jsonify({'Entidades': entidades_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500