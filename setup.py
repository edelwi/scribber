import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scribber",
    version="v0.0.3",
    author="Evgeniy Semenov",
    author_email="edelwi@yandex.ru",
    description="A simple document generator with not very rich functionality that can export a document to "
                "some formats such as text, docx, xlsx and markdown.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edelwi/scribber",
    packages=setuptools.find_packages(),
    # entry_points={},
    install_requires=[
        'lxml>=4.6.0,<5.0.0',
        'pydantic>=1.8.0,<2.0.0',
        'python-docx>=0.8.0,<1.0.0',
        'typing_extensions>=4.0.0,<5.0.0'
        'XlsxWriter>=3.0.0,<4.0.0'
        ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)