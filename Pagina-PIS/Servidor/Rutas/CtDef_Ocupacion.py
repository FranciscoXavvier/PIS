from flask import Blueprint, jsonify, request
from Modelos.CtDef_Ocupacion import CtDef_Ocupacion
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_ocupacion = Blueprint('def_ocupacion', __name__)

@bp_def_ocupacion.route('/defOcupacion', methods=['GET'])
def obtener_ocupaciones():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_ocupacion = CtDef_Ocupacion.query.filter_by(Cve=Cve).all()
        else:
            def_ocupacion = CtDef_Ocupacion.query.all()

        ocupacion_dict = [ocupacion.to_dict() for ocupacion in def_ocupacion]
        return jsonify({'Ocupaciones': ocupacion_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500