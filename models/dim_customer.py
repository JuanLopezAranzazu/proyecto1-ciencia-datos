from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from db.database import Base
import enum

class GenderEnum(enum.Enum):
  Female = "Female"
  Male = "Male"

class DimCustomer(Base):
  __tablename__ = "dim_customer"

  id = Column(String, primary_key=True)
  gender = Column(Enum(GenderEnum))
  age = Column(Integer)

  invoices = relationship("FactInvoice", back_populates="dim_customer", cascade="all, delete")
