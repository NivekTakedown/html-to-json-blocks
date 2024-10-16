from setuptools import setup, find_packages
from pathlib import Path

# Leer el contenido del README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='html-to-json-blocks',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'beautifulsoup4>=4.9.3',
        'beautifulsoup4==4.9.3',
        'pytest==6.2.5',
        'pytest-cov==2.12.1',
    ],
    extras_require={
        'dev': [
            'pytest>=6.2.3',
            'pytest-cov>=2.11.1',
        ],
    },
    entry_points={
        'console_scripts': [
            'html2json=html_to_json_blocks.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A library to convert HTML to JSON blocks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/html-to-json-blocks',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    license='MIT',
    keywords='html json converter',
)
