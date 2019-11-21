from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, pictureLink, description):
	product = Product(
		name = name, 
		price = price, 
		pictureLink = pictureLink, 
		description = description)
	session.add(product)
	session.commit()

def edit_by_id(id, attribute, value):
	prod = session.query(Product).filter_by(id = id)
	prod.attribute = value
	session.commit()

def delete_by_id(id):
	session.query(Product).filter_by(id = id).delete()
	session.commit()

def get_all_products():
	return(session.query(Product).all())

def get_by_id(id):
	return(session.query(Product).filter_by(id = id))

def add_to_cart(productID):
	cart = Cart(
		productID = productID)
	session.add(cart)
	session.commit()

# add_product("product1", 39.99, "static/product1.jpg", "product 1 is surely the best product you will ever find")
# add_product("product2", 19.99, "static/product1.jpg", "product 2 is just a bit better than product 1 I swear")
