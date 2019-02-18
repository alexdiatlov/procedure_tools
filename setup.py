from setuptools import setup
from version import __version__

setup(
    name="procedure_tools",
    version=__version__,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'procedure=procedure:main',
        ],
    },
)
