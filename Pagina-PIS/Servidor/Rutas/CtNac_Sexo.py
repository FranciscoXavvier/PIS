from flask import Blueprint, jsonify, request
from Modelos.CtNac_Sexo import CtNac_Sexo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_sexo = Blueprint('nac_sexo', __name__)

@bp_nac_sexo.route('/nacSexo', methods=['GET'])
def obtener_sexos():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_sexo = CtNac_Sexo.query.filter_by(Clave=Clave).all()
        else:
            nac_sexo = CtNac_Sexo.query.all()

        sexo_dict = [sexo.to_dict() for sexo in nac_sexo]
        return jsonify({'Sexos': sexo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500