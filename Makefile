run_server:
	gunicorn --workers=4 --log-level debug -b 0.0.0.0:${PORT} app:app

run_tests:
	APP_SETTINGS=testing python3 -m unittest discover --buffer

docker_unittest:
	docker compose run basic_school_ml_project bash -c 'cd /app && APP_SETTINGS=testing python3 -m unittest discover --buffer'

docker_pylint:
	docker compose run basic_school_ml_project bash -c 'cd /app && pylint --fail-under=5 lib/*.py tests/*.py'
