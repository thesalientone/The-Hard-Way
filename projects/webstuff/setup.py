try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {

    'description': 'My Project',
    'author': 'Phoenix',
    'url': 'URL to get it at.',
    'download_url' : 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['webstuff'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
