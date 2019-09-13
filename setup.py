from setuptools import setup

setup(
    name="rgng",
    version="0.0.1",
    author="enriqueav",
    author_email="",
    description="Python port of the name generator",
    long_description="Python port of the name generator",
    py_modules=["rgng"],
    long_description_content_type="text/markdown",
    url="https://github.com/gpenverne/random-game-name-generator",
    packages=['rgng'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
