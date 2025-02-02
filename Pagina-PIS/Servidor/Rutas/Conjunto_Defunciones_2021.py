from flask import Blueprint, jsonify, request
from Modelos.Conjunto_Defunciones_2021 import ConjuntoDeDatosDefuncionesRegistrados2021
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_defunciones_2021 = Blueprint('defunciones_2021', __name__)

@bp_defunciones_2021.route('/defunciones2021', methods=['GET'])
def obtener_defunciones_2021():
    try:
        query = ConjuntoDeDatosDefuncionesRegistrados2021.query

        # Obtener los valores de los parámetros de solicitud
        Ent_ocurr = request.args.get('Ent_ocurr')
        Mun_ocurr = request.args.get('Mun_ocurr')
        Loc_ocurr = request.args.get('Loc_ocurr')

        # Agregar los filtros si los parámetros están presentes
        if Ent_ocurr:
            query = query.filter_by(Ent_ocurr=Ent_ocurr)
        if Mun_ocurr:
            query = query.filter_by(Mun_ocurr=Mun_ocurr)
        if Loc_ocurr:
            query = query.filter_by(Loc_ocurr=Loc_ocurr)

        defunciones2021 = query.all()

        defunciones2021_dict = [defunciones2021.to_dict() for defunciones2021 in defunciones2021]
        return jsonify({'Defunciones de 2021': defunciones2021_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500