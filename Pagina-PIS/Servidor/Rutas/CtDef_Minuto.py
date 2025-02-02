from flask import Blueprint, jsonify, request
from Modelos.CtDef_Minuto import CtDef_Minuto
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_minuto = Blueprint('def_minuto', __name__)

@bp_def_minuto.route('/defMinuto', methods=['GET'])
def obtener_minutos():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_minuto = CtDef_Minuto.query.filter_by(Cve=Cve).all()
        else:
            def_minuto = CtDef_Minuto.query.all()

        minuto_dict = [minuto.to_dict() for minuto in def_minuto]
        return jsonify({'Minutos': minuto_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500