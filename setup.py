import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magic8ball",
    version="1.1.1",
    author="Cyrus Yip",
    author_email="cyruscmyip1@gmail.com",
    description="Magic 8 ball answers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/realcyguy/magic8ball",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)