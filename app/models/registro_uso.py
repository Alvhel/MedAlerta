from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class RegistroUso(Base):
    __tablename__ = "registro_uso"

    id_registro = Column(Integer, primary_key=True, autoincrement=True)
    id_alerta = Column(Integer, ForeignKey("alerta.id_alerta"), nullable=False)
    data_horario_consumo = Column(DateTime, nullable=False)
    observacoes = Column(String(200))

    alerta = relationship("Alerta", back_populates="registro_uso")