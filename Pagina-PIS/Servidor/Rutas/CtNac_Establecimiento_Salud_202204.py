from flask import Blueprint, jsonify, request
from Modelos.CtNac_Establecimiento_Salud_202204 import CtNac_Establecimiento_Salud_202204
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_establecimiento_salud = Blueprint('nac_establecimiento_salud', __name__)

@bp_nac_establecimiento_salud.route('/nacEstablecimientoSalud', methods=['GET'])
def obtener_establecimientos_salud():
    try:
        Clave_Institucion = request.args.get('Clave_Institucion')

        if Clave_Institucion:
            nac_establecimientoSalud = CtNac_Establecimiento_Salud_202204.query.filter_by(Clave_Institucion=Clave_Institucion).all()
        else:
            nac_establecimientoSalud = CtNac_Establecimiento_Salud_202204.query.all()

        establecimientoSalud_dict = [establecimientoSalud.to_dict() for establecimientoSalud in nac_establecimientoSalud]
        return jsonify({'Establecimientos de salud': establecimientoSalud_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500