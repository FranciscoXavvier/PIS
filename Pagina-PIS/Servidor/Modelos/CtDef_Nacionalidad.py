from db import db

class CtDef_Nacionalidad(db.Model):
    __tablename__ = 'CtDef_Nacionalidad'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
