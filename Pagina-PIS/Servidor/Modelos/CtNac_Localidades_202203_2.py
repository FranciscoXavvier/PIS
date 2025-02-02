from db import db
from sqlalchemy import PrimaryKeyConstraint

class CtNac_Localidades_202203_2(db.Model):
    __tablename__ = 'CtNac_Localidades_202203_2'
    Cve_Ent = db.Column(db.String(10), nullable=False)
    Cve_Mun = db.Column(db.SmallInteger, nullable=False)
    Cve_Loc = db.Column(db.SmallInteger, nullable=False)
    Nom_Loc = db.Column(db.String(100), nullable=False)
    Estatus = db.Column(db.String(50))

    __table_args__ = (
        PrimaryKeyConstraint('Cve_Ent', 'Cve_Mun', 'Cve_Loc'),
    )

    def to_dict(self):
        return {
            'Cve_Ent': self.Cve_Ent,
            'Cve_Mun': self.Cve_Mun,
            'Cve_Loc': self.Cve_Loc,
            'Nom_Loc': self.Nom_Loc,
            'Estatus': self.Estatus
        }
