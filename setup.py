from setuptools import setup, find_packages
from procedure_tools.version import __version__

setup(
    name='procedure_tools',
    version=__version__,
    packages=find_packages(),
    python_requires='>=2.7',
    install_requires=[
        'requests',
        'pathlib',
        'python-dateutil',
    ],
    entry_points={
        'console_scripts': [
            'procedure=procedure_tools.procedure:main',
        ],
    },
    package_data={'': ['data/*.json']},
)
