from setuptools import setup, find_packages

setup(
    name="txt2html",
    version="0.9.0",  # Start with a suitable version number
    packages=find_packages(),
    entry_points={"console_scripts": ["txt2html=txt2html.main:main"]},
    author="Mingming Ma",
    license="MIT",
)
