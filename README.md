# Stuff - A GitHub actions automatic testing project
This program does nothing useful, but is very well tested. :)

It is build and automaticlaly tested based on:

* VENV: [Python Tutorial: VENV (Windows) - How to Use Virtual Environments with the Built-In venv Module](https://youtu.be/APOPm01BVrk) by Corey Schafeer.
* Everything else: [Automated Testing in Python with pytest, tox, and GitHub Actions](https://youtu.be/DhUpxWjOhME) by mCoding.


## Setup and usage
Create venv:

* `python -m venv stuff_env`

Launch venv by using one of he following commands:

* `stuff_env/Scripts/activate.bat`
* `stuff_env/Scripts/Activate.ps1`

Using PowerShell (`Activate.ps1`) you can also deactivate using by simply:

* `deactivate`

Install project as a package:

* `pip install -e .`

Install requirements (remove `_dev` for normal requirements):

* `pip install -r requirements_dev.txt`

Run simple tests in venv:

* `mypy src`
* `flake8 src`
* `pytest`

Run tests in multiple environments:

* `tox`

Test results from tox-gh-actions:

![Tests](https://github.com/catsymptote/automated_test_on_github_test/actions/workflows/tests.yml/badge.svg)
