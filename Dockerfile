FROM python:3.8

COPY . /app

WORKDIR /app

run pip install -r requirements.txt

cmd ["pip" "install" "git+https://github.com/SebGr/fml-wright.git"]

EXPOSE 5000

cmd ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "generator.app:app"]