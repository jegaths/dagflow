ARG CUSTOM_PYTHON_VERSION
ARG AIRFLOW_VERSION

FROM python:${CUSTOM_PYTHON_VERSION}
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade -r /app/requirements.txt


RUN echo "AIRFLOW_VERSION=${AIRFLOW_VERSION}"
RUN echo "CUSTOM_PYTHON_VERSION=${CUSTOM_PYTHON_VERSION}"

# RUN pip install "apache-airflow[postgres,google]==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${CUSTOM_PYTHON_VERSION}.txt"
# RUN pip install plyvel

COPY . /app

EXPOSE 8000

# CMD ["ls"]

# 
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]