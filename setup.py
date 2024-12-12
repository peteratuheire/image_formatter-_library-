from setuptools import setup, find_packages

setup(
    name="image-formatter",
    version="0.1.0",
    description="A simple cross-platform library for basic image formatting.",
    author="Your Name",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=[
        "pillow"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
