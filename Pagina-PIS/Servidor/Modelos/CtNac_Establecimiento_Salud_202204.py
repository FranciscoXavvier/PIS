from db import db

class CtNac_Establecimiento_Salud_202204(db.Model):
    __tablename__ = 'CtNac_Establecimiento_Salud_202204'
    Id = db.Column(db.Integer, primary_key=True)
    Clues = db.Column(db.String(50), nullable=False)
    Nombre_Entidad = db.Column(db.String(50), nullable=False)
    Clave_Entidad = db.Column(db.SmallInteger, nullable=False)
    Nombre_Municipio = db.Column(db.String(150), nullable=False)
    Clave_Municipio = db.Column(db.SmallInteger, nullable=False)
    Nombre_Localidad = db.Column(db.String(100), nullable=False)
    Clave_Localidad = db.Column(db.SmallInteger, nullable=False)
    Nombre_Jurisdiccion = db.Column(db.String(50), nullable=False)
    Clave_Jurisdiccion = db.Column(db.SmallInteger, nullable=False)
    Nombre_Institucion = db.Column(db.String(100), nullable=False)
    Clave_Institucion = db.Column(db.String(50), nullable=False)
    Nombre_Tipo_Establecimiento = db.Column(db.String(50), nullable=False)
    Clave_Tipo_Establecimiento = db.Column(db.SmallInteger, nullable=False)
    Nombre_Tipologia = db.Column(db.String(200), nullable=False)
    Clave_Tipologia = db.Column(db.String(50), nullable=False)
    Nombre_SubTipologia = db.Column(db.String(150), nullable=False)
    Clave_SubTipologia = db.Column(db.String(50), nullable=False)
    Clave_Scian = db.Column(db.Integer)
    Descripcion_Clave_Scian = db.Column(db.String(150))
    Consultorios_De_Med_Gral = db.Column(db.SmallInteger, nullable=False)
    Consultorios_En_Otras_Areas = db.Column(db.SmallInteger, nullable=False)
    Total_Consultorios = db.Column(db.SmallInteger, nullable=False)
    Camas_En_Area_De_Hos = db.Column(db.SmallInteger, nullable=False)
    Camas_En_Otras_Areas = db.Column(db.SmallInteger, nullable=False)
    Total_Camas = db.Column(db.SmallInteger, nullable=False)
    Nombre_Unidad = db.Column(db.String(200), nullable=False)
    Clave_Vialidad = db.Column(db.SmallInteger)
    Tipo_Vialidad = db.Column(db.String(50))
    Vialidad = db.Column(db.String(200))
    Numero_Exterior = db.Column(db.String(50))
    Numero_Interior = db.Column(db.String(50))
    Clave_Tipo_Asentamiento = db.Column(db.String(100))
    Tipo_Asentamiento = db.Column(db.String(50))
    Asentamiento = db.Column(db.String(200))
    Entre_Tipo_Vialidad_1 = db.Column(db.String(50))
    Entre_Vialidad_1 = db.Column(db.String(100))
    Entre_Tipo_Vialidad_2 = db.Column(db.String(100))
    Entre_Vialidad_2 = db.Column(db.String(100))
    Observaciones_Direccion = db.Column(db.String(500))
    Codigo_Postal = db.Column(db.Integer)
    Estatus_Operacion = db.Column(db.String(50), nullable=False)
    Clave_Estatus_Operacion = db.Column(db.SmallInteger, nullable=False)
    Tiene_Licencia_Sanitaria = db.Column(db.String(50))
    Numero_Licencia_Sanitaria = db.Column(db.String(50))
    Tiene_Aviso_Funcionamiento = db.Column(db.String(50))
    Fecha_Emision_Av_Fun = db.Column(db.Date)
    Rfc_Establecimiento = db.Column(db.String(50))
    Fecha_Construccion = db.Column(db.Date)
    Fecha_Inicio_Operacion = db.Column(db.Date)
    Unidad_Movil_Marca = db.Column(db.String(50))
    Unidad_Movil_Modelo = db.Column(db.String(150))
    Unidad_Movil_Capacidad = db.Column(db.String(50))
    Unidad_Movil_Programa = db.Column(db.String(50))
    Unidad_Movil_Clave_Programa = db.Column(db.String(50))
    Unidad_Movil_Tipo = db.Column(db.String(50))
    Unidad_Movil_Clave_Tipo = db.Column(db.String(50))
    Unidad_Movil_Tipologia = db.Column(db.String(50))
    Unidad_Movil_Clave_Tipologia = db.Column(db.SmallInteger)
    Latitud = db.Column(db.String(50))
    Longitud = db.Column(db.String(50))
    Nombre_Ins_Adm = db.Column(db.String(100))
    Clave_Ins_Adm = db.Column(db.String(50))
    Nivel_Atencion = db.Column(db.String(50), nullable=False)
    Clave_Nivel_Atencion = db.Column(db.SmallInteger, nullable=False)
    Estatus_Acreditacion = db.Column(db.String(50), nullable=False)
    Clave_Estatus_Acreditacion = db.Column(db.String(50), nullable=False)
    Acreditaciones = db.Column(db.String(50))
    SubAcreditacion = db.Column(db.String(50))
    Estrato_Unidad = db.Column(db.String(50), nullable=False)
    Clave_Estrato_Unidad = db.Column(db.SmallInteger, nullable=False)
    Tipo_Obra = db.Column(db.String(50))
    Clave_Tipo_Obra = db.Column(db.SmallInteger)
    Horario_Atencion = db.Column(db.Text)
    Areas_Y_Servicios = db.Column(db.Text)
    Ultimo_Movimiento = db.Column(db.String(50), nullable=False)
    Fecha_Ultimo_Movimiento = db.Column(db.Date)
    Motivo_Baja = db.Column(db.String(50))
    Fecha_Efectiva_Baja = db.Column(db.Date)
    Certificacion_Csg = db.Column(db.String(50), nullable=False)
    Tipo_Certificacion = db.Column(db.String(50), nullable=False)
    Vigencia_Certificacion = db.Column(db.Date)

    def to_dict(self):
        return {
            'Id': self.Id,
            'Clues': self.Clues,
            'Nombre_Entidad': self.Nombre_Entidad,
            'Clave_Entidad': self.Clave_Entidad,
            'Nombre_Municipio': self.Nombre_Municipio,
            'Clave_Municipio': self.Clave_Municipio,
            'Nombre_Localidad': self.Nombre_Localidad,
            'Clave_Localidad': self.Clave_Localidad,
            'Nombre_Jurisdiccion': self.Nombre_Jurisdiccion,
            'Clave_Jurisdiccion': self.Clave_Jurisdiccion,
            'Nombre_Institucion': self.Nombre_Institucion,
            'Clave_Institucion': self.Clave_Institucion,
            'Nombre_Tipo_Establecimiento': self.Nombre_Tipo_Establecimiento,
            'Clave_Tipo_Establecimiento': self.Clave_Tipo_Establecimiento,
            'Nombre_Tipologia': self.Nombre_Tipologia,
            'Clave_Tipologia': self.Clave_Tipologia,
            'Nombre_SubTipologia': self.Nombre_SubTipologia,
            'Clave_SubTipologia': self.Clave_SubTipologia,
            'Clave_Scian': self.Clave_Scian,
            'Descripcion_Clave_Scian': self.Descripcion_Clave_Scian,
            'Consultorios_De_Med_Gral': self.Consultorios_De_Med_Gral,
            'Consultorios_En_Otras_Areas': self.Consultorios_En_Otras_Areas,
            'Total_Consultorios': self.Total_Consultorios,
            'Camas_En_Area_De_Hos': self.Camas_En_Area_De_Hos,
            'Camas_En_Otras_Areas': self.Camas_En_Otras_Areas,
            'Total_Camas': self.Total_Camas,
            'Nombre_Unidad': self.Nombre_Unidad,
            'Clave_Vialidad': self.Clave_Vialidad,
            'Tipo_Vialidad': self.Tipo_Vialidad,
            'Vialidad': self.Vialidad,
            'Numero_Exterior': self.Numero_Exterior,
            'Numero_Interior': self.Numero_Interior,
            'Clave_Tipo_Asentamiento': self.Clave_Tipo_Asentamiento,
            'Tipo_Asentamiento': self.Tipo_Asentamiento,
            'Asentamiento': self.Asentamiento,
            'Entre_Tipo_Vialidad_1': self.Entre_Tipo_Vialidad_1,
            'Entre_Vialidad_1': self.Entre_Vialidad_1,
            'Entre_Tipo_Vialidad_2': self.Entre_Tipo_Vialidad_2,
            'Entre_Vialidad_2': self.Entre_Vialidad_2,
            'Observaciones_Direccion': self.Observaciones_Direccion,
            'Codigo_Postal': self.Codigo_Postal,
            'Estatus_Operacion': self.Estatus_Operacion,
            'Clave_Estatus_Operacion': self.Clave_Estatus_Operacion,
            'Tiene_Licencia_Sanitaria': self.Tiene_Licencia_Sanitaria,
            'Numero_Licencia_Sanitaria': self.Numero_Licencia_Sanitaria,
            'Tiene_Aviso_Funcionamiento': self.Tiene_Aviso_Funcionamiento,
            'Fecha_Emision_Av_Fun': self.Fecha_Emision_Av_Fun,
            'Rfc_Establecimiento': self.Rfc_Establecimiento,
            'Fecha_Construccion': self.Fecha_Construccion,
            'Fecha_Inicio_Operacion': self.Fecha_Inicio_Operacion,
            'Unidad_Movil_Marca': self.Unidad_Movil_Marca,
            'Unidad_Movil_Modelo': self.Unidad_Movil_Modelo,
            'Unidad_Movil_Capacidad': self.Unidad_Movil_Capacidad,
            'Unidad_Movil_Programa': self.Unidad_Movil_Programa,
            'Unidad_Movil_Clave_Programa': self.Unidad_Movil_Clave_Programa,
            'Unidad_Movil_Tipo': self.Unidad_Movil_Tipo,
            'Unidad_Movil_Clave_Tipo': self.Unidad_Movil_Clave_Tipo,
            'Unidad_Movil_Tipologia': self.Unidad_Movil_Tipologia,
            'Unidad_Movil_Clave_Tipologia': self.Unidad_Movil_Clave_Tipologia,
            'Latitud': self.Latitud,
            'Longitud': self.Longitud,
            'Nombre_Ins_Adm': self.Nombre_Ins_Adm,
            'Clave_Ins_Adm': self.Clave_Ins_Adm,
            'Nivel_Atencion': self.Nivel_Atencion,
            'Clave_Nivel_Atencion': self.Clave_Nivel_Atencion,
            'Estatus_Acreditacion': self.Estatus_Acreditacion,
            'Clave_Estatus_Acreditacion': self.Clave_Estatus_Acreditacion,
            'Acreditaciones': self.Acreditaciones,
            'SubAcreditacion': self.SubAcreditacion,
            'Estrato_Unidad': self.Estrato_Unidad,
            'Clave_Estrato_Unidad': self.Clave_Estrato_Unidad,
            'Tipo_Obra': self.Tipo_Obra,
            'Clave_Tipo_Obra': self.Clave_Tipo_Obra,
            'Horario_Atencion': self.Horario_Atencion,
            'Areas_Y_Servicios': self.Areas_Y_Servicios,
            'Ultimo_Movimiento': self.Ultimo_Movimiento,
            'Fecha_Ultimo_Movimiento': self.Fecha_Ultimo_Movimiento,
            'Motivo_Baja': self.Motivo_Baja,
            'Fecha_Efectiva_Baja': self.Fecha_Efectiva_Baja,
            'Certificacion_Csg': self.Certificacion_Csg,
            'Tipo_Certificacion': self.Tipo_Certificacion,
            'Vigencia_Certificacion': self.Vigencia_Certificacion
        }
