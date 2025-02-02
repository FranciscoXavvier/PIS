from db import db
from sqlalchemy import PrimaryKeyConstraint

class PoblacionPorEntidadFederativa2010_2025(db.Model):
    __tablename__ = 'Población_Por_Entidad_Federativa_2010_2025'
    Anio = db.Column(db.SmallInteger, nullable=False)
    Clave_EntFed = db.Column(db.SmallInteger, nullable=False)
    Entidad_federativa = db.Column(db.String(60), nullable=False)
    Men_1_H = db.Column(db.Integer, nullable=False)
    H_1_4 = db.Column(db.Integer, nullable=False)
    H_5_9 = db.Column(db.Integer, nullable=False)
    H_10_14 = db.Column(db.Integer, nullable=False)
    H_15_19 = db.Column(db.Integer, nullable=False)
    H_20_24 = db.Column(db.Integer, nullable=False)
    H_25_29 = db.Column(db.Integer, nullable=False)
    H_30_34 = db.Column(db.Integer, nullable=False)
    H_35_39 = db.Column(db.Integer, nullable=False)
    H_40_44 = db.Column(db.Integer, nullable=False)
    H_45_49 = db.Column(db.Integer, nullable=False)
    H_50_54 = db.Column(db.Integer, nullable=False)
    H_55_59 = db.Column(db.Integer, nullable=False)
    H_60_64 = db.Column(db.Integer, nullable=False)
    H_65_69 = db.Column(db.Integer, nullable=False)
    H_70_74 = db.Column(db.Integer, nullable=False)
    H_75_79 = db.Column(db.Integer, nullable=False)
    H_80_84 = db.Column(db.Integer, nullable=False)
    H_85yMas = db.Column(db.Integer, nullable=False)
    Men_1_M = db.Column(db.Integer, nullable=False)
    M_1_4 = db.Column(db.Integer, nullable=False)
    M_5_9 = db.Column(db.Integer, nullable=False)
    M_10_14 = db.Column(db.Integer, nullable=False)
    M_15_19 = db.Column(db.Integer, nullable=False)
    M_20_24 = db.Column(db.Integer, nullable=False)
    M_25_29 = db.Column(db.Integer, nullable=False)
    M_30_34 = db.Column(db.Integer, nullable=False)
    M_35_39 = db.Column(db.Integer, nullable=False)
    M_40_44 = db.Column(db.Integer, nullable=False)
    M_45_49 = db.Column(db.Integer, nullable=False)
    M_50_54 = db.Column(db.Integer, nullable=False)
    M_55_59 = db.Column(db.Integer, nullable=False)
    M_60_64 = db.Column(db.Integer, nullable=False)
    M_65_69 = db.Column(db.Integer, nullable=False)
    M_70_74 = db.Column(db.Integer, nullable=False)
    M_75_79 = db.Column(db.Integer, nullable=False)
    M_80_84 = db.Column(db.Integer, nullable=False)
    M_85yMas = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('Anio', 'Clave_EntFed'),
    )

    def to_dict(self):
        return {
            'Anio': self.Anio,
            'Clave_EntFed': self.Clave_EntFed,
            'Entidad_federativa': self.Entidad_federativa,
            'Men_1_H': self.Men_1_H,
            'H_1_4': self.H_1_4,
            'H_5_9': self.H_5_9,
            'H_10_14': self.H_10_14,
            'H_15_19': self.H_15_19,
            'H_20_24': self.H_20_24,
            'H_25_29': self.H_25_29,
            'H_30_34': self.H_30_34,
            'H_35_39': self.H_35_39,
            'H_40_44': self.H_40_44,
            'H_45_49': self.H_45_49,
            'H_50_54': self.H_50_54,
            'H_55_59': self.H_55_59,
            'H_60_64': self.H_60_64,
            'H_65_69': self.H_65_69,
            'H_70_74': self.H_70_74,
            'H_75_79': self.H_75_79,
            'H_80_84': self.H_80_84,
            'H_85yMas': self.H_85yMas,
            'Men_1_M': self.Men_1_M,
            'M_1_4': self.M_1_4,
            'M_5_9': self.M_5_9,
            'M_10_14': self.M_10_14,
            'M_15_19': self.M_15_19,
            'M_20_24': self.M_20_24,
            'M_25_29': self.M_25_29,
            'M_30_34': self.M_30_34,
            'M_35_39': self.M_35_39,
            'M_40_44': self.M_40_44,
            'M_45_49': self.M_45_49,
            'M_50_54': self.M_50_54,
            'M_55_59': self.M_55_59,
            'M_60_64': self.M_60_64,
            'M_65_69': self.M_65_69,
            'M_70_74': self.M_70_74,
            'M_75_79': self.M_75_79,
            'M_80_84': self.M_80_84,
            'M_85yMas': self.M_85yMas
        }