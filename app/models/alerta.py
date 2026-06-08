from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class StatusAlertaEnum(str, enum.Enum):
    pendente = "pendente"
    consumido = "consumido"
    nao_consumido = "nao_consumido"


class Alerta(Base):
    __tablename__ = "alerta"

    id_alerta = Column(Integer, primary_key=True, autoincrement=True)
    id_tratamento = Column(Integer, ForeignKey("usuario_medicamento.id_tratamento"), nullable=False)
    data_horario_alerta = Column(DateTime, nullable=False)
    status_alerta = Column(Enum(StatusAlertaEnum), default=StatusAlertaEnum.pendente, nullable=False)

    tratamento = relationship("UsuarioMedicamento", back_populates="alertas")
    registro_uso = relationship("RegistroUso", back_populates="alerta", uselist=False)