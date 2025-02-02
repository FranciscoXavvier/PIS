from flask import Blueprint, jsonify, request
from Modelos.Nacimientos_Entidad_Residencia_ocurridos_2020 import Nacimientos_Entidad_Residencia_ocurridos_2020
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nacimientos_entidad_residencia_2020 = Blueprint('nacimientos_entidad_residencia_2020', __name__)

@bp_nacimientos_entidad_residencia_2020.route('/nacimientosEntidadResidencia2020', methods=['GET'])
def obtener_nacimientos_entidad_residencia_ocurridos_2020():
    try:
        Clv_Residencia = request.args.get('Clv_Residencia')

        if Clv_Residencia:
            nacimientosEntidadResidencia2020 = Nacimientos_Entidad_Residencia_ocurridos_2020.query.filter_by(Clv_Residencia=Clv_Residencia).all()
        else:
            nacimientosEntidadResidencia2020 = Nacimientos_Entidad_Residencia_ocurridos_2020.query.all()

        nacimientosEntidadResidencia2020_dict = [nacimientosEntidadResidencia2020.to_dict() for nacimientosEntidadResidencia2020 in nacimientosEntidadResidencia2020]
        return jsonify({'Nacimientos por entidad residencia 2020': nacimientosEntidadResidencia2020_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500