# Making a Flask app installable using setuptools

We now have a Flask app, but how do we install it like any Python package? It is possible that another application might depend on our application, or that our application is in fact an extension for Flask and would need to be installed in a Python environment so it can be used by other applications. In this recipe, we will see how `setuptools` can be used to create an installable Python package.

most of the configuration is self-explanatory. The classifiers are used when the application is made available on PyPI. These will help other users search the application using the relevant classifiers.

Now, we can run this file with the install keyword, as follows:

```bash
$ python setup.py install
```

The preceding command will install the application along with all the dependencies mentioned in install_requires, that is, Flask and all of Flask's dependencies. Now the app can be used just like any Python package in a Python environment.
