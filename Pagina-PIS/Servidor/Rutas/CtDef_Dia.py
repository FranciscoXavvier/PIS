from flask import Blueprint, jsonify, request
from Modelos.CtDef_Dia import CtDef_Dia
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_dia = Blueprint('def_dia', __name__)

@bp_def_dia.route('/defDia', methods=['GET'])
def obtener_dias():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_dia = CtDef_Dia.query.filter_by(Cve=Cve).all()
        else:
            def_dia = CtDef_Dia.query.all()

        dia_dict = [dia.to_dict() for dia in def_dia]
        return jsonify({'Dias': dia_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500