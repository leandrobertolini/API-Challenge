SHELL=/bin/bash

default: test

help:
	@echo "test - run tests quickly with the default Python"
	@echo "release - package and upload a release"

test:
	python spotippos/manage.py test spotippos/properties/tests

test-coverage:
	python spotippos/manage.py test spotippos/properties/tests --with-coverage --cover-package=properties

migrations:
	python spotippos/manage.py migrate

run:
	python spotippos/manage.py runserver		
	
clean:
	@find . -iname '*.pyc' -delete -o -iname '*.pyo' -delete
	@find . -name '__pycache__' -prune | xargs rm -rf # clean __pycache__ dirs build by py.test