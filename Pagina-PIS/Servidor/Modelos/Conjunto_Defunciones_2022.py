from db import db

class ConjuntoDeDatosDefuncionesRegistrados2022(db.Model):
    __tablename__ = 'Conjunto_De_Datos_Defunciones_Registrados_2022'

    IdDefuncion = db.Column(db.Integer, primary_key=True)
    Ent_regis = db.Column(db.SmallInteger, nullable=False)
    Mun_regis = db.Column(db.SmallInteger, nullable=False)
    Tloc_regis = db.Column(db.SmallInteger, nullable=False)
    Loc_regis = db.Column(db.SmallInteger, nullable=False)
    Ent_resid = db.Column(db.SmallInteger, nullable=False)
    Mun_resid = db.Column(db.SmallInteger, nullable=False)
    Tloc_resid = db.Column(db.SmallInteger, nullable=False)
    Loc_resid = db.Column(db.SmallInteger, nullable=False)
    Ent_ocurr = db.Column(db.SmallInteger, nullable=False)
    Mun_ocurr = db.Column(db.SmallInteger, nullable=False)
    Tloc_ocurr = db.Column(db.SmallInteger, nullable=False)
    Loc_ocurr = db.Column(db.SmallInteger, nullable=False)
    Causa_def = db.Column(db.String(50), nullable=False)
    Cod_adicio = db.Column(db.String(50))
    Lista_mex = db.Column(db.String(50), nullable=False)
    Sexo = db.Column(db.SmallInteger, nullable=False)
    Ent_nac = db.Column(db.SmallInteger, nullable=False)
    Afromex = db.Column(db.SmallInteger, nullable=False)
    Conindig = db.Column(db.SmallInteger, nullable=False)
    Lengua = db.Column(db.SmallInteger, nullable=False)
    Cve_lengua = db.Column(db.SmallInteger, nullable=False)
    Nacionalid = db.Column(db.SmallInteger, nullable=False)
    Nacesp_cve = db.Column(db.SmallInteger, nullable=False)
    Edad = db.Column(db.SmallInteger, nullable=False)
    Sem_gest = db.Column(db.SmallInteger, nullable=False)
    Gramos = db.Column(db.SmallInteger, nullable=False)
    Dia_ocurr = db.Column(db.SmallInteger, nullable=False)
    Mes_ocurr = db.Column(db.SmallInteger, nullable=False)
    Anio_ocur = db.Column(db.SmallInteger, nullable=False)
    Dia_regis = db.Column(db.SmallInteger, nullable=False)
    Mes_regis = db.Column(db.SmallInteger, nullable=False)
    Anio_regis = db.Column(db.SmallInteger, nullable=False)
    Dia_nacim = db.Column(db.SmallInteger, nullable=False)
    Mes_nacim = db.Column(db.SmallInteger, nullable=False)
    Anio_nacim = db.Column(db.SmallInteger, nullable=False)
    Cond_act = db.Column(db.SmallInteger, nullable=False)
    Ocupacion = db.Column(db.SmallInteger, nullable=False)
    Escolarida = db.Column(db.SmallInteger, nullable=False)
    Edo_civil = db.Column(db.SmallInteger, nullable=False)
    Tipo_defun = db.Column(db.SmallInteger, nullable=False)
    Ocurr_trab = db.Column(db.SmallInteger, nullable=False)
    Lugar_ocur = db.Column(db.SmallInteger, nullable=False)
    Par_agre = db.Column(db.SmallInteger, nullable=False)
    Asist_medi = db.Column(db.SmallInteger, nullable=False)
    Cirugia = db.Column(db.SmallInteger, nullable=False)
    Natviole = db.Column(db.SmallInteger, nullable=False)
    Necropsia = db.Column(db.SmallInteger, nullable=False)
    Usonecrops = db.Column(db.SmallInteger, nullable=False)
    Encefalica = db.Column(db.SmallInteger, nullable=False)
    Donador = db.Column(db.SmallInteger, nullable=False)
    Sitio_ocur = db.Column(db.SmallInteger, nullable=False)
    Cond_cert = db.Column(db.SmallInteger, nullable=False)
    Derechohab = db.Column(db.SmallInteger, nullable=False)
    Embarazo = db.Column(db.SmallInteger, nullable=False)
    Rel_emba = db.Column(db.SmallInteger, nullable=False)
    Horas = db.Column(db.SmallInteger, nullable=False)
    Minutos = db.Column(db.SmallInteger, nullable=False)
    Capitulo = db.Column(db.SmallInteger, nullable=False)
    Grupo = db.Column(db.SmallInteger, nullable=True)
    Lista1 = db.Column(db.SmallInteger, nullable=True)
    Gr_lismex = db.Column(db.String(20), nullable=False)
    Area_ur = db.Column(db.SmallInteger, nullable=False)
    Edad_agru = db.Column(db.SmallInteger, nullable=False)
    Complicaro = db.Column(db.SmallInteger, nullable=False)
    Dia_cert = db.Column(db.SmallInteger, nullable=False)
    Mes_cert = db.Column(db.SmallInteger, nullable=False)
    Anio_cert = db.Column(db.SmallInteger, nullable=False)
    Maternas = db.Column(db.String(20), nullable=True)
    Ent_ocules = db.Column(db.SmallInteger, nullable=False)
    Mun_ocules = db.Column(db.SmallInteger, nullable=False)
    Loc_ocules = db.Column(db.SmallInteger, nullable=False)
    Razon_m = db.Column(db.SmallInteger, nullable=False)
    Id_inegi = db.Column(db.String(255), nullable=False)
    Dis_re_oax = db.Column(db.SmallInteger, nullable=False)
    Edad_descodificada = db.Column(db.SmallInteger, nullable=True)

    def to_dict(self):
        return {
            'IdDefuncion': self.IdDefuncion,
            'Ent_regis': self.Ent_regis,
            'Mun_regis': self.Mun_regis,
            'Tloc_regis': self.Tloc_regis,
            'Loc_regis': self.Loc_regis,
            'Ent_resid': self.Ent_resid,
            'Mun_resid': self.Mun_resid,
            'Tloc_resid': self.Tloc_resid,
            'Loc_resid': self.Loc_resid,
            'Ent_ocurr': self.Ent_ocurr,
            'Mun_ocurr': self.Mun_ocurr,
            'Tloc_ocurr': self.Tloc_ocurr,
            'Loc_ocurr': self.Loc_ocurr,
            'Causa_def': self.Causa_def,
            'Cod_adicio': self.Cod_adicio,
            'Lista_mex': self.Lista_mex,
            'Sexo': self.Sexo,
            'Ent_nac': self.Ent_nac,
            'Afromex': self.Afromex,
            'Conindig': self.Conindig,
            'Lengua': self.Lengua,
            'Cve_lengua': self.Cve_lengua,
            'Nacionalid': self.Nacionalid,
            'Nacesp_cve': self.Nacesp_cve,
            'Edad': self.Edad,
            'Sem_gest': self.Sem_gest,
            'Gramos': self.Gramos,
            'Dia_ocurr': self.Dia_ocurr,
            'Mes_ocurr': self.Mes_ocurr,
            'Anio_ocur': self.Anio_ocur,
            'Dia_regis': self.Dia_regis,
            'Mes_regis': self.Mes_regis,
            'Anio_regis': self.Anio_regis,
            'Dia_nacim': self.Dia_nacim,
            'Mes_nacim': self.Mes_nacim,
            'Anio_nacim': self.Anio_nacim,
            'Cond_act': self.Cond_act,
            'Ocupacion': self.Ocupacion,
            'Escolarida': self.Escolarida,
            'Edo_civil': self.Edo_civil,
            'Tipo_defun': self.Tipo_defun,
            'Ocurr_trab': self.Ocurr_trab,
            'Lugar_ocur': self.Lugar_ocur,
            'Par_agre': self.Par_agre,
            'Asist_medi': self.Asist_medi,
            'Cirugia': self.Cirugia,
            'Natviole': self.Natviole,
            'Necropsia': self.Necropsia,
            'Usonecrops': self.Usonecrops,
            'Encefalica': self.Encefalica,
            'Donador': self.Donador,
            'Sitio_ocur': self.Sitio_ocur,
            'Cond_cert': self.Cond_cert,
            'Derechohab': self.Derechohab,
            'Embarazo': self.Embarazo,
            'Rel_emba': self.Rel_emba,
            'Horas': self.Horas,
            'Minutos': self.Minutos,
            'Capitulo': self.Capitulo,
            'Grupo': self.Grupo,
            'Lista1': self.Lista1,
            'Gr_lismex': self.Gr_lismex,
            'Area_ur': self.Area_ur,
            'Edad_agru': self.Edad_agru,
            'Complicaro': self.Complicaro,
            'Dia_cert': self.Dia_cert,
            'Mes_cert': self.Mes_cert,
            'Anio_cert': self.Anio_cert,
            'Maternas': self.Maternas,
            'Ent_ocules': self.Ent_ocules,
            'Mun_ocules': self.Mun_ocules,
            'Loc_ocules': self.Loc_ocules,
            'Razon_m': self.Razon_m,
            'Id_inegi': self.Id_inegi,
            'Dis_re_oax': self.Dis_re_oax,
            'Edad_descodificada': self.Edad_descodificada
        }
