from flask import Blueprint, jsonify, request
from Modelos.CtDef_Causa_Defuncion import CtDef_Causa_Defuncion
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_causaDefuncion = Blueprint('def_causa_defuncion', __name__)

@bp_def_causaDefuncion.route('/defCausaDefuncion', methods=['GET'])
def obtener_causas_defuncion():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_causaDefuncion = CtDef_Causa_Defuncion.query.filter_by(Cve=Cve).all()
        else:
            def_causaDefuncion = CtDef_Causa_Defuncion.query.all()

        causaDefuncion_dict = [causaDefuncion.to_dict() for causaDefuncion in def_causaDefuncion]
        return jsonify({'Causas defunciones': causaDefuncion_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500