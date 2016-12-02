from setuptools import setup, find_packages
import easyflask

setup(
    name='easyflask',
    version=easyflask.__version__,
    author='guan ming',
    author_email='i@guanming.me',
    url='https://github.com/lennon-guan/easyflask',
    packages=find_packages(),
    package_data={
        '': ['*.tpl'],
    },
    description='Flask project generator',
    include_package_data=True,
    entry_points=dict(
        console_scripts=[
            'easyflask = easyflask.cli:main',
        ],
    ),
)
