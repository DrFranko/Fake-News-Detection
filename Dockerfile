FROM python:3.9-slim

WORKDIR /FAKENEWS

COPY . /FAKENEWS

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

CMD ["python", "app.py"]
