from flask import Blueprint, jsonify, request
from Modelos.CtDef_Sitio_Ocurrencia import CtDef_Sitio_Ocurrencia
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_sitio_ocurrencia = Blueprint('def_sitio_ocurrencia', __name__)

@bp_def_sitio_ocurrencia.route('/defSitioOcurrencia', methods=['GET'])
def obtener_sitios_ocurrencia():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_sitioOcurrencia = CtDef_Sitio_Ocurrencia.query.filter_by(Cve=Cve).all()
        else:
            def_sitioOcurrencia = CtDef_Sitio_Ocurrencia.query.all()

        sitioOcurrencia_dict = [sitioOcurrencia.to_dict() for sitioOcurrencia in def_sitioOcurrencia]
        return jsonify({'Sitios ocurrencia': sitioOcurrencia_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500