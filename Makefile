
default:
	pip install -e .
	pip install wheel
	pip install twine

release: clean
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	rm -r *.egg-info
	rm -r dist/
	rm -r build/
