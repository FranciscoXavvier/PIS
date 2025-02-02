from flask import Blueprint, jsonify, request
from Modelos.CtNac_Condicion_Hijo_Anterior import CtNac_Condicion_Hijo_Anterior
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_condicion_hijo_anterior = Blueprint('nac_condicion_hijo_anterior', __name__)

@bp_nac_condicion_hijo_anterior.route('/nacCondicionHijoAnterior', methods=['GET'])
def obtener_condiciones_hijos_anteriores():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_condicionHijoAnterior = CtNac_Condicion_Hijo_Anterior.query.filter_by(Clave=Clave).all()
        else:
            nac_condicionHijoAnterior = CtNac_Condicion_Hijo_Anterior.query.all()

        condicionHijoAnterior_dict = [condicionHijoAnterior.to_dict() for condicionHijoAnterior in nac_condicionHijoAnterior]
        return jsonify({'Condiciones hijos anteriores': condicionHijoAnterior_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500