from flask import Blueprint, jsonify, request
from Modelos.Conjunto_Defunciones_2020 import ConjuntoDeDatosDefuncionesRegistrados2020
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_defunciones_2020 = Blueprint('defunciones_2020', __name__)

@bp_defunciones_2020.route('/defunciones2020', methods=['GET'])
def obtener_defunciones_2020():
    try:
        query = ConjuntoDeDatosDefuncionesRegistrados2020.query

        # Obtener los valores de los parámetros de solicitud
        Causa_def = request.args.get('Causa_def')
        Ent_ocurr = request.args.get('Ent_ocurr')
        Mun_ocurr = request.args.get('Mun_ocurr')
        Loc_ocurr = request.args.get('Loc_ocurr')

        # Agregar los filtros si los parámetros están presentes
        if Causa_def:
            query = query.filter_by(Causa_def=Causa_def)
        if Ent_ocurr:
            query = query.filter_by(Ent_ocurr=Ent_ocurr)
        if Mun_ocurr:
            query = query.filter_by(Mun_ocurr=Mun_ocurr)
        if Loc_ocurr:
            query = query.filter_by(Loc_ocurr=Loc_ocurr)

        defunciones2020 = query.all()

        defunciones2020_dict = [defunciones2020.to_dict() for defunciones2020 in defunciones2020]
        return jsonify({'Defunciones de 2020': defunciones2020_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500