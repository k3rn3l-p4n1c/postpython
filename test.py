from postpython.core import PostPython

pp = PostPython('/path/to/collection/Bazinama.postman_collection.json')
pp.environments.update({'BASE_URL': 'http://127.0.0.1:5000', 'PASSWORD': 'test', 'EMAIL': 'info@example.com'})
pp.environments.update(pp.User.login().json()['message'])

print(pp.User.get_my_info().json())
