flake:
	@if command -v flake8 > /dev/null; then \
		echo "Running flake8"; \
		flake8 --count mne examples tutorials; \
	else \
		echo "flake8 not found, please install it!"; \
		exit 1; \
	fi;
	@echo "flake8 passed"
