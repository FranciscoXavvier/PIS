from flask import Blueprint, jsonify, request
from Modelos.CtDef_Certificante import CtDef_Certificante
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_certificante = Blueprint('def_certificante', __name__)

@bp_def_certificante.route('/defCertificante', methods=['GET'])
def obtener_certificantes():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_certificante = CtDef_Certificante.query.filter_by(Cve=Cve).all()
        else:
            def_certificante = CtDef_Certificante.query.all()

        certificante_dict = [certificante.to_dict() for certificante in def_certificante]
        return jsonify({'Certificantes': certificante_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500