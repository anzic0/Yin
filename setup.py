from setuptools import setup


setup(
    name="Yin",
    version='0.3',
    description="Fast Python implementation of the Yin algorithm: a fundamental frequency estimator",
    author=["Patrice Guyot"],
    pymodules=["gcmi"],
    install_requires=['numpy', 'scipy', 'matplotlib'],
)

