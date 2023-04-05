from pydantic import BaseModel

COLLECTION = "pipeline"


class Nodes(BaseModel):
    width: int
    height: int
    id: str
    type: str
    position: dict
    data: str
    selected: bool
    positionAbsolute: dict
    dragging: bool


class Edges(BaseModel):
    source: str
    sourceHandle: str
    target: str
    targetHandle: str
    animated: bool
    id: str


class Viewport(BaseModel):
    x: int
    y: int
    zoom: int


class ReactFlowData(BaseModel):
    nodes: list[Nodes]
    edges: list[Edges]
    viewport: Viewport

    class Config:
        schema_extra = {
            "example": {
                "nodes": [],
                "edges": [],
                "viewport": {"x": 0, "y": 0, "zoom": 1},
            }
        }


class DagStatement(BaseModel):
    dag_variable_name: str
    call: str

    class Config:
        schema_extra = {
            "example": {
                "dag_variable_name": "dag",
                "call": 'DAG(\n"my_dag_id",\ndefault_args={\n"owner": "Jegath S",\n"depends_on_past": True,\n"start_date": days_ago(1),\n"email": ["myemail.com"],\n"email_on_failure": False,\n"email_on_retry": False,\n"retries": 3,\n"retry_delay": timedelta(minutes=5),\n},\ndescription="Dagflow dag descroption",\nschedule_interval="0 0 * * *",\nconcurrency=10,\n)',
            }
        }


class Operators(BaseModel):
    name: str
    import_path: str
    args: dict
    description: str


class PipelineData(BaseModel):
    pipeline_name: str
    global_statements: str
    operators: dict[str, Operators]
    react_flow_data: ReactFlowData
    import_statements: str
    dag_statement: DagStatement

    class Config:
        schema_extra = {
            "example": {
                "pipeline_name": "pipeline_name",
                "global_statements": "def test()\n print('test')",
                "operators": {},
                "react_flow_data": {},
                "import_statements": "from airflow import DAG",
                "dag_statement": {
                    "dag_variable_name": "dag",
                    "call": 'DAG(\n"my_dag_id",\ndefault_args={\n"owner": "Jegath S",\n"depends_on_past": True,\n"start_date": days_ago(1),\n"email": ["myemail.com"],\n"email_on_failure": False,\n"email_on_retry": False,\n"retries": 3,\n"retry_delay": timedelta(minutes=5),\n},\ndescription="Dagflow dag descroption",\nschedule_interval="0 0 * * *",\nconcurrency=10,\n)',
                },
            }
        }


class Pipeline(BaseModel):
    data: PipelineData
