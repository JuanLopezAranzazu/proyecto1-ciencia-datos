from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import relationship
from db.database import Base

class DimDate(Base):
  __tablename__ = "dim_date"

  id = Column(Integer, primary_key=True)
  full_date = Column(Date)
  day = Column(Integer)
  month = Column(Integer)
  year = Column(Integer)
  day_of_week = Column(Integer)

  invoices = relationship("FactInvoice", back_populates="date", cascade="all, delete")
