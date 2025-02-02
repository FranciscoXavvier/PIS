from flask import Blueprint, jsonify, request
from Modelos.CtNac_Ocupacion_Habitual import CtNac_Ocupacion_Habitual
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_ocupacion_habitual = Blueprint('nac_ocupacion_habitual', __name__)

@bp_nac_ocupacion_habitual.route('/nacOcupacionHabitual', methods=['GET'])
def obtener_ocupaciones_habituales():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_ocupacionHabitual = CtNac_Ocupacion_Habitual.query.filter_by(Clave=Clave).all()
        else:
            nac_ocupacionHabitual = CtNac_Ocupacion_Habitual.query.all()

        ocupacionHabitual_dict = [ocupacionHabitual.to_dict() for ocupacionHabitual in nac_ocupacionHabitual]
        return jsonify({'Ocupaciones habituales': ocupacionHabitual_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500