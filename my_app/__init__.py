from flask import Flask 
from my_app.product.views import product_blueprint
import ccy 
from flask import request
 
app = Flask(__name__) 
app.register_blueprint(product_blueprint) 

@app.template_filter('format_currency') 
def format_currency_filter(amount): 
    currency_code = ccy.countryccy(request.accept_languages.best[-2:]) 
    return '{0} {1}'.format(currency_code, amount)