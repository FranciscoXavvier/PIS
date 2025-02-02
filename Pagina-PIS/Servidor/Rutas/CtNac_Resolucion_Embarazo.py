from flask import Blueprint, jsonify, request
from Modelos.CtNac_Resolucion_Embarazo import CtNac_Resolucion_Embarazo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_resolucion_embarazo = Blueprint('nac_resolucion_embarazo', __name__)

@bp_nac_resolucion_embarazo.route('/nacResolucionEmbarazo', methods=['GET'])
def obtener_resoluciones_embarazos():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_resolucionEmbarazo = CtNac_Resolucion_Embarazo.query.filter_by(Clave=Clave).all()
        else:
            nac_resolucionEmbarazo = CtNac_Resolucion_Embarazo.query.all()

        resolucionEmbarazo_dict = [resolucionEmbarazo.to_dict() for resolucionEmbarazo in nac_resolucionEmbarazo]
        return jsonify({'Resoluciones embarazo': resolucionEmbarazo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500