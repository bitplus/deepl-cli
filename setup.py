from setuptools import setup, find_packages
setup(
    name='deepl-cli',
    version='0.0.1',
    description='',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eggplants/deepl-cli',
    author='eggplants',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    install_requires=['selenium==3.141'],
    entry_points={
        'console_scripts': [
            'deepl=deepl.main:main'
        ]
    }
)
