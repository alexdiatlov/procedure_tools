from setuptools import setup
from version import __version__

setup(
    name='procedure_tools',
    version=__version__,
    python_requires='>=2.7',
    install_requires=[
        'requests',
        'pathlib',
        'python-dateutil',
    ],
    entry_points={
        'console_scripts': [
            'procedure=procedure:main',
        ],
    },
)
