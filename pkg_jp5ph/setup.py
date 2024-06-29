#setup.py

from setuptools import setup, find_packages

setup(
    name='pkg_jp5ph',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your package dependencies here
    ],
    extras_require={
        'dev': [
            'pytest',
            # other development dependencies
        ],
    },
    author='jd_pinto',
    author_email='jp5ph@virginia.edu',
    description='word processors',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jdpman/jp5ph_DS5111su24_lab_01.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
