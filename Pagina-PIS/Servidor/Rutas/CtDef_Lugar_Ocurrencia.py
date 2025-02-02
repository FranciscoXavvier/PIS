from flask import Blueprint, jsonify, request
from Modelos.CtDef_Lugar_Ocurrencia import CtDef_Lugar_Ocurrencia
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_lugar_ocurrencia = Blueprint('def_lugar_ocurrencia', __name__)

@bp_def_lugar_ocurrencia.route('/defLugarOcurrencia', methods=['GET'])
def obtener_lugares_ocurrencia():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_lugarOcurrencia = CtDef_Lugar_Ocurrencia.query.filter_by(Cve=Cve).all()
        else:
            def_lugarOcurrencia = CtDef_Lugar_Ocurrencia.query.all()

        lugarOcurrencia_dict = [lugarOcurrencia.to_dict() for lugarOcurrencia in def_lugarOcurrencia]
        return jsonify({'Lugares de ocurrencia': lugarOcurrencia_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500