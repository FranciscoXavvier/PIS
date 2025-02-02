from flask import Blueprint, jsonify, request
from Modelos.CtDef_Tamaño_Localidad import CtDef_Tamaño_Localidad
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_tamaño_localidad = Blueprint('def_tamaño_localidad', __name__)

@bp_def_tamaño_localidad.route('/defTamanioLocalidad', methods=['GET'])
def obtener_tamaños_localidad():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_tamañoLocalidad = CtDef_Tamaño_Localidad.query.filter_by(Cve=Cve).all()
        else:
            def_tamañoLocalidad = CtDef_Tamaño_Localidad.query.all()

        tamañoLocalidad_dict = [tamañoLocalidad.to_dict() for tamañoLocalidad in def_tamañoLocalidad]
        return jsonify({'Tamaños de localidad': tamañoLocalidad_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500