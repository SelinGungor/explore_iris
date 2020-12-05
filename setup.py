from setuptools import setup, find_namespace_packages

VERSION = {}

with open("src/explore/__init__.py") as fp:
    exec(fp.read(), VERSION)

setup(
    name="explore-iris",
    author="Selin Gungor",
    author_email="selingungor01@gmail.com",
    description="""Simple Iris dataset exploration""",
    version=VERSION.get("__version__", None),
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "click>=7.1,<8.0",
        "wheel>=0.34,<1.0",
        "setuptools>=45.0"
    ],
    entry_points={"console_scripts": ["explore=exlplore.__main__:main"]},
)
