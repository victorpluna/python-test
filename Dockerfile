FROM python:3.6
ENV PYTHON_UNBUFFERED=1

RUN mkdir /code
WORKDIR /code

CMD apt-get update && apt-get install -y python-pip python-dev libpq-dev

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

CMD [ "python", "./main.py", "--level", "1" ]