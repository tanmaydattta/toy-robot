directory = venv

force_venv: | $(directory)
	@echo "will run no matter what"
	rm -rf ./venv
	virtualenv -p python3 $(directory)
	source ./$(directory)/bin/activate; \
	pip install -r requirements.txt; \

$(directory): 
	virtualenv -p python3 $(directory)
	source ./$(directory)/bin/activate; \
	pip install -r requirements.txt; \

test_all:
	@echo
	@echo
	@echo "************************** Testing Table class *******************"
	python -m unittest tests/test_Table.py

	@echo
	@echo
	@echo "************************** Testing Robot class *******************"
	python -m unittest tests/test_Robot.py

run_default:
	@echo
	@echo "Running Robot with input.txt file"
	@echo
	@python run.py < input.txt

.PHONY: force_setup, test_all