# Postpython
Postpython is a library for [Postman](https://www.getpostman.com/) that run postman's collections.
If you are using postman, but collection runner is not flexible enough for you and postman codegen is too boring,
Postpython is here for your continuous integration.

## Why use Postpython instead of postman codegen?
- Postman codegen should be applied one by one for each request and it's boring when your api changes,
 but with postpython you don't need to generate code.
 Just export collection with postman and use it with Postpython.
- In code generation you don't have environment feature any more and variables are hardcoded.

## Why user Postpython instead of Postman collection runner?
- With postpython you write your own script. But collection runner just tun all your requests one by one.
So with Postpython you can design more complex test suites.

## How to install?
Postpython is available on [PyPI](https://pypi.python.org/pypi?name=postpython&version=0.1.2&:action=display) and you can install it using pip:
```
$ pip install postpython
```
## How to use?

Import `PostPython`
```$python
from postpython.core import PostPython
```
Make an instance from `PostPython` and give address of postman collection file.
```$python
runner = PostPython('/path/to/collection/Postman echo.postman_collection')
```
Now you can call your request. Folders' name change to upper camel case and requests' name change to lowercase form.
In this example the name of folder is "Request Methods" and it's change to `RequestMethods` and the name of request was
"GET Request" and it's change to `get_request`. So you should call a function like `runner.YourFolderName.you_request_name()`
```$python
response = runner.RequestMethods.get_request()
print(response.json())
print(response.status_code)
```

### Variable assignment
In Postpython you can assign values to environment variables in runtime.
```
runner.environments.update({'BASE_URL': 'http://127.0.0.1:5000'})
runner.environments.update({'PASSWORD': 'test', 'EMAIL': 'you@email.com'})
```
### AttributeError
Since `RequestMethods` and `get_request` does not really exists you intelligent IDE cannot help you.
So Postpython try to correct you mistakes. If you spell a function or folder wrong it will suggest you the closest name.
```
>>> response = runner.RequestMethods.get_requasts()

Traceback (most recent call last):
  File "test.py", line 11, in <module>
    response = runner.RequestMethods.get_requasts()
  File "/usr/local/lib/python3.5/site-packages/postpython/core.py", line 73, in __getattr__
    'Did you mean %s' % (item, self.name, similar))
AttributeError: get_requasts request does not exist in RequestMethods folder.
Did you mean get_request

```
You can also use `help()` function to print all available requests.
```
>>> runner.help()
Posible requests:
runner.AuthOthers.hawk_auth()
runner.AuthOthers.basic_auth()
runner.AuthOthers.oauth1_0_verify_signature()
runner.RequestMethods.get_request()
runner.RequestMethods.put_request()
runner.RequestMethods.delete_request()
runner.RequestMethods.post_request()
runner.RequestMethods.patch_request()
...

>>> runner.RequestMethods.help()
runner.RequestMethods.delete_request()
runner.RequestMethods.patch_request()
runner.RequestMethods.get_request()
runner.RequestMethods.put_request()
runner.RequestMethods.post_request()

```

## Contribution
Feel free to share your ideas or any problems in [issues](https://github.com/k3rn3l-p4n1c/postpython/issues).
Contributions are welcomed. Give postpython a star to encourage me to continue its development.
