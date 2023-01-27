.PHONY: setup_venv

setup_venv:
	python3 -m venv .venv && . .venv/bin/activate \
	&& python3 -m pip install --upgrade pip \
	&& python3 -m pip install -r requirements.txt
