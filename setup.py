from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="color-harmony",
    version="1.0.0",
    description="A Python package to get color harmonies of a given image.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/profnote/ColorHarmony",
    author="Niti Wattanasirichaigoon",
    author_email="niti.wattanasirichaigoon@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ColorHarmony"],
    include_package_data=True,
    install_requires=["pillow", "scikit-learn", "matplotlib"],
    entry_points={
        "console_scripts": [
            "color-harmony=ColorHarmony.colorHarmony:main",
        ]
    },
)
