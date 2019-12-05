from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import get_all_products, add_to_cart, get_cart, get_by_name

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/', methods=['GET' , 'POST'])
def homepage():
	if request.method == 'GET':
		loggedIn = False
		return render_template("home.html", loggedIn = loggedIn)
	else:
		loggedIn = True
		username = request.form['username']
		return render_template("home.html", loggedIn = loggedIn, username = username)

@app.route('/store')
def store():
	products = get_all_products()
	return render_template("store.html", products = products)

@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/cart', methods=['GET' , 'POST'])
def cart():
	if request.method == 'GET':
		userCart = get_cart()
		allProducts = get_all_products()
		return render_template("cart.html", allProducts = allProducts, userCart = userCart)
	else:
		added = request.form['added']
		add_to_cart(added)
		userCart = get_cart()
		allProducts = get_all_products()
		return render_template("cart.html", allProducts = allProducts, userCart = userCart)
	

@app.route('/login')
def login():
	
	return render_template("login.html")

@app.route('/portal')
def portal():
	allProducts = get_all_products()
	return render_template("portal.html", allProducts = allProducts)


if __name__ == '__main__':
    app.run(debug=True)

