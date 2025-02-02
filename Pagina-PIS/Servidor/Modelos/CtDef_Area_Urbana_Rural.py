from db import db

class CtDef_Area_Urbana_Rural(db.Model):
    __tablename__ = 'CtDef_Area_Urbana_Rural'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
