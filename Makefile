
run: install-deps
	mkdocs serve --livereload

install-deps:
	pip install -r requirements.txt

deploy:
	mkdocs gh-deploy
