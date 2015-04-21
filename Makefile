
DIRNAME=$(PWD)

template:
	$(DIRNAME)/bin/cookiecutter -v --no-input $(DIRNAME)

run: template
	cd project_name; docker-compose run web

rtest: template
	cd project_name; docker-compose run web tox

test:
	$(DIRNAME)/bin/cookiecutter -v --no-input $(DIRNAME)
	cd project_name; ../bin/tox
