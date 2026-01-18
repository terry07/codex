.PHONY: source docs tests

source:
	@illiterate -d . docs/*.md
	@make tests

tests:
	pytest
