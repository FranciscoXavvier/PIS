from db import db

class CtNac_Resolucion_Embarazo(db.Model):
    __tablename__ = 'CtNac_Resolucion_Embarazo'
    Clave = db.Column(db.SmallInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
