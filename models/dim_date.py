from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from db.database import Base

class DimDate(Base):
  __tablename__ = "dim_date"

  id = Column(Integer, primary_key=True)
  full_date = Column(Date) # fecha completa
  day = Column(Integer) # día
  month = Column(Integer) # mes
  year = Column(Integer) # año
  day_of_week = Column(Integer) # día de la semana

  invoices = relationship("FactInvoice", back_populates="date", cascade="all, delete")
