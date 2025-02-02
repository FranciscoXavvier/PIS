from db import db

class CtNac_Lugar_Nacimiento(db.Model):
    __tablename__ = 'CtNac_Lugar_Nacimiento'
    Clave = db.Column(db.SmallInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
