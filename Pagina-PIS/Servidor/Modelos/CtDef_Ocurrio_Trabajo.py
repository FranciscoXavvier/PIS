from db import db

class CtDef_Ocurrio_Trabajo(db.Model):
    __tablename__ = 'CtDef_Ocurrio_Trabajo'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(60), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
