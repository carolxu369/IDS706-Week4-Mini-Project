setup:
	python -m venv venv
	source venv/bin/activate
    	pip install -r requirements.txt

test:
    	python -m pytest -vv --cov=main test_*.py

lint:
    	pylint main.py

run:
	python main.py

clean:
    	rm -rf venv __pycache__
