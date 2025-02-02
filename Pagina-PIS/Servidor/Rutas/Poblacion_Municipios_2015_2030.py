from flask import Blueprint, jsonify, request
from Modelos.Poblacion_Municipios_2015_2030 import PoblacionMunicipios2015_2030
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_poblacion_municipios_2015_2030 = Blueprint('poblacion_municipios_2015_2030', __name__)

@bp_poblacion_municipios_2015_2030.route('/poblacionMunicipios20152030', methods=['GET'])
def obtener_poblacion_municipios_2015_2030():
    try:
        query = PoblacionMunicipios2015_2030.query

        # Obtener los valores de los parámetros de solicitud
        Anio = request.args.get('Anio')
        Ent_Fed = request.args.get('Ent_Fed')
        Municipio = request.args.get('Municipio')

        # Agregar los filtros si los parámetros están presentes
        if Anio:
            query = query.filter_by(Anio=Anio)
        if Ent_Fed:
            query = query.filter_by(Ent_Fed=Ent_Fed)
        if Municipio:
            query = query.filter_by(Municipio=Municipio)

        poblacionMunicipios20152030 = query.all()

        poblacionMunicipios20152030_dict = [poblacionMunicipios20152030.to_dict() for poblacionMunicipios20152030 in poblacionMunicipios20152030]
        return jsonify({'Poblacion por municipio': poblacionMunicipios20152030_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500