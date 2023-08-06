from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='a folder that cleans files',
      author='Fedorchenko Tetiana',
      author_email='tasiafedochenko@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:start']})