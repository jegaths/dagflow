import { atom } from "recoil";

export const selectedNodeState = atom({
    key: "selectedNodeState",
    default: undefined,
})

export const pipelineState = atom({
    key: "pipelineState",
    // TODO:Have to remove this line after testing
    default: {
        "pipeline_name": "", "global": "def test():\r\n    print(\"It will be ok!\")", "operators": {}, "react_flow_data": {}
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

