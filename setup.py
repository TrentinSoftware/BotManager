from setuptools import setup, find_packages


setup(
    name="botmanager",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "botmanager.create-project=botmanager.cli:create_project",
        ],
    },
)
