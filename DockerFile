FROM python:3.11-slim
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && pip install -r requirements.txt

# 7 Run the application
CMD ["python","app.py"]