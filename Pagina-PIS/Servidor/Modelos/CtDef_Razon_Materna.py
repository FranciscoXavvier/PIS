from db import db

class CtDef_Razon_Materna(db.Model):
    __tablename__ = 'CtDef_Razon_Materna'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
