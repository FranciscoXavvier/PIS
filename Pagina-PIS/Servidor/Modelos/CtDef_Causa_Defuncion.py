from db import db

class CtDef_Causa_Defuncion(db.Model):
    __tablename__ = 'CtDef_Causa_Defuncion'
    Cve = db.Column(db.String(50), primary_key=True)
    Descrip = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            'Cve': self.Cve,
            'Descrip': self.Descrip
        }
