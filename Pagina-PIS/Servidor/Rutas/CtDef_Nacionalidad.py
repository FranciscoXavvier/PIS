from flask import Blueprint, jsonify, request
from Modelos.CtDef_Nacionalidad import CtDef_Nacionalidad
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_nacionalidad = Blueprint('def_nacionalidad', __name__)

@bp_def_nacionalidad.route('/defNacionalidad', methods=['GET'])
def obtener_nacionalidades():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_nacionalidad = CtDef_Nacionalidad.query.filter_by(Cve=Cve).all()
        else:
            def_nacionalidad = CtDef_Nacionalidad.query.all()

        nacionalidad_dict = [nacionalidad.to_dict() for nacionalidad in def_nacionalidad]
        return jsonify({'Nacionalidades': nacionalidad_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500