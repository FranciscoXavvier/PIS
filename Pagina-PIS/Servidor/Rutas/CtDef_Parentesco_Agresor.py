from flask import Blueprint, jsonify, request
from Modelos.CtDef_Parentesco_Agresor import CtDef_Parentesco_Agresor
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_parentesco_agresor = Blueprint('def_parentesco_agresor', __name__)

@bp_def_parentesco_agresor.route('/defParentescoAgresor', methods=['GET'])
def obtener_parentescos_agresor():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_parentescoAgresor = CtDef_Parentesco_Agresor.query.filter_by(Cve=Cve).all()
        else:
            def_parentescoAgresor = CtDef_Parentesco_Agresor.query.all()

        parentescoAgresor_dict = [parentescoAgrespr.to_dict() for parentescoAgrespr in def_parentescoAgresor]
        return jsonify({'Parentescos agresor': parentescoAgresor_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500