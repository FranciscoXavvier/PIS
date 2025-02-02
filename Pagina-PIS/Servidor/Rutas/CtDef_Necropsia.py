from flask import Blueprint, jsonify, request
from Modelos.CtDef_Necropsia import CtDef_Necropsia
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_necropsia = Blueprint('def_necropsia', __name__)

@bp_def_necropsia.route('/defNecropsia', methods=['GET'])
def obtener_necropsias():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_necropsia = CtDef_Necropsia.query.filter_by(Cve=Cve).all()
        else:
            def_necropsia = CtDef_Necropsia.query.all()

        necropsia_dict = [necropsia.to_dict() for necropsia in def_necropsia]
        return jsonify({'Necropsias': necropsia_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500