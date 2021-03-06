from setuptools import setup

setup(name='unbabel-py',
      version='0.22',
      description='Python Wrapper around Unbabel HTTP API',
      author='Joao Graca',
      author_email='gracaninja@unbabel.co',
      packages=[
          'unbabel',
          ],
      package_dir={
        'unbabel': 'unbabel/',
        },
      install_requires=[
        'requests',
          ],
      url = 'https://github.com/Unbabel/unbabel-py',
      download_url = 'https://github.com/Unbabel/unbabel-py/tarball/0.1',
      classifiers = ['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python ',
                     'Topic :: Text Processing'
                     ]
      )
