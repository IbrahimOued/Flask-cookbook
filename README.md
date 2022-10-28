# Boostraping the recommanded layout

y default, Flask expects templates to be placed inside a folder named `templates` at the application root level. If this folder is present, then Flask will automatically read the contents by making the contents of this folder available for use with the `render_template()` method, which we will use extensively throughout this book.

The first thing to do is to add a new folder named `templates` under `my_app`. The application structure should look like the following directory structure:

```yml
flask_app/ 
    - run.py 
    my_app/ 
        - __init__.py 
        - hello/ 
            - __init__.py 
            - views.py 
        - templates
```