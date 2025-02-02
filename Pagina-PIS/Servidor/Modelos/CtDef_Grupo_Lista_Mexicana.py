from db import db

class CtDef_Grupo_Lista_Mexicana(db.Model):
    __tablename__ = 'CtDef_Grupo_Lista_Mexicana'
    Cve = db.Column(db.String(10), primary_key=True)
    Descrip = db.Column(db.String(150), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
