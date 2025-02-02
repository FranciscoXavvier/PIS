from flask import Blueprint, jsonify, request
from Modelos.CtDef_Capitulo_Grupo import CtDef_Capitulo_Grupo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_capituloGrupo = Blueprint('def_capitulo_grupo', __name__)

@bp_def_capituloGrupo.route('/defCapituloGrupo', methods=['GET'])
def obtener_capitulos_grupo():
    try:
        Cve = request.args.get('Cve')

        if Cve:
            def_capituloGrupo = CtDef_Capitulo_Grupo.query.filter_by(Cve=Cve).all()
        else:
            def_capituloGrupo = CtDef_Capitulo_Grupo.query.all()

        capitulosGrupo_dict = [capituloGrupo.to_dict() for capituloGrupo in def_capituloGrupo]
        return jsonify({'Capitulos de grupo': capitulosGrupo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500