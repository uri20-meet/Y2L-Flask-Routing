from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
	"""docstring for ClassName"""
	__tablename__ = 'products'
	productId = Column(Integer, primary_key = True)
	name = Column(String)
	price = Column(Float)
	pictureLink = Column(String)
	description = Column(String)

	def __repr__(self):
		return("productId: {} \n"
			"name: {} \n"
			"price: {} \n"
			"pictureLink: {} \n"
			"description: {} \n"
			).format(self.productId,
			self.name,
			self.price,
			self.pictureLink,
			self.description)

class Cart(Base):
	"""docstring for ClassName"""
	__tablename__ = 'Cart'
	ID = Column(Integer, primary_key = True)
	productID = Column(Integer)

	def __repr__(self):
		return("ID: {} \n"
			"productID: {} \n"
			).format(self.ID, self.productID)


