FROM python:latest

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "./app.py"]