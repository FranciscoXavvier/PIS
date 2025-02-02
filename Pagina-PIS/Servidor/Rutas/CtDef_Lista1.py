from flask import Blueprint, jsonify, request
from Modelos.CtDef_Lista1 import CtDef_Lista1
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_lista1 = Blueprint('def_lista1', __name__)

@bp_def_lista1.route('/defLista1', methods=['GET'])
def obtener_listas1():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_lista1 = CtDef_Lista1.query.filter_by(Cve=Cve).all()
        else:
            def_lista1 = CtDef_Lista1.query.all()

        lista1_dict = [lista1.to_dict() for lista1 in def_lista1]
        return jsonify({'Listas 1': lista1_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500