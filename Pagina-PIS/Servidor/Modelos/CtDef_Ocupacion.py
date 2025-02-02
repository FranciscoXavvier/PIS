from db import db

class CtDef_Ocupacion(db.Model):
    __tablename__ = 'CtDef_Ocupacion'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
