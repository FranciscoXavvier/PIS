from flask import Blueprint, jsonify, request
from Modelos.CtDef_Entidad_Municipio_Localidad_2020 import CtDef_Entidad_Municipio_Localidad_2020
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_def_entidadMunicipioLocalidad_2020 = Blueprint('def_entidadMunicipioLocalidad_2020', __name__)

@bp_def_entidadMunicipioLocalidad_2020.route('/defEntidadMunicipioLocalidad2020', methods=['GET'])
def obtener_entidades_municipios_localidades_2020():
    try:
        query = CtDef_Entidad_Municipio_Localidad_2020.query

        # Obtener los valores de los parámetros de solicitud
        Cve_Ent = request.args.get('Cve_Ent')
        Cve_Mun = request.args.get('Cve_Mun')
        Cve_Loc = request.args.get('Cve_Loc')

        # Agregar los filtros si los parámetros están presentes
        if Cve_Ent:
            query = query.filter_by(Cve_Ent=Cve_Ent)
        if Cve_Mun:
            query = query.filter_by(Cve_Mun=Cve_Mun)
        if Cve_Loc:
            query = query.filter_by(Cve_Loc=Cve_Loc)

        def_entidadMunicipioLocalidad_2020 = query.all()

        entidadMunicipioLocalidad_2020_dict = [entidadMunicipioLocalidad_2020.to_dict() for entidadMunicipioLocalidad_2020 in def_entidadMunicipioLocalidad_2020]
        return jsonify({'Entidaddes, municipios y localidades': entidadMunicipioLocalidad_2020_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500