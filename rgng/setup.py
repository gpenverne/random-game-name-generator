import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rgng",
    version="0.0.1",
    author="enriqueav",
    author_email="",
    description="Python port of the name generator",
    long_description=long_description,
    py_modules=["rgng"],
    long_description_content_type="text/markdown",
    url="https://github.com/gpenverne/random-game-name-generator",
    packages=setuptools.find_packages(include=['rgng', 'rgng.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
