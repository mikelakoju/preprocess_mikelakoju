import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name = 'preprocess_mikelakoju', #Remember this name must be unique globally
    version = '0.0.3',
    author_email = 'lakojum@yahoo.com',
    description = 'This is a preprocessing package for NLP',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Aproved :: MIT License',
        'Operating System :: OS :: Independent'
    ],
    python_requires = '>=3.5'
)