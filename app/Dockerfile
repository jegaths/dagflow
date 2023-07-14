ARG CUSTOM_PYTHON_VERSION=3.10
FROM python:${CUSTOM_PYTHON_VERSION}

ARG AIRFLOW_VERSION=2.5.3
ARG PYTHON_VERSION=3.10
RUN echo ${AIRFLOW_VERSION} ${PYTHON_VERSION}
RUN echo "$(echo $PYTHON_VERSION | cut -d '.' -f 1,2)" > version.txt

RUN VERSION_MAJOR_MINOR=$(cat version.txt) \
    && pip install "apache-airflow[postgres,google]==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-$VERSION_MAJOR_MINOR.txt"

RUN pip install plyvel

WORKDIR /app

RUN pip install pyroscope-io

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt


COPY . /app

EXPOSE 8000

# CMD ["ls"]

# 
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]