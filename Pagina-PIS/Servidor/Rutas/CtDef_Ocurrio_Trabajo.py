from flask import Blueprint, jsonify, request
from Modelos.CtDef_Ocurrio_Trabajo import CtDef_Ocurrio_Trabajo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_ocurrio_trabajo = Blueprint('def_ocurrio_trabajo', __name__)

@bp_def_ocurrio_trabajo.route('/defOcurrioTrabajo', methods=['GET'])
def obtener_ocurrio_trabajo():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_ocurrioTrabajo = CtDef_Ocurrio_Trabajo.query.filter_by(Cve=Cve).all()
        else:
            def_ocurrioTrabajo = CtDef_Ocurrio_Trabajo.query.all()

        ocurrioTrabajo_dict = [ocurrioTrabajo.to_dict() for ocurrioTrabajo in def_ocurrioTrabajo]
        return jsonify({'Ocurrio trabajo': ocurrioTrabajo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500