from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import get_all_products, add_to_cart

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/store')
def store():
	return render_template("store.html")

@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/store/cart', methods=['GET' , 'POST'])
def cart():
	if request.method == 'GET':
		n = get_all_products()
		return render_template("cart.html", products = n)
	else:
		# added = 
		# add_to_cart(added)
		n = get_all_products()
		return render_template("cart.html", products = n)
	


if __name__ == '__main__':
    app.run(debug=True)

