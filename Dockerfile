FROM python:3.9-slim

WORKDIR /pypi-data
COPY . /pypi-data
RUN python -m pip install -r requirements.txt
CMD python main.py
