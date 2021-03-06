from setuptools import setup, find_packages
from pip.req import parse_requirements

VERSION = '1.0.0'

INSTALL_REQUIRES = [
    str(r.req) for r in parse_requirements('requirements.txt', session=False)
]

setup(
    name="judge-pics",
    description="Database of Judge Pictures",
    version=VERSION,
    author="Mike Lissner",
    author_email="info@free.law",
    maintainer="Mike Lisser",
    maintainer_email="info@free.law",
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    package_data={
        'judge_pics': [
            'data/128/*',
            'data/256/*',
            'data/512/*',
            'data/orig/*',
            'data/judges.json',
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="tests",
    install_requires=INSTALL_REQUIRES,
)
