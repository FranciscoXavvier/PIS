from flask import Blueprint, jsonify, request
from Modelos.Nacimientos_ocurridos_2020 import Nacimientos_ocurridos_2020
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nacimientos_ocurridos_2020 = Blueprint('nacimientos_ocurridos_2020', __name__)

@bp_nacimientos_ocurridos_2020.route('/nacimientosOcurridos2020', methods=['GET'])
def obtener_nacimientos_ocurridos_2020():
    try:
        query = Nacimientos_ocurridos_2020.query

        # Obtener los valores de los parámetros de solicitud
        Entidad_Nacimiento = request.args.get('Entidad_Nacimiento')
        Municipio_Nacimiento = request.args.get('Municipio_Nacimiento')

        # Agregar los filtros si los parámetros están presentes
        if Entidad_Nacimiento:
            query = query.filter_by(Entidad_Nacimiento=Entidad_Nacimiento)
        if Municipio_Nacimiento:
            query = query.filter_by(Municipio_Nacimiento=Municipio_Nacimiento)

        nacimientoOcurrido2020 = query.all()

        nacimientoOcurrido2020_dict = [nacimientoOcurrido2020.to_dict() for nacimientoOcurrido2020 in nacimientoOcurrido2020]
        return jsonify({'Nacimientos ocurridos 2020': nacimientoOcurrido2020_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500