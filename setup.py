from setuptools import setup

setup(
    name="file-protector",
    version="1.0.0",
    license='BSD-3',
    description="A Python File Protector",
    author='Krisna Pranav',
    author_email='krisna.pranav@gmail.com',
    url='https://github.com/krishpranav/file-protector',
    packages=['file-protector'],
    package_data={
        'file-protector': ['LICENSE']
    },
    install_requires=['future'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System',
    ],
)