from flask import Blueprint, jsonify, request
from Modelos.CtDef_Presunta_Defuncion_Violenta import CtDef_Presunta_Defuncion_Violenta
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_presunta_defuncion_violenta = Blueprint('def_presunta_defuncion_violenta', __name__)

@bp_def_presunta_defuncion_violenta.route('/defPresuntaDefViolenta', methods=['GET'])
def obtener_presunta_defuncion_violenta():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_presuntaDefuncionViolenta = CtDef_Presunta_Defuncion_Violenta.query.filter_by(Cve=Cve).all()
        else:
            def_presuntaDefuncionViolenta = CtDef_Presunta_Defuncion_Violenta.query.all()

        presuntaDefuncionViolenta_dict = [presuntaDefuncionViolenta.to_dict() for presuntaDefuncionViolenta in def_presuntaDefuncionViolenta]
        return jsonify({'Presunta defuncion violenta': presuntaDefuncionViolenta_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500