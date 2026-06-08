from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(10))
    email = Column(String(100), nullable=False, unique=True)
    endereco_rua = Column(String(100))
    endereco_numero = Column(Integer)
    endereco_complemento = Column(String(50))
    endereco_bairro = Column(String(50))
    endereco_cep = Column(String(10))
    endereco_cidade = Column(String(50))
    endereco_estado = Column(String(2))

    medicamentos = relationship("UsuarioMedicamento", back_populates="usuario")
