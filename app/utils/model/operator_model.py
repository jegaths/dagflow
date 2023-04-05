from pydantic import BaseModel
from typing import Optional


# "args": {
#     "python_callable": {
#       "default_argument": "",
#       "data_type": "",
#       "required": true
#     },
# }


class Args(BaseModel):
    name: str
    default_argument: str = ""
    data_type: str = ""
    required: bool = False


class Operator(BaseModel):
    id: int
    name: str
    path: str
    node_type: str = "operator"
    args: list[Args] = [Args(name="task_id", default_argument="", data_type="string", required=True)]
