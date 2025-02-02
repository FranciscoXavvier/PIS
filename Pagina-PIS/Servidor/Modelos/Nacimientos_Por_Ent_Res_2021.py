from db import db

class NacimientosPorEntRes2021(db.Model):
    __tablename__ = 'Nacimientos_Por_Ent_Res_2021'
    Ent_Fed = db.Column(db.SmallInteger, primary_key=True)
    Total_Nacimientos = db.Column(db.Integer)

    def to_dict(self):
        return {
            'Ent_Fed': self.Ent_Fed,
            'Total_Nacimientos': self.Total_Nacimientos
        }
