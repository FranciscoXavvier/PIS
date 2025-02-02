from db import db

class Nacimientos_ocurridos_2021(db.Model):
    __tablename__ = 'Nacimientos_ocurridos_2021'
    IdNacimiento = db.Column(db.Integer, primary_key=True)
    Nacio_Extranjero = db.Column(db.SmallInteger, nullable=False)
    Entidad_Nacimiento = db.Column(db.SmallInteger, nullable=False)
    Municipio_Nacimiento = db.Column(db.SmallInteger, nullable=False)
    Edad = db.Column(db.SmallInteger, nullable=False)
    Se_Considera_Indigena = db.Column(db.SmallInteger, nullable=False)
    Habla_Lengua_Indigena = db.Column(db.SmallInteger, nullable=False)
    Fecha_Nacimiento_Madre = db.Column(db.String(20))
    Estado_Conyugal = db.Column(db.SmallInteger, nullable=False)
    Reside_Extranjero = db.Column(db.SmallInteger, nullable=False)
    Entidad_Residencia = db.Column(db.SmallInteger, nullable=False)
    Municipio_Residencia = db.Column(db.SmallInteger, nullable=False)
    Localidad_Residencia = db.Column(db.SmallInteger, nullable=False)
    Num_Embarazos = db.Column(db.SmallInteger, nullable=False)
    Hijos_Nacidos_Muertos = db.Column(db.SmallInteger, nullable=False)
    Hijos_Nacidos_Vivos = db.Column(db.SmallInteger, nullable=False)
    Hijos_Sobrevivientes = db.Column(db.SmallInteger, nullable=False)
    Condicion_Hijo_Anterior = db.Column(db.SmallInteger, nullable=False)
    Vive_Hijo_Anterior = db.Column(db.SmallInteger, nullable=False)
    Orden_Nacimiento = db.Column(db.SmallInteger, nullable=False)
    Atencion_Prenatal = db.Column(db.SmallInteger, nullable=False)
    Trimestre_Primer_Consulta = db.Column(db.SmallInteger, nullable=False)
    Total_Consultas = db.Column(db.SmallInteger)
    Sobrevivio_Parto = db.Column(db.SmallInteger, nullable=False)
    Afiliacion = db.Column(db.SmallInteger, nullable=False)
    Escolaridad = db.Column(db.SmallInteger, nullable=False)
    Interrumpio_Estudios = db.Column(db.SmallInteger, nullable=False)
    Clave_Ocupacion_Habitual = db.Column(db.SmallInteger, nullable=False)
    Trabaja_Actualmente = db.Column(db.SmallInteger, nullable=False)
    Edad_Padre = db.Column(db.SmallInteger)
    Fecha_Nacimiento = db.Column(db.Date, nullable=False)
    Hora_Nacimiento = db.Column(db.String(10), nullable=False)
    Sexo = db.Column(db.SmallInteger, nullable=False)
    Edad_Gestacional = db.Column(db.SmallInteger, nullable=False)
    Talla = db.Column(db.SmallInteger, nullable=False)
    Peso = db.Column(db.SmallInteger, nullable=False)
    Apgar = db.Column(db.SmallInteger, nullable=False)
    Silverman = db.Column(db.SmallInteger, nullable=False)
    Tamiz_Auditivo = db.Column(db.SmallInteger, nullable=False)
    Vacuna_BCG = db.Column(db.SmallInteger, nullable=False)
    Vacuna_Hepatitis_B = db.Column(db.SmallInteger, nullable=False)
    Vitamina_A = db.Column(db.SmallInteger, nullable=False)
    Vitamina_K = db.Column(db.SmallInteger, nullable=False)
    Producto_Embarazo = db.Column(db.SmallInteger, nullable=False)
    Orden_Producto = db.Column(db.SmallInteger)
    Total_Productos = db.Column(db.SmallInteger)
    Codigo_Anomalia1 = db.Column(db.String(10), nullable=False)
    Codigo_Anomalia2 = db.Column(db.String(10), nullable=False)
    Lugar_Nacimiento = db.Column(db.SmallInteger, nullable=False)
    Clues = db.Column(db.String(50))
    Tiempo_Traslado = db.Column(db.Time)
    Resolucion_Embarazo = db.Column(db.SmallInteger, nullable=False)
    Utilizo_Forceps = db.Column(db.SmallInteger, nullable=False)
    Tipo_Cesarea = db.Column(db.SmallInteger, nullable=False)
    Personal_Atendio = db.Column(db.SmallInteger, nullable=False)
    Tipo_Medico_Atendio = db.Column(db.SmallInteger)
    Entidad_Federativa_Parto = db.Column(db.SmallInteger, nullable=False)
    Municipio_Parto = db.Column(db.SmallInteger, nullable=False)
    Localidad_Parto = db.Column(db.SmallInteger, nullable=False)
    Certificado_Por = db.Column(db.SmallInteger, nullable=False)
    Clues_Certifica = db.Column(db.String(50))
    EntidadFed_Certifica = db.Column(db.SmallInteger, nullable=False)
    Municipio_Certifica = db.Column(db.SmallInteger, nullable=False)
    Localidad_Certifica = db.Column(db.SmallInteger, nullable=False)
    Fecha_Certificado = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'IdNacimiento': self.IdNacimiento,
            'Nacio_Extranjero': self.Nacio_Extranjero,
            'Entidad_Nacimiento': self.Entidad_Nacimiento,
            'Municipio_Nacimiento': self.Municipio_Nacimiento,
            'Edad': self.Edad,
            'Se_Considera_Indigena': self.Se_Considera_Indigena,
            'Habla_Lengua_Indigena': self.Habla_Lengua_Indigena,
            'Fecha_Nacimiento_Madre': self.Fecha_Nacimiento_Madre,
            'Estado_Conyugal': self.Estado_Conyugal,
            'Reside_Extranjero': self.Reside_Extranjero,
            'Entidad_Residencia': self.Entidad_Residencia,
            'Municipio_Residencia': self.Municipio_Residencia,
            'Localidad_Residencia': self.Localidad_Residencia,
            'Num_Embarazos': self.Num_Embarazos,
            'Hijos_Nacidos_Muertos': self.Hijos_Nacidos_Muertos,
            'Hijos_Nacidos_Vivos': self.Hijos_Nacidos_Vivos,
            'Hijos_Sobrevivientes': self.Hijos_Sobrevivientes,
            'Condicion_Hijo_Anterior': self.Condicion_Hijo_Anterior,
            'Vive_Hijo_Anterior': self.Vive_Hijo_Anterior,
            'Orden_Nacimiento': self.Orden_Nacimiento,
            'Atencion_Prenatal': self.Atencion_Prenatal,
            'Trimestre_Primer_Consulta': self.Trimestre_Primer_Consulta,
            'Total_Consultas': self.Total_Consultas,
            'Sobrevivio_Parto': self.Sobrevivio_Parto,
            'Afiliacion': self.Afiliacion,
            'Escolaridad': self.Escolaridad,
            'Interrumpio_Estudios': self.Interrumpio_Estudios,
            'Clave_Ocupacion_Habitual': self.Clave_Ocupacion_Habitual,
            'Trabaja_Actualmente': self.Trabaja_Actualmente,
            'Edad_Padre': self.Edad_Padre,
            'Fecha_Nacimiento': self.Fecha_Nacimiento,
            'Hora_Nacimiento': self.Hora_Nacimiento,
            'Sexo': self.Sexo,
            'Edad_Gestacional': self.Edad_Gestacional,
            'Talla': self.Talla,
            'Peso': self.Peso,
            'Apgar': self.Apgar,
            'Silverman': self.Silverman,
            'Tamiz_Auditivo': self.Tamiz_Auditivo,
            'Vacuna_BCG': self.Vacuna_BCG,
            'Vacuna_Hepatitis_B': self.Vacuna_Hepatitis_B,
            'Vitamina_A': self.Vitamina_A,
            'Vitamina_K': self.Vitamina_K,
            'Producto_Embarazo': self.Producto_Embarazo,
            'Orden_Producto': self.Orden_Producto,
            'Total_Productos': self.Total_Productos,
            'Codigo_Anomalia1': self.Codigo_Anomalia1,
            'Codigo_Anomalia2': self.Codigo_Anomalia2,
            'Lugar_Nacimiento': self.Lugar_Nacimiento,
            'Clues': self.Clues,
            'Tiempo_Traslado': self.Tiempo_Traslado,
            'Resolucion_Embarazo': self.Resolucion_Embarazo,
            'Utilizo_Forceps': self.Utilizo_Forceps,
            'Tipo_Cesarea': self.Tipo_Cesarea,
            'Personal_Atendio': self.Personal_Atendio,
            'Tipo_Medico_Atendio': self.Tipo_Medico_Atendio,
            'Entidad_Federativa_Parto': self.Entidad_Federativa_Parto,
            'Municipio_Parto': self.Municipio_Parto,
            'Localidad_Parto': self.Localidad_Parto,
            'Certificado_Por': self.Certificado_Por,
            'Clues_Certifica': self.Clues_Certifica,
            'EntidadFed_Certifica': self.EntidadFed_Certifica,
            'Municipio_Certifica': self.Municipio_Certifica,
            'Localidad_Certifica': self.Localidad_Certifica,
            'Fecha_Certificado': self.Fecha_Certificado
        }