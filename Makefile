
DIRNAME=$(PWD)

template:
	$(DIRNAME)/bin/cookiecutter -v --no-input $(DIRNAME)

run: template
	cd project_name; sh docker/run.sh bash

rtest: template
	cd project_name; sh docker/run.sh tox

test:
	$(DIRNAME)/bin/cookiecutter -v --no-input $(DIRNAME)
	cd project_name; ../bin/tox
