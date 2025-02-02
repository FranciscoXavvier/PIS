from flask import Blueprint, jsonify, request
from Modelos.CtNac_Localidades_202203_2 import CtNac_Localidades_202203_2
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_localidades_202203_2 = Blueprint('nac_localidades_202203_2', __name__)

@bp_nac_localidades_202203_2.route('/nacLocalidades202203', methods=['GET'])
def obtener_localidades_202203():
    try:
        query = CtNac_Localidades_202203_2.query

        # Obtener los valores de los parámetros de solicitud
        Cve_Ent = request.args.get('Cve_Ent')
        Cve_Mun = request.args.get('Cve_Mun')
        Cve_Loc = request.args.get('Cve_Loc')

        # Agregar los filtros si los parámetros están presentes
        if Cve_Ent:
            query = query.filter_by(Cve_Ent=Cve_Ent)
        if Cve_Mun:
            query = query.filter_by(Cve_Mun=Cve_Mun)
        if Cve_Loc:
            query = query.filter_by(Cve_Loc=Cve_Loc)

        nac_localidades202203 = query.all()

        localidades202203_dict = [localidades202203.to_dict() for localidades202203 in nac_localidades202203]
        return jsonify({'Localidades': localidades202203_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500