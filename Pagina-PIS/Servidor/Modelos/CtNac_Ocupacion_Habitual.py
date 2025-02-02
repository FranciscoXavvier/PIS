from db import db

class CtNac_Ocupacion_Habitual(db.Model):
    __tablename__ = 'CtNac_Ocupacion_Habitual'
    Clave = db.Column(db.SmallInteger, primary_key=True)
    Descripcion = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
