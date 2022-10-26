# Configuring using class-based settings

An interesting way of laying out configurations for different deployment modes, such as **production**, **testing**, **staging**, and so on, can be cleanly done using the inheritance pattern of classes. Each mode can have several different configuration settings, or some settings that will remain the same. In this recipe, we will learn how to use class-based settings to achieve such a pattern.

```python
class BaseConfig(object): 
    'Base config class'
    SECRET_KEY = 'A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE = 'my value'
 
class ProductionConfig(BaseConfig): 
    'Production specific config' 
    DEBUG = False 
    SECRET_KEY = open('/path/to/secret/file').read() 
 
class StagingConfig(BaseConfig): 
    'Staging specific config' 
    DEBUG = True 
 
class DevelopmentConfig(BaseConfig): 
    'Development environment specific config' 
    DEBUG = True 
    TESTING = True 
    SECRET_KEY = 'Another random secret key'
```

> The **secret key** is stored in a separate file because, for security reasons, **it should not be a part of your version-control system**. This should be kept in the local filesystem on the machine itself, whether it is your personal machine or a server.

Now we can use any of the preceding classes while loading the application's configuration via from_object(). Let's say that we save the preceding class-based configuration in a file named configuration.py, as follows:

```python
app.config.from_object('configuration.DevelopmentConfig')
```

Overall, this makes the management of configurations for different deployment environments more flexible and easy.
