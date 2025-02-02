from flask import Blueprint, jsonify, request
from Modelos.CtDef_Sexo import CtDef_Sexo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_sexo = Blueprint('def_sexo', __name__)

@bp_def_sexo.route('/defSexo', methods=['GET'])
def obtener_sexos():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_sexo = CtDef_Sexo.query.filter_by(Cve=Cve).all()
        else:
            def_sexo = CtDef_Sexo.query.all()

        sexo_dict = [sexo.to_dict() for sexo in def_sexo]
        return jsonify({'Sexos': sexo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500