from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Normalize',
      url='https://github.com/serjbuda/code/tree/main/Current_task/clean_folder',
      author='Buda Serj',
      author_email='buda_serj@yahoo.com',
      license='MIT',
      packages=find_namespace_packages()
      entry_points = {'console_scripts': ['clean-folder=clean-folder.clean:main']}
      )
