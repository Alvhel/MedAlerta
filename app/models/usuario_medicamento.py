from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class UsuarioMedicamento(Base):
    __tablename__ = "usuario_medicamento"

    id_tratamento = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_medicamento = Column(Integer, ForeignKey("medicamento.id_medicamento"), nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    duracao_dias = Column(Integer, nullable=False)
    intervalo_horas = Column(Integer, nullable=False)
    dosagem = Column(String(50), nullable=False)
    observacoes = Column(String(200))

    usuario = relationship("Usuario", back_populates="medicamentos")
    medicamento = relationship("Medicamento", back_populates="usuarios")
    alertas = relationship("Alerta", back_populates="tratamento")