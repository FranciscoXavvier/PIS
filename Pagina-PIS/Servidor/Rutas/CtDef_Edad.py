from flask import Blueprint, jsonify, request
from Modelos.CtDef_Edad import CtDef_Edad
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_edad = Blueprint('def_edad', __name__)

@bp_def_edad.route('/defEdad', methods=['GET'])
def obtener_edades():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_edad = CtDef_Edad.query.filter_by(Cve=Cve).all()
        else:
            def_edad = CtDef_Edad.query.all()

        edad_dict = [edad.to_dict() for edad in def_edad]
        return jsonify({'Edades': edad_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500