from db import db
from sqlalchemy import PrimaryKeyConstraint

class Indicadores_Municipio_Residencia_2020(db.Model):
    __tablename__ = 'Indicadores_Municipio_Residencia_2020'
    Entidad_Res = db.Column(db.SmallInteger, nullable=False)
    Descripcion_Ent_Res = db.Column(db.String(100), nullable=True)
    Municipio_Res = db.Column(db.SmallInteger, nullable=False)
    Descripcion_Mun_Res = db.Column(db.String(100), nullable=True)
    Nacimientos_Anio = db.Column(db.Integer, nullable=True)
    Total_Defunciones_Menores1 = db.Column(db.Integer, nullable=True)
    Tasa_Mortalidad_Infantil = db.Column(db.Float, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('Entidad_Res', 'Municipio_Res'),
    )

    def to_dict(self):
        return {
            'Entidad_Res': self.Entidad_Res,
            'Descripcion_Ent_Res': self.Descripcion_Ent_Res,
            'Municipio_Res': self.Municipio_Res,
            'Descripcion_Mun_Res': self.Descripcion_Mun_Res,
            'Nacimientos_Anio': self.Nacimientos_Anio,
            'Total_Defunciones_Menores1': self.Total_Defunciones_Menores1,
            'Tasa_Mortalidad_Infantil': self.Tasa_Mortalidad_Infantil
        }