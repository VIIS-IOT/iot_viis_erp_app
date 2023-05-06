from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in iot_viis/__init__.py
from iot_viis import __version__ as version

setup(
	name="iot_viis",
	version=version,
	description="IoT Viis",
	author="Pyroject",
	author_email="phuongtung0801@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
