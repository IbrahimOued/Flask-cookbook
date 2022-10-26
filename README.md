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
