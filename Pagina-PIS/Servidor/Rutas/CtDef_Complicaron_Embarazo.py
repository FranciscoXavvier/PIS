from flask import Blueprint, jsonify, request
from Modelos.CtDef_Complicaron_Embarazo import CtDef_Complicaron_Embarazo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_complicaron_embarazo = Blueprint('def_complicaron_embarazo', __name__)

@bp_def_complicaron_embarazo.route('/defComplicaronEmbarazo', methods=['GET'])
def obtener_complicaron_embarazos():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_complicaronEmbarazo = CtDef_Complicaron_Embarazo.query.filter_by(Cve=Cve).all()
        else:
            def_complicaronEmbarazo = CtDef_Complicaron_Embarazo.query.all()

        complicaronEmbarazo_dict = [complicaronEmbarazo.to_dict() for complicaronEmbarazo in def_complicaronEmbarazo]
        return jsonify({'Complicaron embarazos': complicaronEmbarazo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500