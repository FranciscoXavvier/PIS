from flask import Blueprint, jsonify, request
from Modelos.CtNac_Tipo_Cesarea import CtNac_Tipo_Cesarea
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_tipo_cesarea = Blueprint('nac_tipo_cesarea', __name__)

@bp_nac_tipo_cesarea.route('/nacTipoCesarea', methods=['GET'])
def obtener_tipos_cesaeras():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_tipoCesarea = CtNac_Tipo_Cesarea.query.filter_by(Clave=Clave).all()
        else:
            nac_tipoCesarea = CtNac_Tipo_Cesarea.query.all()

        tipoCesarea_dict = [tipoCesarea.to_dict() for tipoCesarea in nac_tipoCesarea]
        return jsonify({'Tipos de cesareas': tipoCesarea_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500