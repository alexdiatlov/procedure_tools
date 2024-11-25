from setuptools import find_packages, setup

from procedure_tools.version import __version__


install_requires = [
    "requests",
    "python-dateutil",
    "colorama",
    "jinja2",
    "faker",
]
tests_require = [
    "pytest",
]
color_require = [
    "colorama",
]

setup(
    name="procedure_tools",
    version=__version__,
    packages=find_packages(),
    python_requires=">=3.4",
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=["pytest-runner"],
    extras_require={
        "test": tests_require,
        "color": color_require,
    },
    entry_points={
        "console_scripts": [
            "procedure=procedure_tools.main:main",
        ],
    },
    package_data={"": ["data/*.json"]},
)
