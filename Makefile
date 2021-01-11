SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.github_repo}}/* {{cookiecutter.github_repo}}/*/*
GENERATED_PROJECT := my-project

# MAIN #########################################################################

.PHONY: ci
ci: build ## CI Build: Test Sample
	make install -C $(GENERATED_PROJECT)
	make test -C $(GENERATED_PROJECT)
	make check -C $(GENERATED_PROJECT)

# DEPENDENCIES #################################################################

install: .install ## Install project

.install: poetry.lock
	poetry install
	@touch $@

poetry.lock: pyproject.toml
	poetry lock

# BUILD ########################################################################

.PHONY: build
build: clean install $(GENERATED_PROJECT) ## Generate Sample
$(GENERATED_PROJECT): $(SOURCE_FILES)
	@cat cookiecutter.json
	@poetry run cookiecutter . --no-input --overwrite-if-exists
	@mkdir -p $(GENERATED_PROJECT)
	@touch $(GENERATED_PROJECT)

# GENERATE ######################################################################

.PHONY: generate
generate: clean install
	poetry run cookiecutter .

# CLEANUP ######################################################################

.PHONY: clean
clean: ## Delete all generated and temporary files
	rm -rf $(GENERATED_PROJECT)

# HELP ########################################################################

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
