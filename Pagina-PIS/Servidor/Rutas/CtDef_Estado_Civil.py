from flask import Blueprint, jsonify, request
from Modelos.CtDef_Estado_Civil import CtDef_Estado_Civil
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_estado_civil = Blueprint('def_estado_civil', __name__)

@bp_def_estado_civil.route('/defEstadoCivil', methods=['GET'])
def obtener_estados_civiles():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_estadoCivil = CtDef_Estado_Civil.query.filter_by(Cve=Cve).all()
        else:
            def_estadoCivil = CtDef_Estado_Civil.query.all()

        estadoCivil_dict = [estadoCivil.to_dict() for estadoCivil in def_estadoCivil]
        return jsonify({'Estados civiles': estadoCivil_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500