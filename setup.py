import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author_email="author@example.com",
    descriptions="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programing Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operator System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(wwhere="src"),
    python_requires=">=3.6",
)