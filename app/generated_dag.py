from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta
dag = DAG('my_dag_id', default_args={'owner': 'Jegath S', 'depends_on_past': True, 'start_date': days_ago(1), 'email': ['myemail.com'], 'email_on_failure': False, 'email_on_retry': False, 'retries': 3, 'retry_delay': timedelta(minutes=5)}, description='Generate datalake from CDR mutations', schedule_interval='0 0 * * *', concurrency=10, tags=['hashing'])

def test():
    a = 10
    print(a)
    print('I think this is working fine')