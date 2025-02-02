from flask import Blueprint, jsonify, request
from Modelos.CtDef_Relacion_Con_Embarazo import CtDef_Relacion_Con_Embarazo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_relacion_embarazo = Blueprint('def_relacion_embarazo', __name__)

@bp_def_relacion_embarazo.route('/defRelacionEmbarazo', methods=['GET'])
def obtener_relaciones_con_embarazo():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_relacionEmbarazo = CtDef_Relacion_Con_Embarazo.query.filter_by(Cve=Cve).all()
        else:
            def_relacionEmbarazo = CtDef_Relacion_Con_Embarazo.query.all()

        relacionEmbarazo_dict = [relacionEmbarazo.to_dict() for relacionEmbarazo in def_relacionEmbarazo]
        return jsonify({'Relaciones con embarazo': relacionEmbarazo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500