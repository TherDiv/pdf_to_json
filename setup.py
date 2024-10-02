from setuptools import setup, find_packages

setup(
    name='pdf_to_json',  # Nombre del paquete
    version='0.1.0',
    packages=find_packages(),  # Encuentra todas las subcarpetas con archivos __init__.py
    install_requires=[
        'boto3',  # Dependencia para AWS S3 y Textract
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library for converting PDF documents to JSON using AWS Textract',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pdf_to_json',  # Cambia la URL a tu repositorio si lo tienes
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
