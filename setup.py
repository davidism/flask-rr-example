from setuptools import find_packages
from setuptools import setup

setup(
    name="Flask-RR",
    version="0.1.0",
    license="BSD",
    author="David Lord",
    author_email="davidism@gmail.com",
    description="Flask that passes request and response objects to views.",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["Flask"],
    extras_require={"dev": ["Flask-Shell-IPython", "python-dotenv", "watchdog"]},
)
