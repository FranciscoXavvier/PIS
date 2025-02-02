from flask import Blueprint, jsonify, request
from Modelos.Nacimientos_Municipio_Residencia_ocurridos_2022 import Nacimientos_Municipio_Residencia_ocurridos_2022
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nacimientos_municipio_residencia_2022 = Blueprint('nacimientos_municipio_residencia_2022', __name__)

@bp_nacimientos_municipio_residencia_2022.route('/nacimientosMunicipioResidencia2022', methods=['GET'])
def obtener_nacimientos_municipio_residencia_2022():
    try:
        query = Nacimientos_Municipio_Residencia_ocurridos_2022.query

        # Obtener los valores de los parámetros de solicitud
        Entidad_Res = request.args.get('Entidad_Res')
        Municipio_Res = request.args.get('Municipio_Res')

        # Agregar los filtros si los parámetros están presentes
        if Entidad_Res:
            query = query.filter_by(Entidad_Res=Entidad_Res)
        if Municipio_Res:
            query = query.filter_by(Municipio_Res=Municipio_Res)

        nacimientosMunicipioResidencia2022 = query.all()

        nacimientosMunicipioResidencia2022_dict = [nacimientosMunicipioResidencia2022.to_dict() for nacimientosMunicipioResidencia2022 in nacimientosMunicipioResidencia2022]
        return jsonify({'Nacimientos municipio residencia 2022': nacimientosMunicipioResidencia2022_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500