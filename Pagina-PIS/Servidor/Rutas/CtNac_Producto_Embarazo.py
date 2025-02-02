from flask import Blueprint, jsonify, request
from Modelos.CtNac_Producto_Embarazo import CtNac_Producto_Embarazo
from sqlalchemy.exc import SQLAlchemyError
import pyodbc

bp_nac_producto_embarazo = Blueprint('nac_producto_embarazo', __name__)

@bp_nac_producto_embarazo.route('/nacProductoEmbarazo', methods=['GET'])
def obtener_productos_embarazo():
    try:
        Clave = request.args.get('Clave')

        if Clave:
            nac_productoEmbarazo = CtNac_Producto_Embarazo.query.filter_by(Clave=Clave).all()
        else:
            nac_productoEmbarazo = CtNac_Producto_Embarazo.query.all()

        productoEmbarazo_dict = [productoEmbarazo.to_dict() for productoEmbarazo in nac_productoEmbarazo]
        return jsonify({'Productos embarazo': productoEmbarazo_dict}), 200
    except SQLAlchemyError as db_error:
        return jsonify({'error': 'Error de conexión a la base de datos: ' + str(db_error)}), 500
    except pyodbc.OperationalError as connection_error:
        return jsonify({'error': 'Error de conexión con el servidor: ' + str(connection_error)}), 500
    except ValueError as value_error:
        return jsonify({'error': 'Error de formato: ' + str(value_error)}), 400
    except Exception as e:
        return jsonify({'error': 'Error desconocido: ' + str(e)}), 500