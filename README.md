# Implementing block composition and layout inheritance

Usually, any web application will have a number of web pages that are different to each other. However, code blocks such as headers and footers will appear the same on almost all pages throughout the site; likewise, the menu will remain the same. In fact, it is usually just the center container block that changes. For this, Jinja2 provides a great way of ensuring inheritance among templates.

With this in mind, it's good practice to have a base template where the basic layout of the site, along with the header and footer, can be structured.

```yml
flask_app/ 
    - run.py 
    my_app/ 
        - __init__.py 
        - product/ 
            - __init__.py 
            - views.py 
            - models.py 
        - templates/ 
            - base.html 
            - home.html 
            - product.html 
        - static/ 
            - js/ 
                - bootstrap.min.js 
            - css/ 
                - bootstrap.min.css 
                - main.css 
```

The name of the blueprint (product) that is passed in the Blueprint constructor will be appended to the endpoints defined in this blueprint. Have a look at the base.html code for clarity.

> The abort() method comes in handy when you want to abort a request with a specific error message. Flask provides basic error message pages that can be customized as needed. We will look at them in the Creating custom 404 and 500 handlers

When considering templates, remember that the first template acts as the base for all templates. Name this template base.html and place it in `my_app/templates/base.html`, as follows:
