from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class DimShoppingMall(Base):
  __tablename__ = "dim_shopping_mall"

  id = Column(Integer, primary_key=True)
  name = Column(String)

  invoices = relationship("FactInvoice", back_populates="shopping_mall", cascade="all, delete")
