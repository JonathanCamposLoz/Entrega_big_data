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

import nltk

from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer
from functools import partial

import pandas as pd

from collections import Counter
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer

from prefect import task, flow

import traceback

@task
def lectura_quejas():
    complaint_dataset = pd.read_csv("Datasets/complaint_data.csv")

    complaint_dataset = complaint_dataset[complaint_dataset['Consumer complaint narrative'].notnull()]

    return complaint_dataset

@task
def descargar_stopwords():
    stopword_set = set(stopwords.words('english'))
    stopword_list = list(stopword_set)

    stopword_list.append("xx")

    stopword_list.append("xxxx")

    stopword_list.append("00")

    return stopword_list

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
def contar_palabras_credit_reporting(connAlchemy_aws,stopword_list,complaint_dataset):

    complaint_credit_rep =  complaint_dataset[complaint_dataset['Product'] == "Credit reporting, credit repair services, or other personal consumer reports"] 

    def get_top_n_words(corpus, n=1, k=1):
        vec = CountVectorizer(ngram_range=(k, k), stop_words= stopword_list)
        bag_of_words = vec.fit_transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        return words_freq[:n]
    
    common_words = get_top_n_words(complaint_credit_rep["Consumer complaint narrative"], 20, 1)

    df_top_words = pd.DataFrame(common_words, columns=["words", "count"])
    
    Base = declarative_base()

    class top_words_credit_reporting(Base):
        __tablename__= "top_words_credit_reporting"

        word = Column(String(100), primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"top_words_credit_reporting(word={self.word!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = df_top_words.values.tolist()

    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = top_words_credit_reporting(
                word = item[0],
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
def contar_palabras_mortgage(connAlchemy_aws,stopword_list,complaint_dataset):

    complaint_credit_mortgage =  complaint_dataset[complaint_dataset['Product'] == "Mortgage"] 

    def get_top_n_words(corpus, n=1, k=1):
        vec = CountVectorizer(ngram_range=(k, k), stop_words= stopword_list)
        bag_of_words = vec.fit_transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        return words_freq[:n]
    
    common_words = get_top_n_words(complaint_credit_mortgage["Consumer complaint narrative"], 20, 1)

    df_top_words = pd.DataFrame(common_words, columns=["words", "count"])
    
    Base = declarative_base()

    class top_words_mortgage(Base):
        __tablename__= "top_words_mortgage"

        word = Column(String(100), primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"top_words_mortgage(word={self.word!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = df_top_words.values.tolist()

    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = top_words_mortgage(
                word = item[0],
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
def contar_palabras_debt_collection(connAlchemy_aws,stopword_list,complaint_dataset):

    complaint_credit_debt_collection =  complaint_dataset[complaint_dataset['Product'] == "Debt collection"] 

    def get_top_n_words(corpus, n=1, k=1):
        vec = CountVectorizer(ngram_range=(k, k), stop_words= stopword_list)
        bag_of_words = vec.fit_transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        return words_freq[:n]
    
    common_words = get_top_n_words(complaint_credit_debt_collection["Consumer complaint narrative"], 20, 1)

    df_top_words = pd.DataFrame(common_words, columns=["words", "count"])
    
    Base = declarative_base()

    class top_words_debt_collection(Base):
        __tablename__= "top_words_debt_collection"

        word = Column(String(100), primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"top_words_debt_collection(word={self.word!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = df_top_words.values.tolist()

    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = top_words_debt_collection(
                word = item[0],
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
def contar_palabras_all(connAlchemy_aws,stopword_list,complaint_dataset):

    def get_top_n_words(corpus, n=1, k=1):
        vec = CountVectorizer(ngram_range=(k, k), stop_words= stopword_list)
        bag_of_words = vec.fit_transform(corpus)
        sum_words = bag_of_words.sum(axis=0) 
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        return words_freq[:n]
    
    common_words = get_top_n_words(complaint_dataset["Consumer complaint narrative"], 20, 1)

    df_top_words = pd.DataFrame(common_words, columns=["words", "count"])
    
    Base = declarative_base()

    class top_words_all_complaints(Base):
        __tablename__= "top_words_all_complaints"

        word = Column(String(100), primary_key=True)
        count = Column(Integer)

        def __repr__(self):
            return f"top_words_all_complaints(word={self.word!r}, count={self.count!r})"
        
    Base.metadata.create_all(connAlchemy_aws)

    regis_list = df_top_words.values.tolist()

    
    try:
        with Session(connAlchemy_aws) as session:

            to_commit_list = []

            for item in regis_list:
                commit_item = top_words_all_complaints(
                word = item[0],
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

    stopwords = descargar_stopwords()

    connAlchemy_aws = conectar_a_base()

    estado_1 = contar_palabras_all(connAlchemy_aws, stopwords, complaint_dataset)

    estado_2 = contar_palabras_credit_reporting(connAlchemy_aws, stopwords, complaint_dataset)

    estado_3 = contar_palabras_debt_collection(connAlchemy_aws, stopwords, complaint_dataset)

    estado_4 = contar_palabras_mortgage(connAlchemy_aws, stopwords, complaint_dataset)

    print(estado_1, estado_2, estado_3, estado_4)

    return (estado_1,estado_2,estado_3,estado_4)

# Condicion para solo ejecutar el archivo cuando se ejecute directamente?
if __name__ == "__main__":
    flujo_analitica()