# 
FROM python:3.11.2

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./app /app

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# docker run --name dagflow-api -p 8000:8000 -d -v $(pwd)/app:/app dagflow-api-image
# docker rm -f dagflow-api
# docker build -t dagflow-api-image .
#docker logs dagflow-api