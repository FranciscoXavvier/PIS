from flask import Blueprint, jsonify, request
from Modelos.CtNac_Trimestre_Primer_Consulta import CtNac_Trimestre_Primer_Consulta
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_trimestre_primer_consulta = Blueprint('nac_trimestre_primer_consulta', __name__)

@bp_nac_trimestre_primer_consulta.route('/nacTrimestrePrimerConsulta', methods=['GET'])
def obtener_trimestre_primer_consulta():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_trimestrePrimerConsulta = CtNac_Trimestre_Primer_Consulta.query.filter_by(Clave=Clave).all()
        else:
            nac_trimestrePrimerConsulta = CtNac_Trimestre_Primer_Consulta.query.all()

        trimestrePrimerConsulta_dict = [trimestrePrimerConsulta.to_dict() for trimestrePrimerConsulta in nac_trimestrePrimerConsulta]
        return jsonify({'Trimestre primer consulta': trimestrePrimerConsulta_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500