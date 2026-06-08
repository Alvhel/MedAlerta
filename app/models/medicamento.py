from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class FormaUsoEnum(str, enum.Enum):
    unidade = "unidade"
    ml = "ml"

class Medicamento(Base):
    __tablename__ = "medicamento"

    id_medicamento = Column(Integer, primary_key=True, autoincrement=True)
    nome_comercial = Column(String(100), nullable=False)
    nome_generico = Column(String(100))
    quantidade = Column(Integer, nullable=False)
    forma_uso = Column(Enum(FormaUsoEnum), nullable=False)
    observacoes = Column(String(200))

    usuarios = relationship("UsuarioMedicamento", back_populates="medicamento")
