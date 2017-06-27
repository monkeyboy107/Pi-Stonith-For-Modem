pip: virtualenv
	@source .venv/bin/activate; pip install .
virtualenv:
	@if ! ls .venv > /dev/null; then virtualenv .venv; fi
clean:
	@rm -rf .venv
