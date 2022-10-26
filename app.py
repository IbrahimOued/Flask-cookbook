from flask import Flask
app = Flask(__name__)
DEBUG = True
TESTING = True

app.config.from_object(__name__)
app.config.from_pyfile('./myconfig')

@app.route("/")
def hello_world():
    return 'Hello world from the planet Flask!'

if __name__ == '__main__':
    # This example also
    # app.run('debug=True')
    app.run()