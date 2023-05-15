from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
dag = DAG('python_op_test', default_args={'owner': 'Jegath S', 'depends_on_past': True, 'start_date': days_ago(1), 'email': ['myemail.com'], 'email_on_failure': False, 'email_on_retry': False, 'retries': 3, 'retry_delay': timedelta(minutes=5)}, description='Dagflow dag descroption', schedule_interval='0 0 * * *', concurrency=10)

def test(string):
    print(string)
test1 = PythonOperator(task_id='test1', python_callable=test, op_kwargs={'string': 'first task'}, show_return_value_in_logs=True, dag=dag)
test2 = PythonOperator(task_id='test2', python_callable=test, show_return_value_in_logs=True, dag=dag)
test1 >> test2