from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()


setup(
    name="gkutils-genghisken", # Replace with your own username
    description='A collection useful utilities',
    long_description=readme(),
    long_description_content_type="text/markdown",
    version="0.0.1",
    author='genghisken',
    author_email='ken.w.smith@gmail.com',
    license='MIT',
    url='https://github.com/genghisken/gkutils',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities',
    ],
    python_requires='>=3.6',
)
