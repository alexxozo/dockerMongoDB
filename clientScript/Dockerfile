FROM python:3
MAINTAINER Docker

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY script.py ./

CMD ["python", "./script.py"]