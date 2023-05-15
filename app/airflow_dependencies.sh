AIRFLOW_VERSION=2.5.3
PYTHON_VERSION=3.10
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
pip install plyvel
# pip install 'apache-airflow[postgres,google]==2.5.3' \
#  --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.1.4/constraints-3.9.txt"