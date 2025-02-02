from db import db

class CtNac_Sexo(db.Model):
    __tablename__ = 'CtNac_Sexo'
    Clave = db.Column(db.SmallInteger, primary_key=True)
    Descripcion = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Clave': self.Clave,
            'Descripcion': self.Descripcion
        }
