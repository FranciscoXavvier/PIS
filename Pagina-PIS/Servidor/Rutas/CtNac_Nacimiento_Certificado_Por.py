from flask import Blueprint, jsonify, request
from Modelos.CtNac_Nacimiento_Certificado_Por import CtNac_Nacimiento_Certificado_Por
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_nacimiento_certificado_por = Blueprint('nac_nacimiento_certificado_por', __name__)

@bp_nac_nacimiento_certificado_por.route('/nacNacimientoCertificadoPor', methods=['GET'])
def obtener_certificaciones_nacimientos():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_nacimientoCertificadoPor = CtNac_Nacimiento_Certificado_Por.query.filter_by(Clave=Clave).all()
        else:
            nac_nacimientoCertificadoPor = CtNac_Nacimiento_Certificado_Por.query.all()

        nacimientoCertificadoPor_dict = [nacimientoCertificadoPor.to_dict() for nacimientoCertificadoPor in nac_nacimientoCertificadoPor]
        return jsonify({'Nacimientos certificados por': nacimientoCertificadoPor_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500