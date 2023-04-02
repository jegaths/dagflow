import { atom } from "recoil";

export const selectedNodeState = atom({
    key: "selectedNodeState",
    default: undefined,
})

export const importStatementState = atom({
    key: "importStatementState",
    default: "from airflow import DAG\nfrom airflow.utils.dates import days_ago\nfrom datetime import timedelta",
})

export const pipelineState = atom({
    key: "pipelineState",
    // TODO:Have to remove this line after testing
    default: {
        "pipeline_name": "", "global": "def test():\r\n    print(\"It will be ok!\")", "operators": {}, "react_flow_data": {}, "dag_statement": "dag = DAG('dagflow_dag_id', default_args={'owner': 'Dagflow', 'depends_on_past': True, 'start_date': days_ago(1), 'email': ['dagflow@gmail.com'], 'email_on_failure': False, 'email_on_retry': False, 'retries': 3, 'retry_delay': timedelta(minutes=5)}, description='Dagflow dag description', schedule_interval='0 0 * * *')"
    },
    // TODO:Enable this line after testing
    // default: { "pipeline_name": "", "global": "", "operators": {}, "react_flow_data": {} },

    // TODO:Delete this line after testing
    // default: { "pipeline_name": "", "global": "", "operators": { "PythonOperator_1_0": { "name": "PythonOperator", "import_path": "airflow.operators.python", "args": { "python_callable": "", "op_args": "", "op_kwargs": "", "templates_dict": "", "templates_exts": "", "kwargs": "", "task_id": "PythonOperator_1_0" }, "description": "Description about this node." }, "PythonOperator_1_1": { "name": "PythonOperator", "import_path": "airflow.operators.python", "args": { "python_callable": "", "op_args": "", "op_kwargs": "", "templates_dict": "", "templates_exts": "", "kwargs": "", "task_id": "PythonOperator_1_1" }, "description": "Description about this node." } } },
})

export const nodeListState = atom({
    key: "nodeListState",
    default: [],
})

export const reactFlowState = atom({
    key: "reactFlowState",
    default: null
})

export const isDetailsPaneOpenState = atom({
    key: "isDetailsPaneOpenState",
    default: false
})

export const selectedTabState = atom({
    key: "selectedTabState",
    default: 0
})

