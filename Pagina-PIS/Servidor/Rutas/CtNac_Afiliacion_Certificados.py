from flask import Blueprint, jsonify, request
from Modelos.CtNac_Afiliacion_Certificados import CtNac_Afiliacion_Certificados
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_afiliacion_certificados = Blueprint('nac_afiliacion_certificados', __name__)

@bp_nac_afiliacion_certificados.route('/nacAfiliacionCertificados', methods=['GET'])
def obtener_afiliaciones_certificados():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_afiliacionCertificados = CtNac_Afiliacion_Certificados.query.filter_by(Clave=Clave).all()
        else:
            nac_afiliacionCertificados = CtNac_Afiliacion_Certificados.query.all()

        afiliacionCertificados_dict = [afiliacionCertificados.to_dict() for afiliacionCertificados in nac_afiliacionCertificados]
        return jsonify({'Afiliaciones certificados': afiliacionCertificados_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500