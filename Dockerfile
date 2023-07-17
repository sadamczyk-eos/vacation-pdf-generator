FROM python:3-alpine

WORKDIR /usr/src/app

COPY ./src/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

CMD [ "python", "./main.py" ]
