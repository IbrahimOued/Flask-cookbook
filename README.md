# Organizing static files

Flask recommends a specific way of organizing static files in an application, as follows:

```yml
my_app/
    - app.py
    - config.py
    - __init__.py
    - static/
        - css/
        - js/
        - images/
            - logo.png
```

While rendering this in templates (say, the logo.png file), we can refer to the static files using the following code:

```html
<img src='/static/images/logo.png'>
```

Alternatively, we can provide a parameter named static_folder to the application object while defining the application in app.py, as follows:

```python
app = Flask(__name__, static_folder='/path/to/static/folder') 
```

In the preceding line of code, static refers to the value of static_url_path on the application object. This can be modified as follows:

```python
app = Flask( 
    __name__, static_url_path='/differentstatic', 
    static_folder='/path/to/static/folder' 
)
```

Now, to render the static file, we will use the following code:

```html
<img src='/differentstatic/logo.png'>
```

It is always a good practice to use url_for to create URLs for static files rather than explicitly defining them, as follows:

```html
<img src="{{ url_for('static', filename='logo.png') }}">
```
