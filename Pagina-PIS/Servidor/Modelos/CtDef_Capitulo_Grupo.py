from db import db

class CtDef_Capitulo_Grupo(db.Model):
    __tablename__ = 'CtDef_Capitulo_Grupo'
    Cap = db.Column(db.SmallInteger, primary_key=True)
    Gpo = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {
            'Cap': self.Cap,
            'Gpo': self.Gpo,
            'Descrip': self.Descrip
        }
