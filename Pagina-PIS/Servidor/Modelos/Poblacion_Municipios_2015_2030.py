from db import db
from sqlalchemy import PrimaryKeyConstraint

class PoblacionMunicipios2015_2030(db.Model):
    __tablename__ = 'Poblacion_Municipios_2015_2030'
    Anio = db.Column(db.SmallInteger, nullable=False)
    Clv_Ent_Mpo = db.Column(db.SmallInteger, nullable=False)
    Pobm_00_04_H = db.Column(db.Integer, nullable=False)
    Pobm_05_09_H = db.Column(db.Integer, nullable=False)
    Pobm_10_14_H = db.Column(db.Integer, nullable=False)
    Pobm_15_19_H = db.Column(db.Integer, nullable=False)
    Pobm_20_24_H = db.Column(db.Integer, nullable=False)
    Pobm_25_29_H = db.Column(db.Integer, nullable=False)
    Pobm_30_34_H = db.Column(db.Integer, nullable=False)
    Pobm_35_39_H = db.Column(db.Integer, nullable=False)
    Pobm_40_44_H = db.Column(db.Integer, nullable=False)
    Pobm_45_49_H = db.Column(db.Integer, nullable=False)
    Pobm_50_54_H = db.Column(db.Integer, nullable=False)
    Pobm_55_59_H = db.Column(db.Integer, nullable=False)
    Pobm_60_64_H = db.Column(db.Integer, nullable=False)
    Pobm_65_MM_H = db.Column(db.Integer, nullable=False)
    Pobm_00_04_M = db.Column(db.Integer, nullable=False)
    Pobm_05_09_M = db.Column(db.Integer, nullable=False)
    Pobm_10_14_M = db.Column(db.Integer, nullable=False)
    Pobm_15_19_M = db.Column(db.Integer, nullable=False)
    Pobm_20_24_M = db.Column(db.Integer, nullable=False)
    Pobm_25_29_M = db.Column(db.Integer, nullable=False)
    Pobm_30_34_M = db.Column(db.Integer, nullable=False)
    Pobm_35_39_M = db.Column(db.Integer, nullable=False)
    Pobm_40_44_M = db.Column(db.Integer, nullable=False)
    Pobm_45_49_M = db.Column(db.Integer, nullable=False)
    Pobm_50_54_M = db.Column(db.Integer, nullable=False)
    Pobm_55_59_M = db.Column(db.Integer, nullable=False)
    Pobm_60_64_M = db.Column(db.Integer, nullable=False)
    Pobm_65_MM_M = db.Column(db.Integer, nullable=False)
    Ent_Fed = db.Column(db.SmallInteger, nullable=False)
    Municipio = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('Anio', 'Ent_Fed', 'Municipio'),
    )

    def to_dict(self):
        return {
            'Anio': self.Anio,
            'Clv_Ent_Mpo': self.Clv_Ent_Mpo,
            'Pobm_00_04_H': self.Pobm_00_04_H,
            'Pobm_05_09_H': self.Pobm_05_09_H,
            'Pobm_10_14_H': self.Pobm_10_14_H,
            'Pobm_15_19_H': self.Pobm_15_19_H,
            'Pobm_20_24_H': self.Pobm_20_24_H,
            'Pobm_25_29_H': self.Pobm_25_29_H,
            'Pobm_30_34_H': self.Pobm_30_34_H,
            'Pobm_35_39_H': self.Pobm_35_39_H,
            'Pobm_40_44_H': self.Pobm_40_44_H,
            'Pobm_45_49_H': self.Pobm_45_49_H,
            'Pobm_50_54_H': self.Pobm_50_54_H,
            'Pobm_55_59_H': self.Pobm_55_59_H,
            'Pobm_60_64_H': self.Pobm_60_64_H,
            'Pobm_65_MM_H': self.Pobm_65_MM_H,
            'Pobm_00_04_M': self.Pobm_00_04_M,
            'Pobm_05_09_M': self.Pobm_05_09_M,
            'Pobm_10_14_M': self.Pobm_10_14_M,
            'Pobm_15_19_M': self.Pobm_15_19_M,
            'Pobm_20_24_M': self.Pobm_20_24_M,
            'Pobm_25_29_M': self.Pobm_25_29_M,
            'Pobm_30_34_M': self.Pobm_30_34_M,
            'Pobm_35_39_M': self.Pobm_35_39_M,
            'Pobm_40_44_M': self.Pobm_40_44_M,
            'Pobm_45_49_M': self.Pobm_45_49_M,
            'Pobm_50_54_M': self.Pobm_50_54_M,
            'Pobm_55_59_M': self.Pobm_55_59_M,
            'Pobm_60_64_M': self.Pobm_60_64_M,
            'Pobm_65_MM_M': self.Pobm_65_MM_M,
            'Ent_Fed': self.Ent_Fed,
            'Municipio': self.Municipio
        }
