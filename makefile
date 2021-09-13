default:
	stuff_env/Scripts/activate.ps1
	make setup_dev
	make tox

setup_dev:
	pip install -e .
	pip install -r requirements_dev.txt

setup_user:
	pip install -e .
	pip install -r requirements.txt

run_tests:
	mypy src
	flake8 src
	pytest

run_tox:
	tox
