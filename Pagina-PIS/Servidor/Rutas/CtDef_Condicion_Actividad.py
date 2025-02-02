from flask import Blueprint, jsonify, request
from Modelos.CtDef_Condicion_Actividad import CtDef_Condicion_Actividad
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_condicion_actividad = Blueprint('def_condicion_actividad', __name__)

@bp_def_condicion_actividad.route('/defCondicionActividad', methods=['GET'])
def obtener_condiciones_actividad():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_condicionActividad = CtDef_Condicion_Actividad.query.filter_by(Cve=Cve).all()
        else:
            def_condicionActividad = CtDef_Condicion_Actividad.query.all()

        condicionActividad_dict = [condicionActividad.to_dict() for condicionActividad in def_condicionActividad]
        return jsonify({'Condiciones actividad': condicionActividad_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500