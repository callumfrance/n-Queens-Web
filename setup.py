from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='n_queens',
        version='1.0.0',
        author="Callum",
        description="Randomly places queens on a chess board",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/callumfrance/n_queens_web",
        packages=find_packages(),
        include_package_date=True,
        zip_safe=False,
        install_requires=[
            'flask',
            ],
        python_requires=">=3.6",
        )
