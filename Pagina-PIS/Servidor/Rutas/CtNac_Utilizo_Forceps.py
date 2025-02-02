from flask import Blueprint, jsonify, request
from Modelos.CtNac_Utilizo_Forceps import CtNac_Utilizo_Forceps
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_utilizo_forceps = Blueprint('nac_utilizo_forceps', __name__)

@bp_nac_utilizo_forceps.route('/nacUtilizoForceps', methods=['GET'])
def obtener_utilizo_forceps():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_utilizoForceps = CtNac_Utilizo_Forceps.query.filter_by(Clave=Clave).all()
        else:
            nac_utilizoForceps = CtNac_Utilizo_Forceps.query.all()

        utilizoForceps_dict = [utilizoForceps.to_dict() for utilizoForceps in nac_utilizoForceps]
        return jsonify({'Utilizo forceps': utilizoForceps_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500