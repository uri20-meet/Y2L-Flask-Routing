from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
	"""docstring for ClassName"""
	__tablename__ = 'products':
		id = Column(Integer, primary_key = True)
		name = Column(String)
		price = Column(Float)
		pictureLink = Column(String)
		description = Column(String)

class Cart(Base):
	"""docstring for ClassName"""
	__tablename__ = 'carts':
		id = Column(Integer, primary_key = True)
		productID = Column(Integer)
