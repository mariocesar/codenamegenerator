
default:
	pip install -e .
	pip install wheel
	pip install twine

release: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -fr *.egg-info
	rm -fr dist/
	rm -fr build/
