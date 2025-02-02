from flask import Blueprint, jsonify, request
from Modelos.CtDef_Lengua_Indigena import CtDef_Lengua_Indigena
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_lengua_indigena = Blueprint('def_lengua_indigena', __name__)

@bp_def_lengua_indigena.route('/defLenguaIndigena', methods=['GET'])
def obtener_lenguas_indigenas():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_lenguaIndigena = CtDef_Lengua_Indigena.query.filter_by(Cve=Cve).all()
        else:
            def_lenguaIndigena = CtDef_Lengua_Indigena.query.all()

        lenguaIndigena_dict = [lenguaIndigena.to_dict() for lenguaIndigena in def_lenguaIndigena]
        return jsonify({'Lenguas indigenas': lenguaIndigena_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500