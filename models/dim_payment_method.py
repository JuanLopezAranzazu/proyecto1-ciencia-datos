from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base

class DimPaymentMethod(Base):
  __tablename__ = "dim_payment_method"

  id = Column(Integer, primary_key=True)
  name = Column(String) # nombre del método de pago

  invoices = relationship("FactInvoice", back_populates="payment_method", cascade="all, delete")
