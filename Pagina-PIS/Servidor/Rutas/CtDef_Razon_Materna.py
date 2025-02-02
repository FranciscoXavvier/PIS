from flask import Blueprint, jsonify, request
from Modelos.CtDef_Razon_Materna import CtDef_Razon_Materna
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_razon_materna = Blueprint('def_razon_materna', __name__)

@bp_def_razon_materna.route('/defRazonMaterna', methods=['GET'])
def obtener_razones_maternas():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_razonMaterna = CtDef_Razon_Materna.query.filter_by(Cve=Cve).all()
        else:
            def_razonMaterna = CtDef_Razon_Materna.query.all()

        razonMaterna_dict = [razonMaterna.to_dict() for razonMaterna in def_razonMaterna]
        return jsonify({'Razones maternas': razonMaterna_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500