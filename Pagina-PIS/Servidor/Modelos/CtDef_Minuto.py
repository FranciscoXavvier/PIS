from db import db

class CtDef_Minuto(db.Model):
    __tablename__ = 'CtDef_Minuto'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(70), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
