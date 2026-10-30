from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey, DateTime, Date, String, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base, scoped_session

engine = create_engine('mysql+pymsql://root:senaisp@10.135.232.23:3306/projeto_final')
db_session =scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

class Ordem_servico(Base):
    __tablename__ = 'ordem_servico'
    id_os = Column(Integer, primary_key=True)
    id_equipemnto = Column(Integer, ForeignKey('equipemnto.id'))
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    descricao = Column(String(100), nullable=False)
    data_hora = Column(DateTime, nullable=False)

class Cliente(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    data_nsc = Column(DateTime, nullable=False)

class Equipamento(Base):
    __tablename__ = 'equipemntos'
    id_equipamento = Column(Integer, primary_key=True)
    fabricante = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)
    nome = Column(String(100), nullable=False)
    data_equipamento = Column(DateTime, nullable=False)
    horario = Column(DateTime, nullable=False)

class Recurso(Base):
    __tablename__ = 'recursos'
    id_recurso = Column(Integer, primary_key=True)
    nome_recurso = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)