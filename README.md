# Being deployment-specific with instance folders

Flask provides yet another method for configuration, where we can efficiently manage deployment-specific parts. Instance folders allow us to segregate deployment-specific files from our version-controlled application. We know that **configuration files can be separate for different deployment environments, such as development and production, but there are also many more files, such as database files, session files, cache files, and other runtime files**. We will **create an instance folder, which will act like a holder bin for such kinds of files**.

By default, the instance folder is picked up from the application automatically if we have a folder name `instance` in our application at the application level, as follows:

```yml
my_app/
    - app.py
    - instance/
        - config.cfg
```

We can also explicitly define the absolute path of the instance folder using the `instance_path` parameter on our application object, as follows:

```python
app = Flask(
    __name__, instance_path='/absolute/path/to/instance/folder'
)
```

To load the configuration file from the instance folder, we will use the `instance_relative_config` parameter on the application object, as follows:

```py
app = Flask(
    __name__, instance_path='path/to/instance/folder', instance_relative_config=True
)
app.config.from_pyfile('config.cfg', silent=True)
```

In the preceding code, first, the instance folder is loaded from the given path, and then, the configuration file is loaded from the file named config.cfg in the given instance folder. Here, `silent=True` is optional and is used to suppress the error if config.cfg is not found in the instance folder.

> It might seem that loading the configuration from the instance folder using `instance_relative_config` is redundant work and could be moved to one of the configuration methods itself. However, the beauty of this process lies in the fact that the instance folder concept is completely independent of configuration, and `instance_relative_config` just complements the configuration object.