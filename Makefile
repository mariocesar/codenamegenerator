
default:
	pip install -e .
	pip install twine

release:
	python setup.py sdist bdist_wheel
	twine upload dist/*
