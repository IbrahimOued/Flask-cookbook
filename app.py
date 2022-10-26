from flask import Flask
app = Flask(__name__)

app.config.from_object('configuration.DevelopmentConfig') 


@app.route("/")
def hello_world():
    return 'Hello world from the planet Flask!'

if __name__ == '__main__':
    app.run()