from db import db

class ConjuntoDeDatosDefuncionesRegistrados2020(db.Model):
    __tablename__ = 'Conjunto_De_Datos_Defunciones_Registrados_2020'
    IdDefuncion = db.Column(db.Integer, primary_key=True)
    Ent_regis = db.Column(db.SmallInteger, nullable=False)
    Mun_regis = db.Column(db.SmallInteger, nullable=False)
    Ent_resid = db.Column(db.SmallInteger, nullable=False)
    Mun_resid = db.Column(db.SmallInteger, nullable=False)
    Tloc_resid = db.Column(db.SmallInteger, nullable=False)
    Loc_resid = db.Column(db.SmallInteger, nullable=False)
    Ent_ocurr = db.Column(db.SmallInteger, nullable=False)
    Mun_ocurr = db.Column(db.SmallInteger, nullable=False)
    Tloc_ocurr = db.Column(db.SmallInteger, nullable=False)
    Loc_ocurr = db.Column(db.SmallInteger, nullable=False)
    Causa_def = db.Column(db.String(50), nullable=False)
    Lista_mex = db.Column(db.String(50), nullable=False)
    Sexo = db.Column(db.SmallInteger, nullable=False)
    Edad = db.Column(db.SmallInteger, nullable=False)
    Dia_ocurr = db.Column(db.SmallInteger, nullable=False)
    Mes_ocurr = db.Column(db.SmallInteger, nullable=False)
    Anio_ocur = db.Column(db.SmallInteger, nullable=False)
    Dia_regis = db.Column(db.SmallInteger, nullable=False)
    Mes_regis = db.Column(db.SmallInteger, nullable=False)
    Anio_regis = db.Column(db.SmallInteger, nullable=False)
    Dia_nacim = db.Column(db.SmallInteger, nullable=False)
    Mes_nacim = db.Column(db.SmallInteger, nullable=False)
    Anio_nacim = db.Column(db.SmallInteger, nullable=False)
    Ocupacion = db.Column(db.SmallInteger, nullable=False)
    Escolarida = db.Column(db.SmallInteger, nullable=False)
    Edo_civil = db.Column(db.SmallInteger, nullable=False)
    Presunto = db.Column(db.SmallInteger, nullable=False)
    Ocurr_trab = db.Column(db.SmallInteger, nullable=False)
    Lugar_ocur = db.Column(db.SmallInteger, nullable=False)
    Necropsia = db.Column(db.SmallInteger, nullable=False)
    Asist_medi = db.Column(db.SmallInteger, nullable=False)
    Sitio_ocur = db.Column(db.SmallInteger, nullable=False)
    Cond_cert = db.Column(db.SmallInteger, nullable=False)
    Nacionalid = db.Column(db.SmallInteger, nullable=False)
    Derechohab = db.Column(db.SmallInteger, nullable=False)
    Embarazo = db.Column(db.SmallInteger, nullable=False)
    Rel_emba = db.Column(db.SmallInteger, nullable=False)
    Horas = db.Column(db.SmallInteger, nullable=False)
    Minutos = db.Column(db.SmallInteger, nullable=False)
    Capitulo = db.Column(db.SmallInteger, nullable=False)
    Grupo = db.Column(db.SmallInteger,nullable=False)
    Lista1 = db.Column(db.SmallInteger, nullable=False)
    Gr_lismex = db.Column(db.String(20), nullable=False)
    Vio_fami = db.Column(db.SmallInteger, nullable=False)
    Area_ur = db.Column(db.SmallInteger, nullable=False)
    Edad_agru = db.Column(db.SmallInteger, nullable=False)
    Complicaro = db.Column(db.SmallInteger, nullable=False)
    Dia_cert = db.Column(db.SmallInteger, nullable=False)
    Mes_cert = db.Column(db.SmallInteger, nullable=False)
    Anio_cert = db.Column(db.SmallInteger, nullable=False)
    Maternas = db.Column(db.String(20))
    Lengua = db.Column(db.SmallInteger, nullable=False)
    Cond_act = db.Column(db.SmallInteger, nullable=False)
    Par_agre = db.Column(db.SmallInteger, nullable=False)
    Ent_ocules = db.Column(db.SmallInteger, nullable=False)
    Mun_ocules = db.Column(db.SmallInteger, nullable=False)
    Loc_ocules = db.Column(db.SmallInteger, nullable=False)
    Razon_m = db.Column(db.SmallInteger, nullable=False)
    Dis_re_oax = db.Column(db.SmallInteger, nullable=False)
    Edad_descodificada = db.Column(db.SmallInteger)

     # Agregar las relaciones ForeignKey para las llaves foráneas
    ocurrencia = db.relationship('CtDef_Entidad_Municipio_Localidad_2020',
                                primaryjoin="and_(ConjuntoDeDatosDefuncionesRegistrados2020.Ent_ocurr==CtDef_Entidad_Municipio_Localidad_2020.Cve_Ent, ConjuntoDeDatosDefuncionesRegistrados2020.Mun_ocurr==CtDef_Entidad_Municipio_Localidad_2020.Cve_Mun, ConjuntoDeDatosDefuncionesRegistrados2020.Loc_ocurr==CtDef_Entidad_Municipio_Localidad_2020.Cve_Loc)",
                                foreign_keys=[Ent_ocurr, Mun_ocurr, Loc_ocurr])

    
    residencia = db.relationship('CtDef_Entidad_Municipio_Localidad_2020',
                                primaryjoin="and_(ConjuntoDeDatosDefuncionesRegistrados2020.Ent_resid==CtDef_Entidad_Municipio_Localidad_2020.Cve_Ent, ConjuntoDeDatosDefuncionesRegistrados2020.Mun_resid==CtDef_Entidad_Municipio_Localidad_2020.Cve_Mun, ConjuntoDeDatosDefuncionesRegistrados2020.Loc_resid==CtDef_Entidad_Municipio_Localidad_2020.Cve_Loc)",
                                foreign_keys=[Ent_resid, Mun_resid, Loc_resid])
    
    capitulo = db.relationship('CtDef_Capitulo_Grupo',
                               primaryjoin="and_(ConjuntoDeDatosDefuncionesRegistrados2020.Capitulo==CtDef_Capitulo_Grupo.Cap, ConjuntoDeDatosDefuncionesRegistrados2020.Grupo==CtDef_Capitulo_Grupo.Gpo)",
                               foreign_keys = [Capitulo, Grupo])
    
    causa = db.relationship('CtDef_Causa_Defuncion',
                            primaryjoin="and_(ConjuntoDeDatosDefuncionesRegistrados2020.Causa_def==CtDef_Causa_Defuncion.Cve)",
                            foreign_keys = [Causa_def])
    
    ocupacion = db.relationship('CtDef_Ocupacion',
                                primaryjoin="and_(ConjuntoDeDatosDefuncionesRegistrados2020.Ocupacion==CtDef_Ocupacion.Cve)",
                                foreign_keys=[Ocupacion])
    
    parentesco = db.relationship('CtDef_Parentesco_Agresor',
                                primaryjoin="and_(ConjuntoDeDatosDefuncionesRegistrados2020.Par_agre==CtDef_Parentesco_Agresor.Cve)",
                                foreign_keys = [Par_agre])

    def to_dict(self):
        return {
            'IdDefuncion': self.IdDefuncion,
            'Ent_regis': self.Ent_regis,
            'Mun_regis': self.Mun_regis,
            'Ent_resid': self.Ent_resid,
            'Mun_resid': self.Mun_resid,
            'Tloc_resid': self.Tloc_resid,
            'Loc_resid': self.Loc_resid,
            'Ent_ocurr': self.Ent_ocurr,
            'Mun_ocurr': self.Mun_ocurr,
            'Tloc_ocurr': self.Tloc_ocurr,
            'Loc_ocurr': self.Loc_ocurr,
            'Causa_def': self.Causa_def,
            'Lista_mex': self.Lista_mex,
            'Sexo': self.Sexo,
            'Edad': self.Edad,
            'Dia_ocurr': self.Dia_ocurr,
            'Mes_ocurr': self.Mes_ocurr,
            'Anio_ocur': self.Anio_ocur,
            'Dia_regis': self.Dia_regis,
            'Mes_regis': self.Mes_regis,
            'Anio_regis': self.Anio_regis,
            'Dia_nacim': self.Dia_nacim,
            'Mes_nacim': self.Mes_nacim,
            'Anio_nacim': self.Anio_nacim,
            'Ocupacion': self.Ocupacion,
            'Escolarida': self.Escolarida,
            'Edo_civil': self.Edo_civil,
            'Presunto': self.Presunto,
            'Ocurr_trab': self.Ocurr_trab,
            'Lugar_ocur': self.Lugar_ocur,
            'Necropsia': self.Necropsia,
            'Asist_medi': self.Asist_medi,
            'Sitio_ocur': self.Sitio_ocur,
            'Cond_cert': self.Cond_cert,
            'Nacionalid': self.Nacionalid,
            'Derechohab': self.Derechohab,
            'Embarazo': self.Embarazo,
            'Rel_emba': self.Rel_emba,
            'Horas': self.Horas,
            'Minutos': self.Minutos,
            'Capitulo': self.Capitulo,
            'Grupo': self.Grupo,
            'Lista1': self.Lista1,
            'Gr_lismex': self.Gr_lismex,
            'Vio_fami': self.Vio_fami,
            'Area_ur': self.Area_ur,
            'Edad_agru': self.Edad_agru,
            'Complicaro': self.Complicaro,
            'Dia_cert': self.Dia_cert,
            'Mes_cert': self.Mes_cert,
            'Anio_cert': self.Anio_cert,
            'Maternas': self.Maternas,
            'Lengua': self.Lengua,
            'Cond_act': self.Cond_act,
            'Par_agre': self.Par_agre,
            'Ent_ocules': self.Ent_ocules,
            'Mun_ocules': self.Mun_ocules,
            'Loc_ocules': self.Loc_ocules,
            'Razon_m': self.Razon_m,
            'Dis_re_oax': self.Dis_re_oax,
            'Edad_descodificada': self.Edad_descodificada
        }
