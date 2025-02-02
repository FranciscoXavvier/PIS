from flask import Blueprint, jsonify, request
from Modelos.Población_Por_Entidad_Federativa_2010_2025 import PoblacionPorEntidadFederativa2010_2025
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_poblacion_por_entidad_federativa_2010_2025 = Blueprint('poblacion_por_entidad_federativa_2010_2025', __name__)

@bp_poblacion_por_entidad_federativa_2010_2025.route('/poblacionEntidadFederativa20102025', methods=['GET'])
def obtener_poblacion_entidad_feredativa_2010_2025():
    try:
        query = PoblacionPorEntidadFederativa2010_2025.query

        # Obtener los valores de los parámetros de solicitud
        Anio = request.args.get('Anio')
        Clave_EntFed = request.args.get('Clave_EntFed')

        # Agregar los filtros si los parámetros están presentes
        if Anio:
            query = query.filter_by(Anio=Anio)
        if Clave_EntFed:
            query = query.filter_by(Clave_EntFed=Clave_EntFed)

        poblacionEntidadFederativa20102025 = query.all()

        poblacionEntidadFederativa20102025_dict = [poblacionEntidadFederativa20102025.to_dict() for poblacionEntidadFederativa20102025 in poblacionEntidadFederativa20102025]
        return jsonify({'Poblacion por entidad federativa 2010 - 2025': poblacionEntidadFederativa20102025_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500