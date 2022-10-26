# Composition of views and models

As our application grows bigger, we might want to structure it in a modular manner. In this recipe, we will do this by restructuring our *Hello World* application.

First, create a new folder in the application and move all files inside this new folder.

Then, create `__init__.py` in the folders, which are to be used as modules.

After that, create a new file called `run.py` in the topmost folder. As the name implies, this file will be used to run the application.

Finally, create separate folders to act as modules.

```yml
flask_app/
    - run.py
    - my_app/
        - __init__py
        - hello/
            - __init__.py
            - models.py
            - views.py
```

Let's see how each of the preceding files will look.

The `flask_app/run.py` file will look something like the following lines of code:

```python
from my_app import app 
app.run(debug=True)
```

The `flask_app/my_app/__init__.py` will look something like:

```python
from flask import Flask
app = Flask(__name__)
import my_app.hello.views
```

Next, we will have an empty file just to make the enclosing folder a Python package, `flask_app/my_app/hello/__init__.py`:

```python
# No content. 
# We need this file just to make this folder a python module.
```

The models file, `flask_app/my_app/hello/models.py`, has a non-persistent key-value store, as follows:

```python
MESSAGES = {
    'default': 'Hello to the word of flask!',
}
```

Finally, the following is the views file, `flask_app/my_app/hello/views.py`. Here, we fetch the message corresponding to the requested key and can also create or update a message:

```python
from my_app import app
from my_app.hello.models import MESSAGES

@app.route('/')
@app.route('/hello')
def hello_world():
    return MESSAGES['default']
    
@app.route('/show/<key>')
def get_messages(key):
    return MESSAGES.get(key) or "%s not found!" % key

@app.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key
```

> Remember that the preceding code is nowhere near production-ready. It is just for demonstration and to make things understandable for new users of Flask.
