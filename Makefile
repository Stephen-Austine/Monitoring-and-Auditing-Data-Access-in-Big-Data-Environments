.PHONY: install test run

install:
	python3 -m pip install -r requirements.txt

test:
	python3 -m unittest discover -s tests -v

run:
	python3 "Monitoring and Auditing Data Access (Big Data)/Anomaly_detection.py"
