from db import db

class CtDef_Lengua_Indigena(db.Model):
    __tablename__ = 'CtDef_Lengua_Indigena'
    Cve = db.Column(db.Integer, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
