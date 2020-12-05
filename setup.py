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
    entry_points={"console_scripts": ["explore=explore.__main__:main"]},
)
