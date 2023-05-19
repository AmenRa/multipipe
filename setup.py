import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multipipe",
    version="0.1.0",
    author="Elias Bassani",
    author_email="elias.bssn@gmail.com",
    description="A Python utility for multiprocessing pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmenRa/unified-io",
    packages=setuptools.find_packages(),
    install_requires=["multiprocess"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: General",
    ],
    keywords=["pipeline", "multiprocessing", "multithreading", "utils", "utilities"],
    python_requires=">=3.7",
)
