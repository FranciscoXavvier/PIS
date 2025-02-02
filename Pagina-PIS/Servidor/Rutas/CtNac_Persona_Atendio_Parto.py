from flask import Blueprint, jsonify, request
from Modelos.CtNac_Persona_Atendio_Parto import CtNac_Persona_Atendio_Parto
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_persona_atendio_parto = Blueprint('nac_persona_atendio_parto', __name__)

@bp_nac_persona_atendio_parto.route('/nacPersonaAtendioParto', methods=['GET'])
def obtener_personas_atendieron_parto():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_personaAtendioParto = CtNac_Persona_Atendio_Parto.query.filter_by(Clave=Clave).all()
        else:
            nac_personaAtendioParto = CtNac_Persona_Atendio_Parto.query.all()

        personaAtendioParto_dict = [personaAtendioParto.to_dict() for personaAtendioParto in nac_personaAtendioParto]
        return jsonify({'Personas atendieron parto': personaAtendioParto_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500