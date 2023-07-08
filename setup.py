from setuptools import setup, find_packages

version = __import__("background_task").__version__

classifiers = [c for c in open("classifiers").read().splitlines() if "#" not in c]

setup(
    name="django-background-tasks",
    version=version,
    description="Database backed asynchronous task queue",
    long_description=open("README.rst").read(),
    author="QueraTeam, arteria GmbH, John Montgomery",
    author_email="contact@quera.org",
    url="https://github.com/QueraTeam/django-background-tasks",
    license="BSD",
    packages=find_packages(exclude=["ez_setup"]),
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    zip_safe=True,
    classifiers=classifiers,
)
