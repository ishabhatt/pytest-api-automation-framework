FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["pytest"]