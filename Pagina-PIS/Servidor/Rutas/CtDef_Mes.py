from flask import Blueprint, jsonify, request
from Modelos.CtDef_Mes import CtDef_Mes
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_mes = Blueprint('def_mes', __name__)

@bp_def_mes.route('/defMes', methods=['GET'])
def obtener_meses():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_mes = CtDef_Mes.query.filter_by(Cve=Cve).all()
        else:
            def_mes = CtDef_Mes.query.all()

        mes_dict = [mes.to_dict() for mes in def_mes]
        return jsonify({'Meses': mes_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500