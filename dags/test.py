from airflow import DAG
from pathlib import Path
from airflow.utils.dates import days_ago
from datetime import timedelta

from airflow.models import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
import os

this_is_a_global_variable = 10

def test_function():
    print("This is a test function")

this_is_a_global_variable += 1

class GvPostgresOperator(BaseOperator):
    template_fields = ("sql",)
    template_ext = (".sql",)
    ui_color = "#944dff"  # cool purple

    def __init__(self, sql: str, postgres_conn_id: str, mode: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.sql = sql
        self.postgres_conn_id = postgres_conn_id
        self.mode = mode

    def push(self, context, records):
        context['ti'].xcom_push(key="rows", value=records)

    def execute(self, context):
        postgres_hook = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        test_function()
        if (self.mode == "read"):
            records = postgres_hook.get_records(sql=self.sql)
            self.push(context, records)

dag_id = Path(__file__).stem

dag = DAG(
    dag_id,
    default_args={
        'owner': 'Jegath S',
        'depends_on_past': True,
        'start_date': days_ago(1),
        'email': ['jegath.suresh@grandvision.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
    },
    description='''
        Generate datalake from CDR mutations
    ''',
    schedule_interval='0 0 * * *',
    concurrency=10,
    tags=["hashing"]
)
get_entities = GvPostgresOperator(
    dag=dag,
    postgres_conn_id="postges_developer_hub_dev",
    task_id="get_entities",
    sql="SELECT entity_name,is_enabled FROM entities",
    mode="read"
)

python_task = PythonOperator(
    dag=dag,
    python_callable=test_function,
    task_id="python_test_op",
)

get_entities >> python_task