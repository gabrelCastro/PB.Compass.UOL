FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip 
    
RUN pip install pandas boto3 dotenv

COPY . .

CMD ["python", "etapa1.py"]