from flask import Blueprint, jsonify, request
from Modelos.CtNac_Estado_Conyugal import CtNac_Estado_Conyugal
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_estado_conyugal = Blueprint('nac_estado_conyugal', __name__)

@bp_nac_estado_conyugal.route('/nacEstadoConyugal', methods=['GET'])
def obtener_estados_conyugales():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_estadoConyugal = CtNac_Estado_Conyugal.query.filter_by(Clave=Clave).all()
        else:
            nac_estadoConyugal = CtNac_Estado_Conyugal.query.all()

        estadoConyugal_dict = [estadoConyugal.to_dict() for estadoConyugal in nac_estadoConyugal]
        return jsonify({'Estados conyugales': estadoConyugal_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500