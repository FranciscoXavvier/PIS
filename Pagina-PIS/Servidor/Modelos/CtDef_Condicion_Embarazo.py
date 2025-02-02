from db import db

class CtDef_Condicion_Embarazo(db.Model):
    __tablename__ = 'CtDef_Condicion_Embarazo'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
