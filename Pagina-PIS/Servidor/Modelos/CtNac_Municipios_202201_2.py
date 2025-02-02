from db import db
from sqlalchemy import PrimaryKeyConstraint

class CtNac_Municipios_202201_2(db.Model):
    __tablename__ = 'CtNac_Municipios_202201_2'
    Clave_Mpo = db.Column(db.SmallInteger, nullable=False)
    Municipio = db.Column(db.String(100), nullable=False)
    Clave_Ent = db.Column(db.SmallInteger, nullable=False)
    Estatus = db.Column(db.String(50), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('Clave_Mpo', 'Clave_Ent'),
    )

    def to_dict(self):
        return {
            'Clave_Mpo': self.Clave_Mpo,
            'Municipio': self.Municipio,
            'Clave_Ent': self.Clave_Ent,
            'Estatus': self.Estatus
        }
