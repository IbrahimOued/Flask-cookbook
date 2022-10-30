# Creating a custom context processor

Sometimes, we **might want to calculate or process a value directly in templates**. Jinja2 maintains the notion that **the processing of logic should be handled in views and not in templates**, and so keeps templates clean. A context processor becomes a handy tool in this case. With a context processor, we can pass our values to a method, which will then be processed in a Python method, and our resultant value will be returned. This is done by simply adding a function to the template context, thanks to Python allowing its users to pass functions like any other object

To write a custom context processor, follow the required steps.

Let's first display the descriptive name of the product in the format `Category / Product-name`. Afterwards, add the method to `my_app/product/views.py`, as follows:

```python
@product_blueprint.context_processor
def product_name_processor(): 
    def full_name(product): 
        return '{0} / {1}'.format(product['category'], 
           product['name']) 
    return {'full_name': full_name}
```

A context is simply a dictionary that can be modified to add or remove values. Any method decorated with @product_blueprint.context_processor should return a dictionary that updates the actual context. We can use the preceding context processor as follows:

```python
{{ full_name(product) }} 
```

We can add the preceding code to our app for the product listing (in the `flask_app/my_app/templates/product.html` file) in the following manner:

```html
{% extends 'home.html' %} 
 
{% block container %} 
  <div class="top-pad"> 
    <h4>{{ full_name(product) }}</h4> 
    <h1>{{ product['name'] }} 
      <small>{{ product['category'] }}</small> 
    </h1> 
    <h3>$ {{ product['price'] }}</h3> 
  </div> 
{% endblock %}
```

The resulting parsed HTML page should look like the following screenshot:

