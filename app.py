from flask import Flask

from my_app.momentjs import momentjs


app = Flask(__name__)

# set jinja template global
app.jinja_env.globals['momentjs'] = momentjs

@app.route("/")
def hello_world():
    return 'Hello world from the planet Flask!'

if __name__ == '__main__':
    app.run()