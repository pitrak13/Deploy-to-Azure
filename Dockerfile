FROM python:3.11.8-alpine3.19

EXPOSE 7999

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY ping-pong.py /app

ENTRYPOINT ["python3"]

CMD ["ping-pong.py"]
