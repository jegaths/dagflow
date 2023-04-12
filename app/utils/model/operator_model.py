from pydantic import BaseModel


class Args(BaseModel):
    default_argument: str = ""
    data_type: str = ""
    required: bool = False


class Operator(BaseModel):
    id: int
    name: str
    import_path: str
    node_type: str = "operator"
    args: dict[str, Args] = {"task_id": Args(default_argument="", data_type="string", required=True)}
