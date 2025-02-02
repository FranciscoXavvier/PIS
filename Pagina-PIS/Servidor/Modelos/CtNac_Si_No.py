from db import db

class CtNac_Si_No(db.Model):
    __tablename__ = 'CtNac_Si_No'
    clave = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column('Descripción', db.String(50))

    def to_dict(self):
        return {
            'clave': self.clave,
            'descripcion': self.descripcion
        }
