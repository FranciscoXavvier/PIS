from flask import Blueprint, jsonify, request
from Modelos.Nacimientos_Por_Ent_Res_2020 import NacimientosPorEntRes2020
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nacimientos_por_ent_res_2020 = Blueprint('nacimientos_por_ent_res_2020', __name__)

@bp_nacimientos_por_ent_res_2020.route('/nacimientosPorEntRes2020', methods=['GET'])
def obtener_nacimientos_por_ent_res_2020():
    try:
        Ent_Fed = request.args.get('Ent_Fed')

        if Ent_Fed:
            nacimientosPorEntRes2020 = NacimientosPorEntRes2020.query.filter_by(Ent_Fed=Ent_Fed).all()
        else:
            nacimientosPorEntRes2020 = NacimientosPorEntRes2020.query.all()

        nacimientosPorEntRes2020_dict = [nacimientosPorEntRes2020.to_dict() for nacimientosPorEntRes2020 in nacimientosPorEntRes2020]
        return jsonify({'Nacimientos por entidad de residencia 2020': nacimientosPorEntRes2020_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500