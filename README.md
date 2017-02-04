# Postpython
Post python is a library for postman that turn postman collection file
into python functions.

### Postpython vs Postman Codegen
- Postman codegen should be applied one by one but postpython work work
 with whole collection.
- Environment variables support.

### How to use?

```$python
from core import PostPython

pp = PostPython('../path/to/yout/postman/collection/YouApi.postman_collection.json')
pp.environments.update({'BASE_URL': 'http://127.0.0.1:5000', 'PASSWORD': 'test', 'EMAIL': 'info@medrick.com'})
pp.environments.update(pp.User.login().json()['message'])
print(pp.User.get_my_info().json())
```