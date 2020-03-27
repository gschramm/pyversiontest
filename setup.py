import setuptools

setuptools.setup(
    name="pyversiontest",
    use_scm_version={'fallback_version':'unknown'},
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    author="Georg Schramm",
    author_email="georg.schramm@kuleuven.be",
    description="test to include version from git archive",
    license='MIT',
    url="https://github.com/gschramm/pymversiontest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: LGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy>=1.15']
)
