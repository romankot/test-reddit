from setuptools import setup
from setuptools import find_packages


if __name__ == '__main__':

    setup(
        name='test-reddit',
        version='0.1',
        license='MIT',
        platforms='any',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'click==6.6',
            'requests==2.10.0',
        ],
        entry_points='''
            [console_scripts]
            reddit-cli=reddit.app:cli
        ''',
    )
