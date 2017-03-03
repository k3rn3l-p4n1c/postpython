from distutils.core import setup

setup(
    name='postpython',
    packages=['postpython'],
    version='0.1.2',
    description='A library to use postman collection in python.',
    author='Bardia Heydari nejad',
    author_email='bardia.heydarinejad@gmail.com',
    url='https://github.com/k3rn3l-p4n1c/postpython',
    download_url='https://codeload.github.com/k3rn3l-p4n1c/postpython/zip/master',  # I'll explain this in a second
    keywords=['postman', 'rest', 'api'],  # arbitrary keywords
    install_requires=[
        'requests',
    ],
    classifiers=[],
)
