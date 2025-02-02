from flask import Blueprint, jsonify, request
from Modelos.Nacimientos_Por_Ent_Res_2021 import NacimientosPorEntRes2021
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nacimientos_por_ent_res_2021 = Blueprint('nacimientos_por_ent_res_2021', __name__)

@bp_nacimientos_por_ent_res_2021.route('/nacimientosPorEntRes2021', methods=['GET'])
def obtener_nacimientos_por_ent_res_2021():
    try:
        Ent_Fed = request.args.get('Ent_Fed')

        if Ent_Fed:
            nacimientosPorEntRes2021 = NacimientosPorEntRes2021.query.filter_by(Ent_Fed=Ent_Fed).all()
        else:
            nacimientosPorEntRes2021 = NacimientosPorEntRes2021.query.all()

        nacimientosPorEntRes2021_dict = [nacimientosPorEntRes2021.to_dict() for nacimientosPorEntRes2021 in nacimientosPorEntRes2021]
        return jsonify({'Nacimientos por entidad de residencia 2021': nacimientosPorEntRes2021_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500