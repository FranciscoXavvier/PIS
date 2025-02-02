from flask import Blueprint, jsonify, request
from Modelos.CtDef_Anio import CtDef_Anio
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_anio = Blueprint('def_anio', __name__)

@bp_def_anio.route('/defAnio', methods=['GET'])
def obtener_anios():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_anio = CtDef_Anio.query.filter_by(Cve=Cve).all()
        else:
            def_anio = CtDef_Anio.query.all()

        anios_dict = [anio.to_dict() for anio in def_anio]
        return jsonify({'Defunciones por anio': anios_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500
