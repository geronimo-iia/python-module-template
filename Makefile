SOURCE_FILES = Makefile cookiecutter.json {{cookiecutter.github_repo}}/* {{cookiecutter.github_repo}}/*/*
GENERATED_PROJECT := my-project

# MAIN #########################################################################

.PHONY: ci
ci: build ## CI Build: Test Sample
	make install -C $(GENERATED_PROJECT)
	cd $(GENERATED_PROJECT) && uv run poe test
	cd $(GENERATED_PROJECT) && uv run poe check

# DEPENDENCIES #################################################################


.PHONY: install
install: lock ## Install project dependencies
	@mkdir -p .cache
	uv venv
	uv pip install -r pyproject.toml

.PHONY: lock
lock: pyproject.toml
	uv lock



# BUILD ########################################################################

.PHONY: build
build: clean install $(GENERATED_PROJECT) ## Generate Sample
$(GENERATED_PROJECT): $(SOURCE_FILES)
	@cat cookiecutter.json
	@uv run cookiecutter . --no-input --overwrite-if-exists
	@mkdir -p $(GENERATED_PROJECT)
	@touch $(GENERATED_PROJECT)

# GENERATE ######################################################################

.PHONY: generate
generate: clean install
	uv run cookiecutter .

# CLEANUP ######################################################################

.PHONY: clean
clean: ## Delete all generated and temporary files
	@rm -rf $(GENERATED_PROJECT)


