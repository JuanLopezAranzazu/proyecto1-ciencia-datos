from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class FactInvoice(Base):
  __tablename__ = "fact_invoice"

  id = Column(String, primary_key=True)
  price = Column(Float)
  quantity = Column(Integer)
  customer_id = Column(String, ForeignKey("dim_customer.id"))
  category_id = Column(Integer, ForeignKey("dim_category.id"))
  payment_method_id = Column(Integer, ForeignKey("dim_payment_method.id"))
  shopping_mall_id = Column(Integer, ForeignKey("dim_shopping_mall.id"))
  date_id = Column(Integer, ForeignKey("dim_date.id"))

  customer = relationship("DimCustomer", back_populates="invoices")
  category = relationship("DimCategory", back_populates="invoices")
  payment_method = relationship("DimPaymentMethod", back_populates="invoices")
  shopping_mall = relationship("DimShoppingMall", back_populates="invoices")
  date = relationship("DimDate", back_populates="invoices")
  