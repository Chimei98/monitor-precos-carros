from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# conexão ao banco de dados
engine = create_engine('sqlite:///carros-db.db')
Base = declarative_base()
_Sessao = sessionmaker(engine)

class Carro(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True) # identificador de cada carro.
    nome = Column(String(255))
    preco = Column(Integer())
    quilometragem = Column(Integer())
    combustivel = Column(String(255))
    caixa = Column(String(255))
    link = Column(String(255), unique=True) # prevenção de duplicatas.


Base.metadata.create_all(engine)