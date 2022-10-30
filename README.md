# Creating a custom Jinja2 filter

After looking at the previous recipe, experienced developers might wonder why we used a context processor for the purpose of creating a well-formatted product name. Well, we can also write a filter for the same purpose, which will make things much cleaner. A filter can be written to display the descriptive name of a product, as shown in the following example:

```python
@product_blueprint.app_template_filter('full_name') 
def full_name_filter(product): 
    return '{0} / {1}'.format(product['category'], product['name'])
```

This can also be used as follows:

```html
{{ product|full_name }} 
```

The preceding code will yield a similar result as in the previous recipe. Moving on, let's now take things to a higher level by using external libraries to format currency.

First, let's create a filter to format a currency based on the current local language. Add the following code to `my_app/__init__.py`:

```python
import ccy 
from flask import request 
 
@app.template_filter('format_currency') 
def format_currency_filter(amount): 
    currency_code = ccy.countryccy(request.accept_languages.best[-2:]) 
    return '{0} {1}'.format(currency_code, amount)
```

> `request.accept_languages` might not work in cases where a request does not have the `ACCEPT-LANGUAGES` *header*. The preceding snippet will require the installation of a new package, ccy, as follows:

```bash
pip3 install ccy
```

The filter created in this example takes the language that best matches the current browser locale (which, in my case, is en-US), takes the last two characters from the locale string, and then generates the currency as per the ISO country code, which is represented by the two characters.

> An interesting point to note in this recipe is that the Jinja2 filter can be created at the blueprint level as well as at the application level. If the filter is at the blueprint level, the decorator would be app_template_filter; otherwise, at the application level, the decorator would be template_filter.

The *Implementing block composition and layout inheritance* branch will aid your understanding of the context of this recipe.
