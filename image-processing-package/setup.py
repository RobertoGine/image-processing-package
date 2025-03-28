from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_desciption = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="image_processing",
    version="0.0.1",
    description="image_processing_package",
    long_description=page_desciption,
    long_description_content_type="text/markdown",
    url="https://github.com/username/package_name",
    author="Roberto",
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6",
)