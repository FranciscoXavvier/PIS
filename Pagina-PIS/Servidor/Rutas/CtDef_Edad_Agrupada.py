from flask import Blueprint, jsonify, request
from Modelos.CtDef_Edad_Agrupada import CtDef_Edad_Agrupada
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_edad_agrupada = Blueprint('def_edad_agrupada', __name__)

@bp_def_edad_agrupada.route('/defEdadAgrupada', methods=['GET'])
def obtener_edades_agrupadas():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_edadAgrupada = CtDef_Edad_Agrupada.query.filter_by(Cve=Cve).all()
        else:
            def_edadAgrupada = CtDef_Edad_Agrupada.query.all()

        edadAgrupada_dict = [edadAgrupada.to_dict() for edadAgrupada in def_edadAgrupada]
        return jsonify({'Edades agrupadas': edadAgrupada_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500