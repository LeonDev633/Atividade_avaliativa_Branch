from sqlalchemy import Column, Integer, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dataclasses import dataclass
from Feature_main import lanche

BD = create_engine("sqlite:///bancodedadosvendas.bd")

Session = sessionmaker(bind=BD)
session = Session()
Base = declarative_base()

@dataclass
class Usuario(Base):
    __tablename__ = "vendas"
    id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String)
    sobrenome = Column(String)
    senha = Column(String)

@dataclass
class Lanche(Base):
    __tablename__ = "lanches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    preco = Column(Float)

Base.metadata.create_all(bind=BD)