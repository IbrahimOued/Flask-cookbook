# Creating a modular web app with blueprints

A blueprint is a concept in Flask that helps make large applications really modular. This keeps application dispatching simple by providing a central place to register all components in an application. A blueprint looks like an application object but is not an application. It also looks like a pluggable app, or a smaller part of a bigger app, but it is not. A blueprint is actually a set of operations that can be registered on an application and represents how to construct or build an application.

We have now defined a blueprint in the `flask_app/my_app/hello/views.py` file. We no longer need the application object anymore, and our complete routing is defined on a blueprint named hello. Instead of @app.route, we use @hello.route. The same blueprint is imported into `flask_app/my_app/__init__.py` and registered on the application object.

We can create any number of blueprints in our application and complete most of the activities that we would usually do, such as providing different template paths or different static paths. We can even have different URL prefixes or subdomains for our blueprints.
