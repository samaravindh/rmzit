from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_rmzit/__init__.py
from frappe_rmzit import __version__ as version

setup(
	name="frappe_rmzit",
	version=version,
	description="rmz oilfield engineering pte",
	author="aravindh sekar",
	author_email="aravindh.sekar@rmzoilfield.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
