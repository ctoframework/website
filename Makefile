
run: install-deps
	mkdocs serve

install-deps:
	pip install -r requirements.txt

deploy:
	mkdocs gh-deploy
