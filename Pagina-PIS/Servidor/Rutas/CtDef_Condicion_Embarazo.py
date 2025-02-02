from flask import Blueprint, jsonify, request
from Modelos.CtDef_Condicion_Embarazo import CtDef_Condicion_Embarazo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_condicion_embarazo = Blueprint('def_condicion_embarazo', __name__)

@bp_def_condicion_embarazo.route('/defCondicionEmbarazo', methods=['GET'])
def obtener_condiciones_embarazo():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_condicionEmbarazo = CtDef_Condicion_Embarazo.query.filter_by(Cve=Cve).all()
        else:
            def_condicionEmbarazo = CtDef_Condicion_Embarazo.query.all()

        condicionEmbarazo_dict = [condicionEmbarazo.to_dict() for condicionEmbarazo in def_condicionEmbarazo]
        return jsonify({'Condiciones embarazo': condicionEmbarazo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500