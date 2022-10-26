# Handling basic configurations

In flask, a configuration is done on an attribute named `config` of the `Flask` object. The `config` attribute is a subclass of a dictionary, and we can modify it just like any dictionary.

The debug Boolean can also be set at the Flask object level rather than at the config level, as follows:

```py
app.debug = True
```

Alternatively, we can pass debug as a named argument to app.run, as follows:
app.run(debug=True)
In new versions of Flask, the debug mode can also set on an environment variable, `FLASK_DEBUG=1`, and then run the app using flask run or Python's -m switch:

```bash
$ export FLASK_DEBUG=1
```

Enabling the debug mode will make the server reload itself in the event of any code changes, and it also provides the very helpful Werkzeug debugger when something goes wrong.

As an **application grows larger, there is a need to manage the application's configuration in a separate file**, as shown in the following example. Mostly specific to machine-based setups, it is unlikely that this will be a part of the version-control system. For this, Flask provides us with multiple ways to fetch configurations. The most frequently used methods are as follows:

* From a python configuration file (`*.cfg`), the configuration can be fetched using the following

```py
app.config.from_pyfile('myconfig.cfg')
```

* From an object, the configuration can be fetched using the following command:

```py
app.config.from_object(__name__)
```

* Alternatively, to load from the same file from which this command is run, we can also use the following command:

```python
app.config.from_object(__name__)
```

* From the environment variable, the configuration can be fetched using the following command:

```python
app.config.from_envvar('PATH_TO_CONFIG_FILE')
```
