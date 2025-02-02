from db import db

class CtDef_Lista1(db.Model):
    __tablename__ = 'CtDef_Lista1'
    Cve = db.Column(db.SmallInteger, primary_key=True)
    Descrip = db.Column(db.String(150), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
