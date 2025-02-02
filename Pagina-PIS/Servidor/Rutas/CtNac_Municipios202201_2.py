from flask import Blueprint, jsonify, request
from Modelos.CtNac_Municipios_202201_2 import CtNac_Municipios_202201_2
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_municipios_202201_2 = Blueprint('nac_municipios_202201_2', __name__)

@bp_nac_municipios_202201_2.route('/nacMunicipios202201', methods=['GET'])
def obtener_municipios_202201():
    try:
        query = CtNac_Municipios_202201_2.query

        # Obtener los valores de los parámetros de solicitud
        Clave_Ent = request.args.get('Clave_Ent')
        Clave_Mpo = request.args.get('Clave_Mpo')

        # Agregar los filtros si los parámetros están presentes
        if Clave_Ent:
            query = query.filter_by(Clave_Ent=Clave_Ent)
        if Clave_Mpo:
            query = query.filter_by(Clave_Mpo=Clave_Mpo)

        nac_municipios202201 = query.all()

        municipios202201_dict = [municipios202201.to_dict() for municipios202201 in nac_municipios202201]
        return jsonify({'Municipios': municipios202201_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500