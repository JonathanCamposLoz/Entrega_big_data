
from sqlalchemy.sql import text
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String, Sequence
from sqlalchemy import Float, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session


from sqlalchemy.orm import Session

Base = declarative_base()


class carga_data():

    def __init__(self):
        self.host_aws = "database-1.cdxv193qnk1p.us-east-1.rds.amazonaws.com"
        self.port_aws = '5432'
        self.user_aws = 'postgres'
        self.password_aws = 'postgres'
        self.database_aws = 'aws_data_bank' #verificar la existencia de la base datos

        self.aws_connAlchemy = create_engine(f'postgresql://{self.user_aws}:{self.password_aws}@{self.host_aws}:{self.port_aws}/{self.database_aws}')
        self.aws_conn = self.aws_connAlchemy.raw_connection()
        self.aws_cur = self.aws_conn.cursor()


    def infoAnio(self, df_anio):
        Base = declarative_base()
        class InfoAnio(Base):
            __tablename__= "num_anio"
                
            id = Column(Integer, Sequence('registro_llamadas_id_seq'), primary_key=True)
            anio = Column(String(250))
            cantidad = Column(Integer)

            def __repr__(self):
                return f"num_anio(id={self.id!r}, anio={self.anio!r}, cantidad={self.cantidad!r}"

        
        Base.metadata.create_all(self.aws_connAlchemy) #conexion previamente creada
        
        all_datos = []
        for index, row in df_anio.iterrows():
            data = InfoAnio(
                id=index,
                anio = row['anio'],
                cantidad = row['cantidad']
            )
            all_datos.append(data)

        with Session(self.aws_connAlchemy) as session:
            session.add_all(all_datos)
            session.commit()
 
    def infoIssue(self, df_issue):
        Base = declarative_base()
        class InfoIssue(Base):
            __tablename__= "num_issue"
                
            id = Column(Integer, Sequence('registro_llamadas_id_seq'), primary_key=True)
            issue = Column(String(250))
            cantidad = Column(Integer)

            def __repr__(self):
                return f"num_issue(id={self.id!r}, issue={self.issue!r}, cantidad={self.cantidad!r}"   


        Base.metadata.create_all(self.aws_connAlchemy) #conexion previamente creada
        
        all_datos = []
        for index, row in df_issue.iterrows():
            data = InfoIssue(
                id=index,
                issue = row['issue'],
                cantidad = row['cantidad']
            )
            all_datos.append(data)

        with Session(self.aws_connAlchemy) as session:
            session.add_all(all_datos)
            session.commit()
    
    def infoProducto(self, df_producto):
        Base = declarative_base()
        class InfoProducto(Base):
            __tablename__= "num_producto"
                
            id = Column(Integer, Sequence('registro_llamadas_id_seq'), primary_key=True)
            product = Column(String(250))
            cantidad = Column(Integer)

            def __repr__(self):
                return f"num_producto(id={self.id!r}, anio={self.anio!r}, product={self.product!r}"
        

        Base.metadata.create_all(self.aws_connAlchemy) #conexion previamente creada
        
        all_datos = []
        for index, row in df_producto.iterrows():
            data = InfoProducto(
                id=index,
                product = row['product'],
                cantidad = row['cantidad']
            )
            all_datos.append(data)

        with Session(self.aws_connAlchemy) as session:
            session.add_all(all_datos)
            session.commit()
      
    def infoSubmitted(self, df_submitted):
        Base = declarative_base()
        class InfoSubmitted(Base):
            __tablename__= "num_submitted"
                
            id = Column(Integer, Sequence('registro_llamadas_id_seq'), primary_key=True)
            submitted_via = Column(String(250))
            cantidad = Column(Integer)

            def __repr__(self):
                return f"num_submitted(id={self.id!r}, submitted_via={self.submitted_via!r}, cantidad={self.cantidad!r}"

        Base.metadata.create_all(self.aws_connAlchemy) #conexion previamente creada
        
        all_datos = []
        for index, row in df_submitted.iterrows():
            data = InfoSubmitted(
                id=index,
                submitted_via = row['submitted_via'],
                cantidad = row['cantidad']
            )
            all_datos.append(data)

        with Session(self.aws_connAlchemy) as session:
            session.add_all(all_datos)
            session.commit()