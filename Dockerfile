FROM python:3.8

COPY . /app

WORKDIR /app

COPY /home/sebastiaan/Projects/fml-wright-project/api_models/models/bicyclegan/complete_floorplan/ ./models

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    libspatialindex-dev

RUN pip install git+https://github.com/SebGr/fml-wright.git

EXPOSE 5000

cmd ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "generator.app:app"]