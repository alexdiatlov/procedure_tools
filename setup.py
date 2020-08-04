from setuptools import setup, find_packages
from procedure_tools.version import __version__

setup(
    name="procedure_tools",
    version=__version__,
    packages=find_packages(),
    python_requires=">=2.7",
    install_requires=[
        "requests",
        "pathlib",
        "python-dateutil",
    ],
    tests_require=[
        "pytest<=4.0.0",
        "mock<4.0.0",
        "configparser<5.0.0",
        "zipp<3.1.0",
    ],
    setup_requires=["pytest-runner"],
    entry_points={"console_scripts": ["procedure=procedure_tools.procedure:main"]},
    package_data={"": ["data/*.json"]},
)
