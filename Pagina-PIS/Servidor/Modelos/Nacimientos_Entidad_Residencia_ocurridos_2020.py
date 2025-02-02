from db import db

class Nacimientos_Entidad_Residencia_ocurridos_2020(db.Model):
    __tablename__ = 'Nacimientos_Entidad_Residencia_ocurridos_2020'
    Clv_Residencia = db.Column(db.SmallInteger, primary_key=True)
    Entidad_Residencia = db.Column(db.String(50), nullable=False)
    Nacimientos = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'Clv_Residencia': self.Clv_Residencia,
            'Entidad_Residencia': self.Entidad_Residencia,
            'Nacimientos': self.Nacimientos
        }
