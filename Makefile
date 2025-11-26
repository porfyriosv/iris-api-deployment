.PHONY: run docker-build docker-run

run:
	uvicorn app:app --reload --port 8000

docker-build:
	docker build -t iris-api .

docker-run:
	docker run -p 8000:8000 iris-api