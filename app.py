from flask import Flask

# This tells the application to load the configuration
# file from the instance folder. The following example
# shows how this will work:
app = Flask( 
    __name__, instance_path='path/to/instance/folder', 
    instance_relative_config=True 
) 
app.config.from_pyfile('config.cfg', silent=True) 

@app.route("/")
def hello_world():
    return 'Hello world from the planet Flask!'

if __name__ == '__main__':
    app.run()