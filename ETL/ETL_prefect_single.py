# Librerias base datos

import csv
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Session

import numpy as np                                                       

#import nltk # imports the natural language toolkit
import pandas as pd

from collections import Counter
from datetime import datetime
#from sklearn.feature_extraction.text import CountVectorizer

from prefect import task, flow

import traceback



@task
def lectura_quejas():
    complaint_dataset = pd.read_csv("Datasets/complaint_data.csv")

    complaint_dataset["Product"] = complaint_dataset["Product"].replace( {"Credit card":"Credit card or prepaid card",
                                        "Credit reporting":"Credit reporting, credit repair services, or other personal consumer reports",
                                        "Money transfers":"Money transfer, virtual currency, or money service",
                                        "Payday loan":"Payday loan, title loan, or personal loan",
                                        "Virtual currency":"Money transfer, virtual currency, or money service",
                                        "Prepaid card":"Credit card or prepaid card"
                                        } )

    return complaint_dataset

@task
def lectura_info_estado():
    state_population_dataset = pd.read_csv("Datasets/estados.csv")
    return state_population_dataset

@task
def conectar_a_base():

    host_aws = "database-1.cdxv193qnk1p.us-east-1.rds.amazonaws.com"
    port_aws = '5432'
    user_aws = 'postgres'
    password_aws = 'postgres'
    database_aws = 'data_bank' #verificar la existencia de la base datos

    connAlchemy_aws = create_engine(f'postgresql://{user_aws}:{password_aws}@{host_aws}:{port_aws}/{database_aws}')

    return connAlchemy_aws

@task
def generar_por_producto(complaint_dataset, connAlchemy_aws):

    per_product = complaint_dataset[["Complaint ID","Product"]]

    per_product = per_product.groupby(["Product"], as_index=False).count()

    per_product = per_product.rename( columns={'Complaint ID': 'Count'} )

    Base = declarative_base()

    class complaints_per_product(Base):
        __tablename__= "complaints_per_product"

        product = Column(String(100), primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"complaints_per_product(order_num={self.product!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = per_product.values.tolist()
    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = complaints_per_product(
                product = item[0],
                count = item[1]
                )

                to_commit_list.append(commit_item)
    
            session.add_all(to_commit_list)
            session.commit()

        return "exito"
    
    except:

        traceback.print_exc()

        return "fallo"
    
@task
def generar_por_issue(complaint_dataset, connAlchemy_aws):

    per_product_issue = complaint_dataset[["Complaint ID","Product","Issue"]]

    per_product_issue = per_product_issue.groupby(["Product","Issue"], as_index=False).count()

    per_product_issue_grouped = per_product_issue.rename( columns={'Complaint ID': 'Count'} )

    per_product_issue_max = per_product_issue_grouped.sort_values(by=['Product', 'Count'], ascending=False).drop_duplicates(subset='Product')

    Base = declarative_base()

    class complaints_max_per_product_issue(Base):
        __tablename__= "complaints_max_per_product_issue"

        product = Column(String(100), primary_key=True)
        issue = Column(String(200))
        count = Column(Integer)

        def __repr__(self):
            return f"complaints_max_per_product_issue(product={self.product!r}, issue={self.issue!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = per_product_issue_max.values.tolist()
    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = complaints_max_per_product_issue(
                product = item[0],
                issue = item[1],
                count = item[2]
                )

                to_commit_list.append(commit_item)
    
            session.add_all(to_commit_list)
            session.commit()

        return "exito"
    
    except:

        traceback.print_exc()

        return "fallo"


@task
def generar_por_estado(complaint_dataset, state_population_dataset, connAlchemy_aws):

    per_state = complaint_dataset[["Complaint ID","State"]]

    per_state = per_state.groupby(["State"], as_index=False).count()

    per_state = per_state.rename( columns={'Complaint ID': 'complaint_count'} )

    state_data = state_population_dataset[["estate","abreviacion","poblacion"]].rename( columns={'estate': 'full_name', "abreviacion":"State", "poblacion":"population"} )

    per_state_10 = per_state.merge(state_data, on = "State", how="left")

    per_state_10 = per_state_10[per_state_10['population'].notnull()]

    per_state_10["complains_per_100k"] = round(( per_state_10["complaint_count"] / per_state_10["population"] ) * 100000, 2)

    Base = declarative_base()

    class complaints_per_100k_state(Base):
        __tablename__= "complaints_per_100k_state"

        state = Column(String(4), primary_key=True)
        complaint_count = Column(Integer)
        full_name = Column(String(50))
        population = Column(Integer)
        complaints_per_100k = Column(Float)

        def __repr__(self):
            return f"complaints_per_100k_state(state={self.state!r}, complaint_count={self.complaint_count!r}), full_name={self.full_name!r}, population={self.population!r}), complaints_per_100k={self.complains_per_100k!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = per_state_10.values.tolist()
    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = complaints_per_100k_state(
                state = item[0],
                complaint_count = item[1],
                full_name = item[2],
                population = item[3],
                complaints_per_100k = item[4]
                )

                to_commit_list.append(commit_item)
    
            session.add_all(to_commit_list)
            session.commit()

        return "exito"
    
    except:

        traceback.print_exc()

        return "fallo"
    

@task
def generar_por_canal(complaint_dataset, connAlchemy_aws):

    per_channel = complaint_dataset[["Complaint ID","Submitted via"]]

    per_channel = per_channel.groupby(["Submitted via"], as_index=False).count()

    per_channel = per_channel.rename( columns={'Complaint ID': 'complaint_count'} )
    
    Base = declarative_base()

    class complaints_per_channel(Base):
        __tablename__= "complaints_per_channel"

        channel = Column(String(20), primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"complaints_per_channel(channel={self.channel!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = per_channel.values.tolist()
    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = complaints_per_channel(
                channel = item[0],
                count = item[1]
                )

                to_commit_list.append(commit_item)
    
            session.add_all(to_commit_list)
            session.commit()

        return "exito"
    
    except:

        traceback.print_exc()

        return "fallo"
    

@task
def generar_por_anio(complaint_dataset, connAlchemy_aws):

    year_asgn = complaint_dataset[["Complaint ID","Date received"]].copy()

    year_asgn['year_received'] = year_asgn["Date received"].str.slice(6, 99)

    year_asgn = year_asgn.drop(["Date received"], axis=1)


    per_year  = year_asgn.groupby(["year_received"], as_index=False).count()

    per_year = per_year.rename( columns={'Complaint ID': 'complaint_count'} )
    
    Base = declarative_base()

    class complaints_per_year(Base):
        __tablename__= "complaints_per_year"

        year = Column(Integer, primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"complaints_per_year(year={self.year!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = per_year.values.tolist()
    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = complaints_per_year(
                year = item[0],
                count = item[1]
                )

                to_commit_list.append(commit_item)
    
            session.add_all(to_commit_list)
            session.commit()

        return "exito"
    
    except:

        traceback.print_exc()

        return "fallo"




@flow
def flujo_analitica():

    complaint_dataset =  lectura_quejas()

    state_population_dataset = lectura_info_estado()

    connAlchemy_aws = conectar_a_base()

    estado_1 = generar_por_producto(complaint_dataset, connAlchemy_aws)

    estado_2 = generar_por_issue(complaint_dataset, connAlchemy_aws)

    estado_3 = generar_por_estado(complaint_dataset, state_population_dataset, connAlchemy_aws)

    estado_4 = generar_por_canal(complaint_dataset, connAlchemy_aws)

    estado_5 = generar_por_anio(complaint_dataset, connAlchemy_aws)

    print(estado_1, estado_2, estado_3, estado_4, estado_5)

    return (estado_1, estado_2, estado_3, estado_4, estado_5)

# Condicion para solo ejecutar el archivo cuando se ejecute directamente?
if __name__ == "__main__":
    flujo_analitica()