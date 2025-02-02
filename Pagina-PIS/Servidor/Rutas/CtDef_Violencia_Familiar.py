from flask import Blueprint, jsonify, request
from Modelos.CtDef_Violencia_Familiar import CtDef_Violencia_Familiar
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_violencia_familiar = Blueprint('def_violencia_familiar', __name__)

@bp_def_violencia_familiar.route('/defViolenciaFamiliar', methods=['GET'])
def obtener_violencias_familiares():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_violenciaFamiliar = CtDef_Violencia_Familiar.query.filter_by(Cve=Cve).all()
        else:
            def_violenciaFamiliar = CtDef_Violencia_Familiar.query.all()

        violenciaFamiliar_dict = [violenciaFamiliar.to_dict() for violenciaFamiliar in def_violenciaFamiliar]
        return jsonify({'Violencias familiares': violenciaFamiliar_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500