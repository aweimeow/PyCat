import setuptools
from distutils.core import setup

entry_points = {
    'console_scripts': [
        'pycat = PyCat.pycat:_main'
    ]
}

setup(
  name='PyCat',
  packages=['PyCat'],
  version='1.0',
  description='NetCat wrote in Python',
  author='aweimeow, sufuf3, ActKz, hsiaohsuan1l1l',
  author_email='aweimemow.tw@gmail.com',
  url='https://github.com/aweimeow/PyCat',
  download_url=('https://github.com/aweimeow/'
                'PyCat/archive/master.tar.gz'),
  keywords=['PyCat', 'netcat'],
  classifiers=[],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
  entry_points=entry_points,
)
