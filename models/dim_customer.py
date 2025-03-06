from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class DimCustomer(Base):
  __tablename__ = "dim_customer"

  id = Column(String, primary_key=True)
  gender = Column(String) # género
  age = Column(Integer) # edad

  invoices = relationship("FactInvoice", back_populates="customer", cascade="all, delete")
