from flask import Flask
app = Flask(__name__)

# from my_app.hello.views import *
import my_app.hello.views
