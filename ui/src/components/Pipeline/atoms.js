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
    default: {
        "pipeline_name": "", "global_statements": "", "operators": {}, "react_flow_data": {}, "dag_statement": {}
    },
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


export const intialEdgesState = atom({
    key: "intialEdgesState",
    default: []
})

export const initialNodesState = atom({
    key: "initialNodesState",
    default: []
})

export const formRefState = atom({
    key: "formRefState",
    default: null
})