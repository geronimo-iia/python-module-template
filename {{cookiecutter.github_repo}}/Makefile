# const
.DEFAULT_GOAL := install

# PROJECT DEPENDENCIES ########################################################

.PHONY: install
install: lock ## Install project dependencies
	@mkdir -p .cache
	uv venv
	uv pip install -r pyproject.toml


lock: pyproject.toml #codeartifact-index
	uv lock
	@touch $@


# PROJECT PUBLISH ########################################################

#.EXPORT_ALL_VARIABLES:
AWS_DOMAIN="<your-domain>"
AWS_ACCOUNT_ID="<your-account-id>"
AWS_REGION="<your-region>"
AWS_CODEARTIFACT_REPOSITORY="<your-repository>"
export AWS_CODEARTIFACT_TOKEN="$$(aws codeartifact get-authorization-token --domain $(AWS_DOMAIN) --domain-owner $(AWS_ACCOUNT_ID) --query authorizationToken --output text)"

codeartifact-index:
	echo 'export UV_EXTRA_INDEX_URL="https://aws:${AWS_CODEARTIFACT_TOKEN}@${AWS_DOMAIN}-${AWS_ACCOUNT_ID}.d.codeartifact.${AWS_REGION}.amazonaws.com/pypi/${AWS_CODEARTIFACT_REPOSITORY}/simple/"'


codeartifact-publish:
	UV_PUBLISH_URL="https://${AWS_DOMAIN}-${AWS_ACCOUNT_ID}.d.codeartifact.${AWS_REGION}.amazonaws.com/pypi/${AWS_CODEARTIFACT_REPOSITORY}/" \
	UV_PUBLISH_USERNAME=aws \
	UV_PUBLISH_PASSWORD="$(AWS_CODEARTIFACT_TOKEN)" \
	uv publish