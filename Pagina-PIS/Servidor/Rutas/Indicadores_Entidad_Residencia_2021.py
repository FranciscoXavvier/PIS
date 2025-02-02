from flask import Blueprint, jsonify, request
from Modelos.Indicadores_Entidad_Residencia_2021 import Indicadores_Entidad_Residencia_2021
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_indicadores_entidad_residencia_2021 = Blueprint('indicadores_entidad_residencia_2021', __name__)

@bp_indicadores_entidad_residencia_2021.route('/indicadoresEntidadResidencia2021', methods=['GET'])
def obtener_indicadores_entidad_residencia_2021():
    try:
        query = Indicadores_Entidad_Residencia_2021.query

        Clave_Ent = request.args.get('Clave_Ent')

        # Agregar los filtros si los parámetros están presentes
        if Clave_Ent:
            query = query.filter_by(Clave_EntFed=Clave_Ent)

        indicadoresEntidadResidencia2021 = query.all()

        indicadoresEntidadResidencia2021_dict = [indicadoresEntidadResidencia2021.to_dict_subset1() for indicadoresEntidadResidencia2021 in indicadoresEntidadResidencia2021]
        return jsonify({'Indicadores Subset1': indicadoresEntidadResidencia2021_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500


@bp_indicadores_entidad_residencia_2021.route('/indicadoresEntidadResidencia2021/subset2', methods=['GET'])
def obtenerindicadores_entidad_residencia_2021_subset2():
    try:
        query = Indicadores_Entidad_Residencia_2021.query

        Clave_Ent = request.args.get('Clave_Ent')

        # Agregar los filtros si los parámetros están presentes
        if Clave_Ent:
            query = query.filter_by(Clave_EntFed=Clave_Ent)
            
        indicadoresEntidadResidencia2021 = query.all()

        indicadoresEntidadResidencia2021_dict = [indicadoresEntidadResidencia2021.to_dict_subset2() for indicadoresEntidadResidencia2021 in indicadoresEntidadResidencia2021]
        return jsonify({'Indicadores Subset2': indicadoresEntidadResidencia2021_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500
