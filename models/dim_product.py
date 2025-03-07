from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.database import Base

class DimProduct(Base):
  __tablename__ = "dim_product"

  id = Column(Integer, primary_key=True)
  name = Column(String) # nombre de la categoría
  price = Column(Float) # precio del producto

  invoices = relationship("FactInvoice", back_populates="product", cascade="all, delete")
