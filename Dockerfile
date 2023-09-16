FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --upgrade pip
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "run.py"]
