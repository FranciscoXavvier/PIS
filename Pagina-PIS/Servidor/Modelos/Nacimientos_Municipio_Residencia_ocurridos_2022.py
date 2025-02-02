from db import db
from sqlalchemy import PrimaryKeyConstraint

class Nacimientos_Municipio_Residencia_ocurridos_2022(db.Model):
    __tablename__ = 'Nacimientos_Municipio_Residencia_ocurridos_2022'
    Entidad_Res = db.Column(db.SmallInteger, nullable=False)
    Descripcion_Ent_Res = db.Column(db.String(100))
    Municipio_Res = db.Column(db.SmallInteger, nullable=False)
    Descripcion_Mun_Res = db.Column(db.String(100))
    Total_Nacimientos = db.Column(db.Integer)

    __table_args__ = (
        PrimaryKeyConstraint('Entidad_Res', 'Municipio_Res'),
    )

    def to_dict(self):
        return {
            'Entidad_Res': self.Entidad_Res,
            'Descripcion_Ent_Res': self.Descripcion_Ent_Res,
            'Municipio_Res': self.Municipio_Res,
            'Descripcion_Mun_Res': self.Descripcion_Mun_Res,
            'Total_Nacimientos': self.Total_Nacimientos
        }
