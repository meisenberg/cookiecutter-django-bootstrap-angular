
DIRNAME=$(PWD)

template:
	$(DIRNAME)/bin/cookiecutter -v --no-input $(DIRNAME)

test:
	$(DIRNAME)/bin/cookiecutter -v --no-input $(DIRNAME)
	cd project_name; ../bin/tox
