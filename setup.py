import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="rp3_dcache",
        version="0.3",
        author="Thomas Duigou",
        author_email="thomas.duigou@inra.fr",
        description="Cache to dope the result retrieval from reaction rules, to be used with RetroPath 3.0",
	long_description=long_description,
    	long_description_content_type="text/markdown",
	url="https://github.com/brsynth/rp3_dcache",
        packages=setuptools.find_packages(),
	python_requires='>=3.6',
	include_package_data=True
)
