# Creating a custom macro for forms

Macros **allow us to write reusable pieces of HTML blocks**. They are analogous to functions in regular programming languages. **We can pass arguments to macros as we do to functions in Python, and we can then use them to process an HTML block**. Macros can be called any number of times, and the output will vary as per the logic inside them. In this recipe, let's understand how to write a macro in Jinja2.

One of the most redundant pieces of code in HTML is that which defines input fields in forms. This is because most fields have similar code with style modifications, for example.

The following snippet is a macro that creates input fields when called. Best practice is to create the macro in a separate file for better reusability, for example, `_helpers.html`:

```html
{% macro render_field(name, class='', value='', type='text') -%} 
    <input type="{{ type }}" name="{{ name }}" class="{{ class }}" 
        value="{{ value }}"/> 
{%- endmacro %} 
```

> The minus sign (-) before and after % will strip the whitespace before and after these blocks, making the HTML code cleaner to read.

Now the macro should be imported in the file to be used, as follows:

```html
{% from '_helpers.html' import render_field %} 
```

it can now be called using the following code:

```html
<fieldset> 
    {{ render_field('username', 'icon-user') }} 
    {{ render_field('password', 'icon-key', type='password') }} 
</fieldset>
```

It is always good practice to define macros in a different file to keep the code clean and increase code readability.

> If you need to write a private macro that cannot be accessed from outside its current file, name the macro with an underscore preceding the name
