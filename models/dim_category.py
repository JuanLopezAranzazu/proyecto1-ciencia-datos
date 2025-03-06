from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class DimCategory(Base):
  __tablename__ = "dim_category"

  id = Column(Integer, primary_key=True)
  name = Column(String) # nombre de la categoría

  invoices = relationship("FactInvoice", back_populates="category", cascade="all, delete")
