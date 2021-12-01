import sys

from setuptools import setup, find_packages
from procedure_tools.version import __version__

if sys.version_info >= (3, 4):
    install_requires = [
        "requests",
        "python-dateutil",
        "colorama",
    ]
    tests_require = [
        "pytest",
    ]
else:
    install_requires = [
        "requests",
        "pathlib",
        "python-dateutil",
        "colorama",
    ]
    tests_require = [
        "pytest<=4.6.9",
        "mock<4.0.0",
        "configparser<5.0.0",
        "zipp<3.1.0",
    ]

color_require = [
    "colorama",
]

setup(
    name="procedure_tools",
    version=__version__,
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=["pytest-runner"],
    extras_require={
        "test": tests_require,
        "color": color_require,
    },
    entry_points={
        "console_scripts": [
            "procedure=procedure_tools.procedure:main",
        ],
    },
    package_data={"": ["data/*.json"]},
)
