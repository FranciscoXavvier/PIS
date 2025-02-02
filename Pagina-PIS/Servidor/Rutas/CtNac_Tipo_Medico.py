from flask import Blueprint, jsonify, request
from Modelos.CtNac_Tipo_Medico import CtNac_Tipo_Medico
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_tipo_medico = Blueprint('nac_tipo_medico', __name__)

@bp_nac_tipo_medico.route('/nacTipoMedico', methods=['GET'])
def obtener_tipos_medicos():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_tipoMedico = CtNac_Tipo_Medico.query.filter_by(Clave=Clave).all()
        else:
            nac_tipoMedico = CtNac_Tipo_Medico.query.all()

        tipoMedico_dict = [tipoMedico.to_dict() for tipoMedico in nac_tipoMedico]
        return jsonify({'Tipos de medicos': tipoMedico_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500