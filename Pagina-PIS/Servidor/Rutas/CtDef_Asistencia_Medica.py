from flask import Blueprint, jsonify, request
from Modelos.CtDef_Asistencia_Medica import CtDef_Asistencia_Medica
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_asistenciaMedica = Blueprint('def_asistencia_medica', __name__)

@bp_def_asistenciaMedica.route('/defAsistenciaMedica', methods=['GET'])
def obtener_asistencias_medicas():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_asistenciaMedica = CtDef_Asistencia_Medica.query.filter_by(Cve=Cve).all()
        else:
            def_asistenciaMedica = CtDef_Asistencia_Medica.query.all()

        asistenciasMedicas_dict = [asistenciaMedica.to_dict() for asistenciaMedica in def_asistenciaMedica]
        return jsonify({'Asistencias medicas': asistenciasMedicas_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500