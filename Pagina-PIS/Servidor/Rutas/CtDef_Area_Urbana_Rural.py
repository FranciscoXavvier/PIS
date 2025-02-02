from flask import Blueprint, jsonify, request
from Modelos.CtDef_Area_Urbana_Rural import CtDef_Area_Urbana_Rural
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_areaUrbana = Blueprint('def_area_urbana_rural', __name__)

@bp_def_areaUrbana.route('/defAreaUrbanaRural', methods=['GET'])
def obtener_areas_urbanas_rurales():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_areaUrbana = CtDef_Area_Urbana_Rural.query.filter_by(Cve=Cve).all()
        else:
            def_areaUrbana = CtDef_Area_Urbana_Rural.query.all()

        areasUrbanas_dict = [areaUrbana.to_dict() for areaUrbana in def_areaUrbana]
        return jsonify({'Areas urbanas rurales': areasUrbanas_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500