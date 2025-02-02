from flask import Flask
from config import *
from db import db
from Rutas.Conjunto_Defunciones_2020 import bp_defunciones_2020
from Rutas.Conjunto_Defunciones_2021 import bp_defunciones_2021
from Rutas.Conjunto_Defunciones_2022 import bp_defunciones_2022
from Rutas.CtDef_Anio import bp_def_anio
from Rutas.CtNac_Si_No import bp_nac_si_no
from Rutas.CtDef_Area_Urbana_Rural import bp_def_areaUrbana
from Rutas.CtDef_Asistencia_Medica import bp_def_asistenciaMedica
from Rutas.CtDef_Capitulo_Grupo import bp_def_capituloGrupo
from Rutas.CtDef_Causa_Defuncion import bp_def_causaDefuncion
from Rutas.CtDef_Certificante import bp_def_certificante
from Rutas.CtDef_Complicaron_Embarazo import bp_def_complicaron_embarazo
from Rutas.CtDef_Condicion_Actividad import bp_def_condicion_actividad
from Rutas.CtDef_Condicion_Embarazo import bp_def_condicion_embarazo
from Rutas.CtDef_Derechohabiencia import bp_def_derecho_habiencia
from Rutas.CtDef_Dia import bp_def_dia
from Rutas.CtDef_Edad_Agrupada import bp_def_edad_agrupada
from Rutas.CtDef_Edad import bp_def_edad
from Rutas.CtDef_Entidad_Municipio_Localidad_2020 import bp_def_entidadMunicipioLocalidad_2020
from Rutas.CtDef_Escolaridad import bp_def_escolaridad
from Rutas.CtDef_Estado_Civil import bp_def_estado_civil
from Rutas.CtDef_Grupo_Lista_Mexicana import bp_def_grupo_lista_mexicana
from Rutas.CtDef_Hora import bp_def_hora
from Rutas.CtDef_Lengua_Indigena import bp_def_lengua_indigena
from Rutas.CtDef_Lista1 import bp_def_lista1
from Rutas.CtDef_Lugar_Ocurrencia import bp_def_lugar_ocurrencia
from Rutas.CtDef_Mes import bp_def_mes
from Rutas.CtDef_Minuto import bp_def_minuto
from Rutas.CtDef_Nacionalidad import bp_def_nacionalidad
from Rutas.CtDef_Necropsia import bp_def_necropsia
from Rutas.CtDef_Ocupacion import bp_def_ocupacion
from Rutas.CtDef_Ocurrio_Trabajo import bp_def_ocurrio_trabajo
from Rutas.CtDef_Parentesco_Agresor import bp_def_parentesco_agresor
from Rutas.CtDef_Presunta_Defuncion_Violenta import bp_def_presunta_defuncion_violenta
from Rutas.CtDef_Razon_Materna import bp_def_razon_materna
from Rutas.CtDef_Relacion_Con_Embarazo import bp_def_relacion_embarazo
from Rutas.CtDef_Sexo import bp_def_sexo
from Rutas.CtDef_Sitio_Ocurrencia import bp_def_sitio_ocurrencia
from Rutas.CtDef_Tamaño_Localidad import bp_def_tamaño_localidad
from Rutas.CtDef_Violencia_Familiar import bp_def_violencia_familiar
from Rutas.CtNac_Afiliacion_Certificados import bp_nac_afiliacion_certificados
from Rutas.CtNac_Condicion_Hijo_Anterior import bp_nac_condicion_hijo_anterior
from Rutas.CtNac_Entidades import bp_nac_entidades
from Rutas.CtNac_Escolaridad import bp_nac_escolaridad
from Rutas.CtNac_Establecimiento_Salud_202204 import bp_nac_establecimiento_salud
from Rutas.CtNac_Estado_Conyugal import bp_nac_estado_conyugal
from Rutas.CtNac_Localidades_202203_2 import bp_nac_localidades_202203_2
from Rutas.CtNac_Lugar_Nacimiento import bp_nac_lugar_nacimiento
from Rutas.CtNac_Municipios202201_2 import bp_nac_municipios_202201_2
from Rutas.CtNac_Nacimiento_Certificado_Por import bp_nac_nacimiento_certificado_por
from Rutas.CtNac_Ocupacion_Habitual import bp_nac_ocupacion_habitual
from Rutas.CtNac_Persona_Atendio_Parto import bp_nac_persona_atendio_parto
from Rutas.CtNac_Producto_Embarazo import bp_nac_producto_embarazo
from Rutas.CtNac_Resolucion_Embarazo import bp_nac_resolucion_embarazo
from Rutas.CtNac_Sexo import bp_nac_sexo
from Rutas.CtNac_Tipo_Cesarea import bp_nac_tipo_cesarea
from Rutas.CtNac_Tipo_Medico import bp_nac_tipo_medico
from Rutas.CtNac_Trimestre_Primer_Consulta import bp_nac_trimestre_primer_consulta
from Rutas.CtNac_Utilizo_Forceps import bp_nac_utilizo_forceps
from Rutas.Indicadores_Entidad_Residencia_2020 import bp_indicadores_entidad_residencia_2020
from Rutas.Indicadores_Entidad_Residencia_2021 import bp_indicadores_entidad_residencia_2021
from Rutas.Indicadores_Entidad_Residencia_2022 import bp_indicadores_entidad_residencia_2022
from Rutas.Indicadores_Municipio_Residencia_2020 import bp_indicadores_municipio_residencia_2020
from Rutas.Indicadores_Municipio_Residencia_2021 import bp_indicadores_municipio_residencia_2021
from Rutas.Indicadores_Municipio_Residencia_2022 import bp_indicadores_municipio_residencia_2022
from Rutas.Nacimientos_Entidad_Residencia_ocurridos_2020 import bp_nacimientos_entidad_residencia_2020
from Rutas.Nacimientos_Municipio_Residencia_ocurridos_2020 import bp_nacimientos_municipio_residencia_2020
from Rutas.Nacimientos_Municipio_Residencia_ocurridos_2021 import bp_nacimientos_municipio_residencia_2021
from Rutas.Nacimientos_Municipio_Residencia_ocurridos_2022 import bp_nacimientos_municipio_residencia_2022
from Rutas.Nacimientos_ocurridos_2020 import bp_nacimientos_ocurridos_2020
from Rutas.Nacimientos_ocurridos_2021 import bp_nacimientos_ocurridos_2021
from Rutas.Nacimientos_ocurridos_2022 import bp_nacimientos_ocurridos_2022
from Rutas.Nacimientos_Por_Ent_Res_2020 import bp_nacimientos_por_ent_res_2020
from Rutas.Nacimientos_Por_Ent_Res_2021 import bp_nacimientos_por_ent_res_2021
from Rutas.Poblacion_Municipios_2015_2030 import bp_poblacion_municipios_2015_2030
from Rutas.Población_Por_Entidad_Federativa_2010_2025 import bp_poblacion_por_entidad_federativa_2010_2025

app = Flask(__name__)
app.config.from_object(__name__)
db.init_app(app)

# Decorador @app.after_request
@app.after_request
def after_request(response):
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

app.register_blueprint(bp_defunciones_2020, url_prefix='/PIS')
app.register_blueprint(bp_defunciones_2021, url_prefix='/PIS')
app.register_blueprint(bp_defunciones_2022,url_prefix ='/PIS')
app.register_blueprint(bp_def_anio, url_prefix='/PIS')
app.register_blueprint(bp_nac_si_no, url_prefix='/PIS')
app.register_blueprint(bp_def_areaUrbana, url_prefix='/PIS')
app.register_blueprint(bp_def_asistenciaMedica, url_prefix='/PIS')
app.register_blueprint(bp_def_capituloGrupo, url_prefix='/PIS')
app.register_blueprint(bp_def_causaDefuncion, url_prefix='/PIS')
app.register_blueprint(bp_def_certificante, url_prefix='/PIS')
app.register_blueprint(bp_def_complicaron_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_def_condicion_actividad, url_prefix='/PIS')
app.register_blueprint(bp_def_condicion_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_def_derecho_habiencia, url_prefix='/PIS')
app.register_blueprint(bp_def_dia, url_prefix='/PIS')
app.register_blueprint(bp_def_edad_agrupada, url_prefix='/PIS')
app.register_blueprint(bp_def_edad, url_prefix='/PIS')
app.register_blueprint(bp_def_entidadMunicipioLocalidad_2020, url_prefix='/PIS')
app.register_blueprint(bp_def_escolaridad, url_prefix='/PIS')
app.register_blueprint(bp_def_estado_civil, url_prefix='/PIS')
app.register_blueprint(bp_def_grupo_lista_mexicana, url_prefix='/PIS')
app.register_blueprint(bp_def_hora, url_prefix='/PIS')
app.register_blueprint(bp_def_lengua_indigena, url_prefix='/PIS')
app.register_blueprint(bp_def_lista1, url_prefix='/PIS')
app.register_blueprint(bp_def_lugar_ocurrencia, url_prefix='/PIS')
app.register_blueprint(bp_def_mes, url_prefix='/PIS')
app.register_blueprint(bp_def_minuto, url_prefix='/PIS')
app.register_blueprint(bp_def_nacionalidad, url_prefix='/PIS')
app.register_blueprint(bp_def_necropsia, url_prefix='/PIS')
app.register_blueprint(bp_def_ocupacion, url_prefix='/PIS')
app.register_blueprint(bp_def_ocurrio_trabajo, url_prefix='/PIS')
app.register_blueprint(bp_def_parentesco_agresor, url_prefix='/PIS')
app.register_blueprint(bp_def_presunta_defuncion_violenta, url_prefix='/PIS')
app.register_blueprint(bp_def_razon_materna, url_prefix='/PIS')
app.register_blueprint(bp_def_relacion_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_def_sexo, url_prefix='/PIS')
app.register_blueprint(bp_def_sitio_ocurrencia, url_prefix='/PIS')
app.register_blueprint(bp_def_tamaño_localidad, url_prefix='/PIS')
app.register_blueprint(bp_def_violencia_familiar, url_prefix='/PIS')
app.register_blueprint(bp_nac_afiliacion_certificados, url_prefix='/PIS')
app.register_blueprint(bp_nac_condicion_hijo_anterior, url_prefix='/PIS')
app.register_blueprint(bp_nac_entidades, url_prefix='/PIS')
app.register_blueprint(bp_nac_escolaridad, url_prefix='/PIS')
app.register_blueprint(bp_nac_establecimiento_salud, url_prefix='/PIS')
app.register_blueprint(bp_nac_estado_conyugal, url_prefix='/PIS')
app.register_blueprint(bp_nac_localidades_202203_2, url_prefix='/PIS')
app.register_blueprint(bp_nac_lugar_nacimiento, url_prefix='/PIS')
app.register_blueprint(bp_nac_municipios_202201_2, url_prefix='/PIS')
app.register_blueprint(bp_nac_nacimiento_certificado_por, url_prefix='/PIS')
app.register_blueprint(bp_nac_ocupacion_habitual, url_prefix='/PIS')
app.register_blueprint(bp_nac_persona_atendio_parto, url_prefix='/PIS')
app.register_blueprint(bp_nac_producto_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_nac_resolucion_embarazo, url_prefix='/PIS')
app.register_blueprint(bp_nac_sexo, url_prefix='/PIS')
app.register_blueprint(bp_nac_tipo_cesarea, url_prefix='/PIS')
app.register_blueprint(bp_nac_tipo_medico, url_prefix='/PIS')
app.register_blueprint(bp_nac_trimestre_primer_consulta, url_prefix='/PIS')
app.register_blueprint(bp_nac_utilizo_forceps, url_prefix='/PIS')
app.register_blueprint(bp_indicadores_entidad_residencia_2020, url_prefix='/PIS')
app.register_blueprint(bp_indicadores_entidad_residencia_2021, url_prefix='/PIS')
app.register_blueprint(bp_indicadores_entidad_residencia_2022, url_prefix='/PIS')
app.register_blueprint(bp_indicadores_municipio_residencia_2020, url_prefix='/PIS')
app.register_blueprint(bp_indicadores_municipio_residencia_2021, url_prefix='/PIS')
app.register_blueprint(bp_indicadores_municipio_residencia_2022, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_entidad_residencia_2020, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_municipio_residencia_2020, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_municipio_residencia_2021, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_municipio_residencia_2022, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_ocurridos_2020, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_ocurridos_2021, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_ocurridos_2022, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_por_ent_res_2020, url_prefix='/PIS')
app.register_blueprint(bp_nacimientos_por_ent_res_2021, url_prefix='/PIS')
app.register_blueprint(bp_poblacion_municipios_2015_2030, url_prefix='/PIS')
app.register_blueprint(bp_poblacion_por_entidad_federativa_2010_2025, url_prefix='/PIS')

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada </h1>", 404

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])