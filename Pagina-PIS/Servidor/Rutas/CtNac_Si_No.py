from flask import Blueprint, jsonify, request
from Modelos.CtNac_Si_No import CtNac_Si_No
from sqlalchemy.exc import SQLAlchemyError
import pyodbc


bp_nac_si_no = Blueprint('nac_si_no', __name__)

@bp_nac_si_no.route('/nacSiNo', methods=['GET'])
def obtener_si_no():
    try:
        clave = request.args.get('clave')

        if clave:
            si_no = CtNac_Si_No.query.filter_by(clave=clave).all()
        else:
            si_no = CtNac_Si_No.query.all()
            
        si_no_dict = [valor.to_dict() for valor in si_no]
        return jsonify({'Nacimientos si_no': si_no_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500
