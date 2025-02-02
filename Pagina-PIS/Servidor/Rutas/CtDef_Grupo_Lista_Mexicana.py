from flask import Blueprint, jsonify, request
from Modelos.CtDef_Grupo_Lista_Mexicana import CtDef_Grupo_Lista_Mexicana
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_grupo_lista_mexicana = Blueprint('def_grupo_lista_mexicana', __name__)

@bp_def_grupo_lista_mexicana.route('/defListaMexicana', methods=['GET'])
def obtener_grupos_listas_mexicanas():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_listaMexicana = CtDef_Grupo_Lista_Mexicana.query.filter_by(Cve=Cve).all()
        else:
            def_listaMexicana = CtDef_Grupo_Lista_Mexicana.query.all()

        listaMexicana_dict = [listaMexicana.to_dict() for listaMexicana in def_listaMexicana]
        return jsonify({'Grupo de listas mexicanas': listaMexicana_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500