# Dagflow

A UI for creating and managing airflow dags.

### How to run ?

```docker
#Build the image
docker build -t dagflow-api-image .

#Run the image
docker run --name dagflow-api -p 8000:8000 -d -v $(pwd)/app:/app -v /mnt/c/Users/Jegath/Documents/Work/Grandvision/docker-airflow-2.1.4/dags:/dags dagflow-api-image

#To see logs
docker logs dagflow-api
```

# docker build -t dagflow-api-image .
#docker logs dagflow-api


<details>
<summary><b>Sample AST JSON for test.py</b></summary>
 
```json
 {
    "_type": "Module",
    "body": [
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 23,
            "end_lineno": 1,
            "level": 0,
            "lineno": 1,
            "module": "airflow",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 20,
                    "end_col_offset": 23,
                    "end_lineno": 1,
                    "lineno": 1,
                    "name": "DAG"
                }
            ]
        },
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 24,
            "end_lineno": 2,
            "level": 0,
            "lineno": 2,
            "module": "pathlib",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 20,
                    "end_col_offset": 24,
                    "end_lineno": 2,
                    "lineno": 2,
                    "name": "Path"
                }
            ]
        },
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 40,
            "end_lineno": 3,
            "level": 0,
            "lineno": 3,
            "module": "airflow.utils.dates",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 32,
                    "end_col_offset": 40,
                    "end_lineno": 3,
                    "lineno": 3,
                    "name": "days_ago"
                }
            ]
        },
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 30,
            "end_lineno": 4,
            "level": 0,
            "lineno": 4,
            "module": "datetime",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 21,
                    "end_col_offset": 30,
                    "end_lineno": 4,
                    "lineno": 4,
                    "name": "timedelta"
                }
            ]
        },
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 39,
            "end_lineno": 6,
            "level": 0,
            "lineno": 6,
            "module": "airflow.models",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 27,
                    "end_col_offset": 39,
                    "end_lineno": 6,
                    "lineno": 6,
                    "name": "BaseOperator"
                }
            ]
        },
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 66,
            "end_lineno": 7,
            "level": 0,
            "lineno": 7,
            "module": "airflow.providers.postgres.hooks.postgres",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 54,
                    "end_col_offset": 66,
                    "end_lineno": 7,
                    "lineno": 7,
                    "name": "PostgresHook"
                }
            ]
        },
        {
            "_type": "ImportFrom",
            "col_offset": 0,
            "end_col_offset": 51,
            "end_lineno": 8,
            "level": 0,
            "lineno": 8,
            "module": "airflow.operators.python",
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 37,
                    "end_col_offset": 51,
                    "end_lineno": 8,
                    "lineno": 8,
                    "name": "PythonOperator"
                }
            ]
        },
        {
            "_type": "Import",
            "col_offset": 0,
            "end_col_offset": 9,
            "end_lineno": 9,
            "lineno": 9,
            "names": [
                {
                    "_type": "alias",
                    "asname": null,
                    "col_offset": 7,
                    "end_col_offset": 9,
                    "end_lineno": 9,
                    "lineno": 9,
                    "name": "os"
                }
            ]
        },
        {
            "_type": "Assign",
            "col_offset": 0,
            "end_col_offset": 30,
            "end_lineno": 11,
            "lineno": 11,
            "targets": [
                {
                    "_type": "Name",
                    "col_offset": 0,
                    "ctx": {
                        "_type": "Store"
                    },
                    "end_col_offset": 25,
                    "end_lineno": 11,
                    "id": "this_is_a_global_variable",
                    "lineno": 11
                }
            ],
            "type_comment": null,
            "value": {
                "_type": "Constant",
                "col_offset": 28,
                "end_col_offset": 30,
                "end_lineno": 11,
                "kind": null,
                "lineno": 11,
                "n": 10,
                "s": 10,
                "value": 10
            }
        },
        {
            "_type": "FunctionDef",
            "args": {
                "_type": "arguments",
                "args": [],
                "defaults": [],
                "kw_defaults": [],
                "kwarg": null,
                "kwonlyargs": [],
                "posonlyargs": [],
                "vararg": null
            },
            "body": [
                {
                    "_type": "Expr",
                    "col_offset": 4,
                    "end_col_offset": 36,
                    "end_lineno": 14,
                    "lineno": 14,
                    "value": {
                        "_type": "Call",
                        "args": [
                            {
                                "_type": "Constant",
                                "col_offset": 10,
                                "end_col_offset": 35,
                                "end_lineno": 14,
                                "kind": null,
                                "lineno": 14,
                                "n": "This is a test function",
                                "s": "This is a test function",
                                "value": "This is a test function"
                            }
                        ],
                        "col_offset": 4,
                        "end_col_offset": 36,
                        "end_lineno": 14,
                        "func": {
                            "_type": "Name",
                            "col_offset": 4,
                            "ctx": {
                                "_type": "Load"
                            },
                            "end_col_offset": 9,
                            "end_lineno": 14,
                            "id": "print",
                            "lineno": 14
                        },
                        "keywords": [],
                        "lineno": 14
                    }
                }
            ],
            "col_offset": 0,
            "decorator_list": [],
            "end_col_offset": 36,
            "end_lineno": 14,
            "lineno": 13,
            "name": "test_function",
            "returns": null,
            "type_comment": null
        },
        {
            "_type": "AugAssign",
            "col_offset": 0,
            "end_col_offset": 30,
            "end_lineno": 16,
            "lineno": 16,
            "op": {
                "_type": "Add"
            },
            "target": {
                "_type": "Name",
                "col_offset": 0,
                "ctx": {
                    "_type": "Store"
                },
                "end_col_offset": 25,
                "end_lineno": 16,
                "id": "this_is_a_global_variable",
                "lineno": 16
            },
            "value": {
                "_type": "Constant",
                "col_offset": 29,
                "end_col_offset": 30,
                "end_lineno": 16,
                "kind": null,
                "lineno": 16,
                "n": 1,
                "s": 1,
                "value": 1
            }
        },
        {
            "_type": "ClassDef",
            "bases": [
                {
                    "_type": "Name",
                    "col_offset": 25,
                    "ctx": {
                        "_type": "Load"
                    },
                    "end_col_offset": 37,
                    "end_lineno": 18,
                    "id": "BaseOperator",
                    "lineno": 18
                }
            ],
            "body": [
                {
                    "_type": "Assign",
                    "col_offset": 4,
                    "end_col_offset": 30,
                    "end_lineno": 19,
                    "lineno": 19,
                    "targets": [
                        {
                            "_type": "Name",
                            "col_offset": 4,
                            "ctx": {
                                "_type": "Store"
                            },
                            "end_col_offset": 19,
                            "end_lineno": 19,
                            "id": "template_fields",
                            "lineno": 19
                        }
                    ],
                    "type_comment": null,
                    "value": {
                        "_type": "Tuple",
                        "col_offset": 22,
                        "ctx": {
                            "_type": "Load"
                        },
                        "dims": [
                            {
                                "_type": "Constant",
                                "col_offset": 23,
                                "end_col_offset": 28,
                                "end_lineno": 19,
                                "kind": null,
                                "lineno": 19,
                                "n": "sql",
                                "s": "sql",
                                "value": "sql"
                            }
                        ],
                        "elts": [
                            {
                                "_type": "Constant",
                                "col_offset": 23,
                                "end_col_offset": 28,
                                "end_lineno": 19,
                                "kind": null,
                                "lineno": 19,
                                "n": "sql",
                                "s": "sql",
                                "value": "sql"
                            }
                        ],
                        "end_col_offset": 30,
                        "end_lineno": 19,
                        "lineno": 19
                    }
                },
                {
                    "_type": "Assign",
                    "col_offset": 4,
                    "end_col_offset": 28,
                    "end_lineno": 20,
                    "lineno": 20,
                    "targets": [
                        {
                            "_type": "Name",
                            "col_offset": 4,
                            "ctx": {
                                "_type": "Store"
                            },
                            "end_col_offset": 16,
                            "end_lineno": 20,
                            "id": "template_ext",
                            "lineno": 20
                        }
                    ],
                    "type_comment": null,
                    "value": {
                        "_type": "Tuple",
                        "col_offset": 19,
                        "ctx": {
                            "_type": "Load"
                        },
                        "dims": [
                            {
                                "_type": "Constant",
                                "col_offset": 20,
                                "end_col_offset": 26,
                                "end_lineno": 20,
                                "kind": null,
                                "lineno": 20,
                                "n": ".sql",
                                "s": ".sql",
                                "value": ".sql"
                            }
                        ],
                        "elts": [
                            {
                                "_type": "Constant",
                                "col_offset": 20,
                                "end_col_offset": 26,
                                "end_lineno": 20,
                                "kind": null,
                                "lineno": 20,
                                "n": ".sql",
                                "s": ".sql",
                                "value": ".sql"
                            }
                        ],
                        "end_col_offset": 28,
                        "end_lineno": 20,
                        "lineno": 20
                    }
                },
                {
                    "_type": "Assign",
                    "col_offset": 4,
                    "end_col_offset": 24,
                    "end_lineno": 21,
                    "lineno": 21,
                    "targets": [
                        {
                            "_type": "Name",
                            "col_offset": 4,
                            "ctx": {
                                "_type": "Store"
                            },
                            "end_col_offset": 12,
                            "end_lineno": 21,
                            "id": "ui_color",
                            "lineno": 21
                        }
                    ],
                    "type_comment": null,
                    "value": {
                        "_type": "Constant",
                        "col_offset": 15,
                        "end_col_offset": 24,
                        "end_lineno": 21,
                        "kind": null,
                        "lineno": 21,
                        "n": "#944dff",
                        "s": "#944dff",
                        "value": "#944dff"
                    }
                },
                {
                    "_type": "FunctionDef",
                    "args": {
                        "_type": "arguments",
                        "args": [
                            {
                                "_type": "arg",
                                "annotation": null,
                                "arg": "self",
                                "col_offset": 17,
                                "end_col_offset": 21,
                                "end_lineno": 23,
                                "lineno": 23,
                                "type_comment": null
                            },
                            {
                                "_type": "arg",
                                "annotation": {
                                    "_type": "Name",
                                    "col_offset": 28,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 31,
                                    "end_lineno": 23,
                                    "id": "str",
                                    "lineno": 23
                                },
                                "arg": "sql",
                                "col_offset": 23,
                                "end_col_offset": 31,
                                "end_lineno": 23,
                                "lineno": 23,
                                "type_comment": null
                            },
                            {
                                "_type": "arg",
                                "annotation": {
                                    "_type": "Name",
                                    "col_offset": 51,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 54,
                                    "end_lineno": 23,
                                    "id": "str",
                                    "lineno": 23
                                },
                                "arg": "postgres_conn_id",
                                "col_offset": 33,
                                "end_col_offset": 54,
                                "end_lineno": 23,
                                "lineno": 23,
                                "type_comment": null
                            },
                            {
                                "_type": "arg",
                                "annotation": {
                                    "_type": "Name",
                                    "col_offset": 62,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 65,
                                    "end_lineno": 23,
                                    "id": "str",
                                    "lineno": 23
                                },
                                "arg": "mode",
                                "col_offset": 56,
                                "end_col_offset": 65,
                                "end_lineno": 23,
                                "lineno": 23,
                                "type_comment": null
                            }
                        ],
                        "defaults": [],
                        "kw_defaults": [],
                        "kwarg": {
                            "_type": "arg",
                            "annotation": null,
                            "arg": "kwargs",
                            "col_offset": 69,
                            "end_col_offset": 75,
                            "end_lineno": 23,
                            "lineno": 23,
                            "type_comment": null
                        },
                        "kwonlyargs": [],
                        "posonlyargs": [],
                        "vararg": null
                    },
                    "body": [
                        {
                            "_type": "Expr",
                            "col_offset": 8,
                            "end_col_offset": 34,
                            "end_lineno": 24,
                            "lineno": 24,
                            "value": {
                                "_type": "Call",
                                "args": [],
                                "col_offset": 8,
                                "end_col_offset": 34,
                                "end_lineno": 24,
                                "func": {
                                    "_type": "Attribute",
                                    "attr": "__init__",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 24,
                                    "end_lineno": 24,
                                    "lineno": 24,
                                    "value": {
                                        "_type": "Call",
                                        "args": [],
                                        "col_offset": 8,
                                        "end_col_offset": 15,
                                        "end_lineno": 24,
                                        "func": {
                                            "_type": "Name",
                                            "col_offset": 8,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 13,
                                            "end_lineno": 24,
                                            "id": "super",
                                            "lineno": 24
                                        },
                                        "keywords": [],
                                        "lineno": 24
                                    }
                                },
                                "keywords": [
                                    {
                                        "_type": "keyword",
                                        "arg": null,
                                        "col_offset": 25,
                                        "end_col_offset": 33,
                                        "end_lineno": 24,
                                        "lineno": 24,
                                        "value": {
                                            "_type": "Name",
                                            "col_offset": 27,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 33,
                                            "end_lineno": 24,
                                            "id": "kwargs",
                                            "lineno": 24
                                        }
                                    }
                                ],
                                "lineno": 24
                            }
                        },
                        {
                            "_type": "Assign",
                            "col_offset": 8,
                            "end_col_offset": 22,
                            "end_lineno": 25,
                            "lineno": 25,
                            "targets": [
                                {
                                    "_type": "Attribute",
                                    "attr": "sql",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Store"
                                    },
                                    "end_col_offset": 16,
                                    "end_lineno": 25,
                                    "lineno": 25,
                                    "value": {
                                        "_type": "Name",
                                        "col_offset": 8,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 12,
                                        "end_lineno": 25,
                                        "id": "self",
                                        "lineno": 25
                                    }
                                }
                            ],
                            "type_comment": null,
                            "value": {
                                "_type": "Name",
                                "col_offset": 19,
                                "ctx": {
                                    "_type": "Load"
                                },
                                "end_col_offset": 22,
                                "end_lineno": 25,
                                "id": "sql",
                                "lineno": 25
                            }
                        },
                        {
                            "_type": "Assign",
                            "col_offset": 8,
                            "end_col_offset": 48,
                            "end_lineno": 26,
                            "lineno": 26,
                            "targets": [
                                {
                                    "_type": "Attribute",
                                    "attr": "postgres_conn_id",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Store"
                                    },
                                    "end_col_offset": 29,
                                    "end_lineno": 26,
                                    "lineno": 26,
                                    "value": {
                                        "_type": "Name",
                                        "col_offset": 8,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 12,
                                        "end_lineno": 26,
                                        "id": "self",
                                        "lineno": 26
                                    }
                                }
                            ],
                            "type_comment": null,
                            "value": {
                                "_type": "Name",
                                "col_offset": 32,
                                "ctx": {
                                    "_type": "Load"
                                },
                                "end_col_offset": 48,
                                "end_lineno": 26,
                                "id": "postgres_conn_id",
                                "lineno": 26
                            }
                        },
                        {
                            "_type": "Assign",
                            "col_offset": 8,
                            "end_col_offset": 24,
                            "end_lineno": 27,
                            "lineno": 27,
                            "targets": [
                                {
                                    "_type": "Attribute",
                                    "attr": "mode",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Store"
                                    },
                                    "end_col_offset": 17,
                                    "end_lineno": 27,
                                    "lineno": 27,
                                    "value": {
                                        "_type": "Name",
                                        "col_offset": 8,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 12,
                                        "end_lineno": 27,
                                        "id": "self",
                                        "lineno": 27
                                    }
                                }
                            ],
                            "type_comment": null,
                            "value": {
                                "_type": "Name",
                                "col_offset": 20,
                                "ctx": {
                                    "_type": "Load"
                                },
                                "end_col_offset": 24,
                                "end_lineno": 27,
                                "id": "mode",
                                "lineno": 27
                            }
                        }
                    ],
                    "col_offset": 4,
                    "decorator_list": [],
                    "end_col_offset": 24,
                    "end_lineno": 27,
                    "lineno": 23,
                    "name": "__init__",
                    "returns": {
                        "_type": "Constant",
                        "col_offset": 80,
                        "end_col_offset": 84,
                        "end_lineno": 23,
                        "kind": null,
                        "lineno": 23,
                        "n": null,
                        "s": null,
                        "value": null
                    },
                    "type_comment": null
                },
                {
                    "_type": "FunctionDef",
                    "args": {
                        "_type": "arguments",
                        "args": [
                            {
                                "_type": "arg",
                                "annotation": null,
                                "arg": "self",
                                "col_offset": 13,
                                "end_col_offset": 17,
                                "end_lineno": 29,
                                "lineno": 29,
                                "type_comment": null
                            },
                            {
                                "_type": "arg",
                                "annotation": null,
                                "arg": "context",
                                "col_offset": 19,
                                "end_col_offset": 26,
                                "end_lineno": 29,
                                "lineno": 29,
                                "type_comment": null
                            },
                            {
                                "_type": "arg",
                                "annotation": null,
                                "arg": "records",
                                "col_offset": 28,
                                "end_col_offset": 35,
                                "end_lineno": 29,
                                "lineno": 29,
                                "type_comment": null
                            }
                        ],
                        "defaults": [],
                        "kw_defaults": [],
                        "kwarg": null,
                        "kwonlyargs": [],
                        "posonlyargs": [],
                        "vararg": null
                    },
                    "body": [
                        {
                            "_type": "Expr",
                            "col_offset": 8,
                            "end_col_offset": 58,
                            "end_lineno": 30,
                            "lineno": 30,
                            "value": {
                                "_type": "Call",
                                "args": [],
                                "col_offset": 8,
                                "end_col_offset": 58,
                                "end_lineno": 30,
                                "func": {
                                    "_type": "Attribute",
                                    "attr": "xcom_push",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 31,
                                    "end_lineno": 30,
                                    "lineno": 30,
                                    "value": {
                                        "_type": "Subscript",
                                        "col_offset": 8,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 21,
                                        "end_lineno": 30,
                                        "lineno": 30,
                                        "slice": {
                                            "_type": "Constant",
                                            "col_offset": 16,
                                            "end_col_offset": 20,
                                            "end_lineno": 30,
                                            "kind": null,
                                            "lineno": 30,
                                            "n": "ti",
                                            "s": "ti",
                                            "value": "ti"
                                        },
                                        "value": {
                                            "_type": "Name",
                                            "col_offset": 8,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 15,
                                            "end_lineno": 30,
                                            "id": "context",
                                            "lineno": 30
                                        }
                                    }
                                },
                                "keywords": [
                                    {
                                        "_type": "keyword",
                                        "arg": "key",
                                        "col_offset": 32,
                                        "end_col_offset": 42,
                                        "end_lineno": 30,
                                        "lineno": 30,
                                        "value": {
                                            "_type": "Constant",
                                            "col_offset": 36,
                                            "end_col_offset": 42,
                                            "end_lineno": 30,
                                            "kind": null,
                                            "lineno": 30,
                                            "n": "rows",
                                            "s": "rows",
                                            "value": "rows"
                                        }
                                    },
                                    {
                                        "_type": "keyword",
                                        "arg": "value",
                                        "col_offset": 44,
                                        "end_col_offset": 57,
                                        "end_lineno": 30,
                                        "lineno": 30,
                                        "value": {
                                            "_type": "Name",
                                            "col_offset": 50,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 57,
                                            "end_lineno": 30,
                                            "id": "records",
                                            "lineno": 30
                                        }
                                    }
                                ],
                                "lineno": 30
                            }
                        }
                    ],
                    "col_offset": 4,
                    "decorator_list": [],
                    "end_col_offset": 58,
                    "end_lineno": 30,
                    "lineno": 29,
                    "name": "push",
                    "returns": null,
                    "type_comment": null
                },
                {
                    "_type": "FunctionDef",
                    "args": {
                        "_type": "arguments",
                        "args": [
                            {
                                "_type": "arg",
                                "annotation": null,
                                "arg": "self",
                                "col_offset": 16,
                                "end_col_offset": 20,
                                "end_lineno": 32,
                                "lineno": 32,
                                "type_comment": null
                            },
                            {
                                "_type": "arg",
                                "annotation": null,
                                "arg": "context",
                                "col_offset": 22,
                                "end_col_offset": 29,
                                "end_lineno": 32,
                                "lineno": 32,
                                "type_comment": null
                            }
                        ],
                        "defaults": [],
                        "kw_defaults": [],
                        "kwarg": null,
                        "kwonlyargs": [],
                        "posonlyargs": [],
                        "vararg": null
                    },
                    "body": [
                        {
                            "_type": "Assign",
                            "col_offset": 8,
                            "end_col_offset": 76,
                            "end_lineno": 33,
                            "lineno": 33,
                            "targets": [
                                {
                                    "_type": "Name",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Store"
                                    },
                                    "end_col_offset": 21,
                                    "end_lineno": 33,
                                    "id": "postgres_hook",
                                    "lineno": 33
                                }
                            ],
                            "type_comment": null,
                            "value": {
                                "_type": "Call",
                                "args": [],
                                "col_offset": 24,
                                "end_col_offset": 76,
                                "end_lineno": 33,
                                "func": {
                                    "_type": "Name",
                                    "col_offset": 24,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 36,
                                    "end_lineno": 33,
                                    "id": "PostgresHook",
                                    "lineno": 33
                                },
                                "keywords": [
                                    {
                                        "_type": "keyword",
                                        "arg": "postgres_conn_id",
                                        "col_offset": 37,
                                        "end_col_offset": 75,
                                        "end_lineno": 33,
                                        "lineno": 33,
                                        "value": {
                                            "_type": "Attribute",
                                            "attr": "postgres_conn_id",
                                            "col_offset": 54,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 75,
                                            "end_lineno": 33,
                                            "lineno": 33,
                                            "value": {
                                                "_type": "Name",
                                                "col_offset": 54,
                                                "ctx": {
                                                    "_type": "Load"
                                                },
                                                "end_col_offset": 58,
                                                "end_lineno": 33,
                                                "id": "self",
                                                "lineno": 33
                                            }
                                        }
                                    }
                                ],
                                "lineno": 33
                            }
                        },
                        {
                            "_type": "Expr",
                            "col_offset": 8,
                            "end_col_offset": 23,
                            "end_lineno": 34,
                            "lineno": 34,
                            "value": {
                                "_type": "Call",
                                "args": [],
                                "col_offset": 8,
                                "end_col_offset": 23,
                                "end_lineno": 34,
                                "func": {
                                    "_type": "Name",
                                    "col_offset": 8,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 21,
                                    "end_lineno": 34,
                                    "id": "test_function",
                                    "lineno": 34
                                },
                                "keywords": [],
                                "lineno": 34
                            }
                        },
                        {
                            "_type": "If",
                            "body": [
                                {
                                    "_type": "Assign",
                                    "col_offset": 12,
                                    "end_col_offset": 61,
                                    "end_lineno": 36,
                                    "lineno": 36,
                                    "targets": [
                                        {
                                            "_type": "Name",
                                            "col_offset": 12,
                                            "ctx": {
                                                "_type": "Store"
                                            },
                                            "end_col_offset": 19,
                                            "end_lineno": 36,
                                            "id": "records",
                                            "lineno": 36
                                        }
                                    ],
                                    "type_comment": null,
                                    "value": {
                                        "_type": "Call",
                                        "args": [],
                                        "col_offset": 22,
                                        "end_col_offset": 61,
                                        "end_lineno": 36,
                                        "func": {
                                            "_type": "Attribute",
                                            "attr": "get_records",
                                            "col_offset": 22,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 47,
                                            "end_lineno": 36,
                                            "lineno": 36,
                                            "value": {
                                                "_type": "Name",
                                                "col_offset": 22,
                                                "ctx": {
                                                    "_type": "Load"
                                                },
                                                "end_col_offset": 35,
                                                "end_lineno": 36,
                                                "id": "postgres_hook",
                                                "lineno": 36
                                            }
                                        },
                                        "keywords": [
                                            {
                                                "_type": "keyword",
                                                "arg": "sql",
                                                "col_offset": 48,
                                                "end_col_offset": 60,
                                                "end_lineno": 36,
                                                "lineno": 36,
                                                "value": {
                                                    "_type": "Attribute",
                                                    "attr": "sql",
                                                    "col_offset": 52,
                                                    "ctx": {
                                                        "_type": "Load"
                                                    },
                                                    "end_col_offset": 60,
                                                    "end_lineno": 36,
                                                    "lineno": 36,
                                                    "value": {
                                                        "_type": "Name",
                                                        "col_offset": 52,
                                                        "ctx": {
                                                            "_type": "Load"
                                                        },
                                                        "end_col_offset": 56,
                                                        "end_lineno": 36,
                                                        "id": "self",
                                                        "lineno": 36
                                                    }
                                                }
                                            }
                                        ],
                                        "lineno": 36
                                    }
                                },
                                {
                                    "_type": "Expr",
                                    "col_offset": 12,
                                    "end_col_offset": 39,
                                    "end_lineno": 37,
                                    "lineno": 37,
                                    "value": {
                                        "_type": "Call",
                                        "args": [
                                            {
                                                "_type": "Name",
                                                "col_offset": 22,
                                                "ctx": {
                                                    "_type": "Load"
                                                },
                                                "end_col_offset": 29,
                                                "end_lineno": 37,
                                                "id": "context",
                                                "lineno": 37
                                            },
                                            {
                                                "_type": "Name",
                                                "col_offset": 31,
                                                "ctx": {
                                                    "_type": "Load"
                                                },
                                                "end_col_offset": 38,
                                                "end_lineno": 37,
                                                "id": "records",
                                                "lineno": 37
                                            }
                                        ],
                                        "col_offset": 12,
                                        "end_col_offset": 39,
                                        "end_lineno": 37,
                                        "func": {
                                            "_type": "Attribute",
                                            "attr": "push",
                                            "col_offset": 12,
                                            "ctx": {
                                                "_type": "Load"
                                            },
                                            "end_col_offset": 21,
                                            "end_lineno": 37,
                                            "lineno": 37,
                                            "value": {
                                                "_type": "Name",
                                                "col_offset": 12,
                                                "ctx": {
                                                    "_type": "Load"
                                                },
                                                "end_col_offset": 16,
                                                "end_lineno": 37,
                                                "id": "self",
                                                "lineno": 37
                                            }
                                        },
                                        "keywords": [],
                                        "lineno": 37
                                    }
                                }
                            ],
                            "col_offset": 8,
                            "end_col_offset": 39,
                            "end_lineno": 37,
                            "lineno": 35,
                            "orelse": [],
                            "test": {
                                "_type": "Compare",
                                "col_offset": 12,
                                "comparators": [
                                    {
                                        "_type": "Constant",
                                        "col_offset": 25,
                                        "end_col_offset": 31,
                                        "end_lineno": 35,
                                        "kind": null,
                                        "lineno": 35,
                                        "n": "read",
                                        "s": "read",
                                        "value": "read"
                                    }
                                ],
                                "end_col_offset": 31,
                                "end_lineno": 35,
                                "left": {
                                    "_type": "Attribute",
                                    "attr": "mode",
                                    "col_offset": 12,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "end_col_offset": 21,
                                    "end_lineno": 35,
                                    "lineno": 35,
                                    "value": {
                                        "_type": "Name",
                                        "col_offset": 12,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 16,
                                        "end_lineno": 35,
                                        "id": "self",
                                        "lineno": 35
                                    }
                                },
                                "lineno": 35,
                                "ops": [
                                    {
                                        "_type": "Eq"
                                    }
                                ]
                            }
                        }
                    ],
                    "col_offset": 4,
                    "decorator_list": [],
                    "end_col_offset": 39,
                    "end_lineno": 37,
                    "lineno": 32,
                    "name": "execute",
                    "returns": null,
                    "type_comment": null
                }
            ],
            "col_offset": 0,
            "decorator_list": [],
            "end_col_offset": 39,
            "end_lineno": 37,
            "keywords": [],
            "lineno": 18,
            "name": "GvPostgresOperator"
        },
        {
            "_type": "Assign",
            "col_offset": 0,
            "end_col_offset": 28,
            "end_lineno": 39,
            "lineno": 39,
            "targets": [
                {
                    "_type": "Name",
                    "col_offset": 0,
                    "ctx": {
                        "_type": "Store"
                    },
                    "end_col_offset": 6,
                    "end_lineno": 39,
                    "id": "dag_id",
                    "lineno": 39
                }
            ],
            "type_comment": null,
            "value": {
                "_type": "Attribute",
                "attr": "stem",
                "col_offset": 9,
                "ctx": {
                    "_type": "Load"
                },
                "end_col_offset": 28,
                "end_lineno": 39,
                "lineno": 39,
                "value": {
                    "_type": "Call",
                    "args": [
                        {
                            "_type": "Name",
                            "col_offset": 14,
                            "ctx": {
                                "_type": "Load"
                            },
                            "end_col_offset": 22,
                            "end_lineno": 39,
                            "id": "__file__",
                            "lineno": 39
                        }
                    ],
                    "col_offset": 9,
                    "end_col_offset": 23,
                    "end_lineno": 39,
                    "func": {
                        "_type": "Name",
                        "col_offset": 9,
                        "ctx": {
                            "_type": "Load"
                        },
                        "end_col_offset": 13,
                        "end_lineno": 39,
                        "id": "Path",
                        "lineno": 39
                    },
                    "keywords": [],
                    "lineno": 39
                }
            }
        },
        {
            "_type": "Assign",
            "col_offset": 0,
            "end_col_offset": 1,
            "end_lineno": 59,
            "lineno": 41,
            "targets": [
                {
                    "_type": "Name",
                    "col_offset": 0,
                    "ctx": {
                        "_type": "Store"
                    },
                    "end_col_offset": 3,
                    "end_lineno": 41,
                    "id": "dag",
                    "lineno": 41
                }
            ],
            "type_comment": null,
            "value": {
                "_type": "Call",
                "args": [
                    {
                        "_type": "Name",
                        "col_offset": 4,
                        "ctx": {
                            "_type": "Load"
                        },
                        "end_col_offset": 10,
                        "end_lineno": 42,
                        "id": "dag_id",
                        "lineno": 42
                    }
                ],
                "col_offset": 6,
                "end_col_offset": 1,
                "end_lineno": 59,
                "func": {
                    "_type": "Name",
                    "col_offset": 6,
                    "ctx": {
                        "_type": "Load"
                    },
                    "end_col_offset": 9,
                    "end_lineno": 41,
                    "id": "DAG",
                    "lineno": 41
                },
                "keywords": [
                    {
                        "_type": "keyword",
                        "arg": "default_args",
                        "col_offset": 4,
                        "end_col_offset": 5,
                        "end_lineno": 52,
                        "lineno": 43,
                        "value": {
                            "_type": "Dict",
                            "col_offset": 17,
                            "end_col_offset": 5,
                            "end_lineno": 52,
                            "keys": [
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 15,
                                    "end_lineno": 44,
                                    "kind": null,
                                    "lineno": 44,
                                    "n": "owner",
                                    "s": "owner",
                                    "value": "owner"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 25,
                                    "end_lineno": 45,
                                    "kind": null,
                                    "lineno": 45,
                                    "n": "depends_on_past",
                                    "s": "depends_on_past",
                                    "value": "depends_on_past"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 20,
                                    "end_lineno": 46,
                                    "kind": null,
                                    "lineno": 46,
                                    "n": "start_date",
                                    "s": "start_date",
                                    "value": "start_date"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 15,
                                    "end_lineno": 47,
                                    "kind": null,
                                    "lineno": 47,
                                    "n": "email",
                                    "s": "email",
                                    "value": "email"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 26,
                                    "end_lineno": 48,
                                    "kind": null,
                                    "lineno": 48,
                                    "n": "email_on_failure",
                                    "s": "email_on_failure",
                                    "value": "email_on_failure"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 24,
                                    "end_lineno": 49,
                                    "kind": null,
                                    "lineno": 49,
                                    "n": "email_on_retry",
                                    "s": "email_on_retry",
                                    "value": "email_on_retry"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 17,
                                    "end_lineno": 50,
                                    "kind": null,
                                    "lineno": 50,
                                    "n": "retries",
                                    "s": "retries",
                                    "value": "retries"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 8,
                                    "end_col_offset": 21,
                                    "end_lineno": 51,
                                    "kind": null,
                                    "lineno": 51,
                                    "n": "retry_delay",
                                    "s": "retry_delay",
                                    "value": "retry_delay"
                                }
                            ],
                            "lineno": 43,
                            "values": [
                                {
                                    "_type": "Constant",
                                    "col_offset": 17,
                                    "end_col_offset": 27,
                                    "end_lineno": 44,
                                    "kind": null,
                                    "lineno": 44,
                                    "n": "Jegath S",
                                    "s": "Jegath S",
                                    "value": "Jegath S"
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 27,
                                    "end_col_offset": 31,
                                    "end_lineno": 45,
                                    "kind": null,
                                    "lineno": 45,
                                    "n": true,
                                    "s": true,
                                    "value": true
                                },
                                {
                                    "_type": "Call",
                                    "args": [
                                        {
                                            "_type": "Constant",
                                            "col_offset": 31,
                                            "end_col_offset": 32,
                                            "end_lineno": 46,
                                            "kind": null,
                                            "lineno": 46,
                                            "n": 1,
                                            "s": 1,
                                            "value": 1
                                        }
                                    ],
                                    "col_offset": 22,
                                    "end_col_offset": 33,
                                    "end_lineno": 46,
                                    "func": {
                                        "_type": "Name",
                                        "col_offset": 22,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 30,
                                        "end_lineno": 46,
                                        "id": "days_ago",
                                        "lineno": 46
                                    },
                                    "keywords": [],
                                    "lineno": 46
                                },
                                {
                                    "_type": "List",
                                    "col_offset": 17,
                                    "ctx": {
                                        "_type": "Load"
                                    },
                                    "elts": [
                                        {
                                            "_type": "Constant",
                                            "col_offset": 18,
                                            "end_col_offset": 49,
                                            "end_lineno": 47,
                                            "kind": null,
                                            "lineno": 47,
                                            "n": "jegath.suresh@grandvision.com",
                                            "s": "jegath.suresh@grandvision.com",
                                            "value": "jegath.suresh@grandvision.com"
                                        }
                                    ],
                                    "end_col_offset": 50,
                                    "end_lineno": 47,
                                    "lineno": 47
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 28,
                                    "end_col_offset": 33,
                                    "end_lineno": 48,
                                    "kind": null,
                                    "lineno": 48,
                                    "n": false,
                                    "s": false,
                                    "value": false
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 26,
                                    "end_col_offset": 31,
                                    "end_lineno": 49,
                                    "kind": null,
                                    "lineno": 49,
                                    "n": false,
                                    "s": false,
                                    "value": false
                                },
                                {
                                    "_type": "Constant",
                                    "col_offset": 19,
                                    "end_col_offset": 20,
                                    "end_lineno": 50,
                                    "kind": null,
                                    "lineno": 50,
                                    "n": 3,
                                    "s": 3,
                                    "value": 3
                                },
                                {
                                    "_type": "Call",
                                    "args": [],
                                    "col_offset": 23,
                                    "end_col_offset": 43,
                                    "end_lineno": 51,
                                    "func": {
                                        "_type": "Name",
                                        "col_offset": 23,
                                        "ctx": {
                                            "_type": "Load"
                                        },
                                        "end_col_offset": 32,
                                        "end_lineno": 51,
                                        "id": "timedelta",
                                        "lineno": 51
                                    },
                                    "keywords": [
                                        {
                                            "_type": "keyword",
                                            "arg": "minutes",
                                            "col_offset": 33,
                                            "end_col_offset": 42,
                                            "end_lineno": 51,
                                            "lineno": 51,
                                            "value": {
                                                "_type": "Constant",
                                                "col_offset": 41,
                                                "end_col_offset": 42,
                                                "end_lineno": 51,
                                                "kind": null,
                                                "lineno": 51,
                                                "n": 5,
                                                "s": 5,
                                                "value": 5
                                            }
                                        }
                                    ],
                                    "lineno": 51
                                }
                            ]
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "description",
                        "col_offset": 4,
                        "end_col_offset": 7,
                        "end_lineno": 55,
                        "lineno": 53,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 16,
                            "end_col_offset": 7,
                            "end_lineno": 55,
                            "kind": null,
                            "lineno": 53,
                            "n": "\n        Generate datalake from CDR mutations\n    ",
                            "s": "\n        Generate datalake from CDR mutations\n    ",
                            "value": "\n        Generate datalake from CDR mutations\n    "
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "schedule_interval",
                        "col_offset": 4,
                        "end_col_offset": 33,
                        "end_lineno": 56,
                        "lineno": 56,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 22,
                            "end_col_offset": 33,
                            "end_lineno": 56,
                            "kind": null,
                            "lineno": 56,
                            "n": "0 0 * * *",
                            "s": "0 0 * * *",
                            "value": "0 0 * * *"
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "concurrency",
                        "col_offset": 4,
                        "end_col_offset": 18,
                        "end_lineno": 57,
                        "lineno": 57,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 16,
                            "end_col_offset": 18,
                            "end_lineno": 57,
                            "kind": null,
                            "lineno": 57,
                            "n": 10,
                            "s": 10,
                            "value": 10
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "tags",
                        "col_offset": 4,
                        "end_col_offset": 20,
                        "end_lineno": 58,
                        "lineno": 58,
                        "value": {
                            "_type": "List",
                            "col_offset": 9,
                            "ctx": {
                                "_type": "Load"
                            },
                            "elts": [
                                {
                                    "_type": "Constant",
                                    "col_offset": 10,
                                    "end_col_offset": 19,
                                    "end_lineno": 58,
                                    "kind": null,
                                    "lineno": 58,
                                    "n": "hashing",
                                    "s": "hashing",
                                    "value": "hashing"
                                }
                            ],
                            "end_col_offset": 20,
                            "end_lineno": 58,
                            "lineno": 58
                        }
                    }
                ],
                "lineno": 41
            }
        },
        {
            "_type": "Assign",
            "col_offset": 0,
            "end_col_offset": 1,
            "end_lineno": 66,
            "lineno": 60,
            "targets": [
                {
                    "_type": "Name",
                    "col_offset": 0,
                    "ctx": {
                        "_type": "Store"
                    },
                    "end_col_offset": 12,
                    "end_lineno": 60,
                    "id": "get_entities",
                    "lineno": 60
                }
            ],
            "type_comment": null,
            "value": {
                "_type": "Call",
                "args": [],
                "col_offset": 15,
                "end_col_offset": 1,
                "end_lineno": 66,
                "func": {
                    "_type": "Name",
                    "col_offset": 15,
                    "ctx": {
                        "_type": "Load"
                    },
                    "end_col_offset": 33,
                    "end_lineno": 60,
                    "id": "GvPostgresOperator",
                    "lineno": 60
                },
                "keywords": [
                    {
                        "_type": "keyword",
                        "arg": "dag",
                        "col_offset": 4,
                        "end_col_offset": 11,
                        "end_lineno": 61,
                        "lineno": 61,
                        "value": {
                            "_type": "Name",
                            "col_offset": 8,
                            "ctx": {
                                "_type": "Load"
                            },
                            "end_col_offset": 11,
                            "end_lineno": 61,
                            "id": "dag",
                            "lineno": 61
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "postgres_conn_id",
                        "col_offset": 4,
                        "end_col_offset": 48,
                        "end_lineno": 62,
                        "lineno": 62,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 21,
                            "end_col_offset": 48,
                            "end_lineno": 62,
                            "kind": null,
                            "lineno": 62,
                            "n": "postges_developer_hub_dev",
                            "s": "postges_developer_hub_dev",
                            "value": "postges_developer_hub_dev"
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "task_id",
                        "col_offset": 4,
                        "end_col_offset": 26,
                        "end_lineno": 63,
                        "lineno": 63,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 12,
                            "end_col_offset": 26,
                            "end_lineno": 63,
                            "kind": null,
                            "lineno": 63,
                            "n": "get_entities",
                            "s": "get_entities",
                            "value": "get_entities"
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "sql",
                        "col_offset": 4,
                        "end_col_offset": 53,
                        "end_lineno": 64,
                        "lineno": 64,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 8,
                            "end_col_offset": 53,
                            "end_lineno": 64,
                            "kind": null,
                            "lineno": 64,
                            "n": "SELECT entity_name,is_enabled FROM entities",
                            "s": "SELECT entity_name,is_enabled FROM entities",
                            "value": "SELECT entity_name,is_enabled FROM entities"
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "mode",
                        "col_offset": 4,
                        "end_col_offset": 15,
                        "end_lineno": 65,
                        "lineno": 65,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 9,
                            "end_col_offset": 15,
                            "end_lineno": 65,
                            "kind": null,
                            "lineno": 65,
                            "n": "read",
                            "s": "read",
                            "value": "read"
                        }
                    }
                ],
                "lineno": 60
            }
        },
        {
            "_type": "Assign",
            "col_offset": 0,
            "end_col_offset": 1,
            "end_lineno": 72,
            "lineno": 68,
            "targets": [
                {
                    "_type": "Name",
                    "col_offset": 0,
                    "ctx": {
                        "_type": "Store"
                    },
                    "end_col_offset": 11,
                    "end_lineno": 68,
                    "id": "python_task",
                    "lineno": 68
                }
            ],
            "type_comment": null,
            "value": {
                "_type": "Call",
                "args": [],
                "col_offset": 14,
                "end_col_offset": 1,
                "end_lineno": 72,
                "func": {
                    "_type": "Name",
                    "col_offset": 14,
                    "ctx": {
                        "_type": "Load"
                    },
                    "end_col_offset": 28,
                    "end_lineno": 68,
                    "id": "PythonOperator",
                    "lineno": 68
                },
                "keywords": [
                    {
                        "_type": "keyword",
                        "arg": "dag",
                        "col_offset": 4,
                        "end_col_offset": 11,
                        "end_lineno": 69,
                        "lineno": 69,
                        "value": {
                            "_type": "Name",
                            "col_offset": 8,
                            "ctx": {
                                "_type": "Load"
                            },
                            "end_col_offset": 11,
                            "end_lineno": 69,
                            "id": "dag",
                            "lineno": 69
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "python_callable",
                        "col_offset": 4,
                        "end_col_offset": 33,
                        "end_lineno": 70,
                        "lineno": 70,
                        "value": {
                            "_type": "Name",
                            "col_offset": 20,
                            "ctx": {
                                "_type": "Load"
                            },
                            "end_col_offset": 33,
                            "end_lineno": 70,
                            "id": "test_function",
                            "lineno": 70
                        }
                    },
                    {
                        "_type": "keyword",
                        "arg": "task_id",
                        "col_offset": 4,
                        "end_col_offset": 28,
                        "end_lineno": 71,
                        "lineno": 71,
                        "value": {
                            "_type": "Constant",
                            "col_offset": 12,
                            "end_col_offset": 28,
                            "end_lineno": 71,
                            "kind": null,
                            "lineno": 71,
                            "n": "python_test_op",
                            "s": "python_test_op",
                            "value": "python_test_op"
                        }
                    }
                ],
                "lineno": 68
            }
        },
        {
            "_type": "Expr",
            "col_offset": 0,
            "end_col_offset": 27,
            "end_lineno": 74,
            "lineno": 74,
            "value": {
                "_type": "BinOp",
                "col_offset": 0,
                "end_col_offset": 27,
                "end_lineno": 74,
                "left": {
                    "_type": "Name",
                    "col_offset": 0,
                    "ctx": {
                        "_type": "Load"
                    },
                    "end_col_offset": 12,
                    "end_lineno": 74,
                    "id": "get_entities",
                    "lineno": 74
                },
                "lineno": 74,
                "op": {
                    "_type": "RShift"
                },
                "right": {
                    "_type": "Name",
                    "col_offset": 16,
                    "ctx": {
                        "_type": "Load"
                    },
                    "end_col_offset": 27,
                    "end_lineno": 74,
                    "id": "python_task",
                    "lineno": 74
                }
            }
        }
    ],
    "type_ignores": []
}
```
</details>

<details>
<summary><b>Sample AST for test.py</b></summary>

```python
from ast import ImportFrom, alias, Module,Assign,Constant,FunctionDef, Load,Store,arguments,Expr,ClassDef,Name,Call,Tuple,arg,Attribute,Subscript,keyword,Compare,BinOp,List,RShift, If,Dict,Eq,AugAssign, Add,Import

Module(
    body=[
        ImportFrom(
            module='airflow',
            names=[
                alias(
                    name='DAG',
                    lineno=1,
                    col_offset=20,
                    end_lineno=1,
                    end_col_offset=23)],
            level=0,
            lineno=1,
            col_offset=0,
            end_lineno=1,
            end_col_offset=23),
        ImportFrom(
            module='pathlib',
            names=[
                alias(
                    name='Path',
                    lineno=2,
                    col_offset=20,
                    end_lineno=2,
                    end_col_offset=24)],
            level=0,
            lineno=2,
            col_offset=0,
            end_lineno=2,
            end_col_offset=24),
        ImportFrom(
            module='airflow.utils.dates',
            names=[
                alias(
                    name='days_ago',
                    lineno=3,
                    col_offset=32,
                    end_lineno=3,
                    end_col_offset=40)],
            level=0,
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=40),
        ImportFrom(
            module='datetime',
            names=[
                alias(
                    name='timedelta',
                    lineno=4,
                    col_offset=21,
                    end_lineno=4,
                    end_col_offset=30)],
            level=0,
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=30),
        ImportFrom(
            module='airflow.models',
            names=[
                alias(
                    name='BaseOperator',
                    lineno=6,
                    col_offset=27,
                    end_lineno=6,
                    end_col_offset=39)],
            level=0,
            lineno=6,
            col_offset=0,
            end_lineno=6,
            end_col_offset=39),
        ImportFrom(
            module='airflow.providers.postgres.hooks.postgres',
            names=[
                alias(
                    name='PostgresHook',
                    lineno=7,
                    col_offset=54,
                    end_lineno=7,
                    end_col_offset=66)],
            level=0,
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=66),
        ImportFrom(
            module='airflow.operators.python',
            names=[
                alias(
                    name='PythonOperator',
                    lineno=8,
                    col_offset=37,
                    end_lineno=8,
                    end_col_offset=51)],
            level=0,
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=51),
        Import(
            names=[
                alias(
                    name='os',
                    lineno=9,
                    col_offset=7,
                    end_lineno=9,
                    end_col_offset=9)],
            lineno=9,
            col_offset=0,
            end_lineno=9,
            end_col_offset=9),
        Assign(
            targets=[
                Name(
                    id='this_is_a_global_variable',
                    ctx=Store(),
                    lineno=11,
                    col_offset=0,
                    end_lineno=11,
                    end_col_offset=25)],
            value=Constant(
                value=10,
                lineno=11,
                col_offset=28,
                end_lineno=11,
                end_col_offset=30),
            lineno=11,
            col_offset=0,
            end_lineno=11,
            end_col_offset=30),
        FunctionDef(
            name='test_function',
            args=arguments(
                posonlyargs=[],
                args=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Expr(
                    value=Call(
                        func=Name(
                            id='print',
                            ctx=Load(),
                            lineno=14,
                            col_offset=4,
                            end_lineno=14,
                            end_col_offset=9),
                        args=[
                            Constant(
                                value='This is a test function',
                                lineno=14,
                                col_offset=10,
                                end_lineno=14,
                                end_col_offset=35)],
                        keywords=[],
                        lineno=14,
                        col_offset=4,
                        end_lineno=14,
                        end_col_offset=36),
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=36)],
            decorator_list=[],
            lineno=13,
            col_offset=0,
            end_lineno=14,
            end_col_offset=36),
        AugAssign(
            target=Name(
                id='this_is_a_global_variable',
                ctx=Store(),
                lineno=16,
                col_offset=0,
                end_lineno=16,
                end_col_offset=25),
            op=Add(),
            value=Constant(
                value=1,
                lineno=16,
                col_offset=29,
                end_lineno=16,
                end_col_offset=30),
            lineno=16,
            col_offset=0,
            end_lineno=16,
            end_col_offset=30),
        ClassDef(
            name='GvPostgresOperator',
            bases=[
                Name(
                    id='BaseOperator',
                    ctx=Load(),
                    lineno=18,
                    col_offset=25,
                    end_lineno=18,
                    end_col_offset=37)],
            keywords=[],
            body=[
                Assign(
                    targets=[
                        Name(
                            id='template_fields',
                            ctx=Store(),
                            lineno=19,
                            col_offset=4,
                            end_lineno=19,
                            end_col_offset=19)],
                    value=Tuple(
                        elts=[
                            Constant(
                                value='sql',
                                lineno=19,
                                col_offset=23,
                                end_lineno=19,
                                end_col_offset=28)],
                        ctx=Load(),
                        lineno=19,
                        col_offset=22,
                        end_lineno=19,
                        end_col_offset=30),
                    lineno=19,
                    col_offset=4,
                    end_lineno=19,
                    end_col_offset=30),
                Assign(
                    targets=[
                        Name(
                            id='template_ext',
                            ctx=Store(),
                            lineno=20,
                            col_offset=4,
                            end_lineno=20,
                            end_col_offset=16)],
                    value=Tuple(
                        elts=[
                            Constant(
                                value='.sql',
                                lineno=20,
                                col_offset=20,
                                end_lineno=20,
                                end_col_offset=26)],
                        ctx=Load(),
                        lineno=20,
                        col_offset=19,
                        end_lineno=20,
                        end_col_offset=28),
                    lineno=20,
                    col_offset=4,
                    end_lineno=20,
                    end_col_offset=28),
                Assign(
                    targets=[
                        Name(
                            id='ui_color',
                            ctx=Store(),
                            lineno=21,
                            col_offset=4,
                            end_lineno=21,
                            end_col_offset=12)],
                    value=Constant(
                        value='#944dff',
                        lineno=21,
                        col_offset=15,
                        end_lineno=21,
                        end_col_offset=24),
                    lineno=21,
                    col_offset=4,
                    end_lineno=21,
                    end_col_offset=24),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(
                                arg='self',
                                lineno=23,
                                col_offset=17,
                                end_lineno=23,
                                end_col_offset=21),
                            arg(
                                arg='sql',
                                annotation=Name(
                                    id='str',
                                    ctx=Load(),
                                    lineno=23,
                                    col_offset=28,
                                    end_lineno=23,
                                    end_col_offset=31),
                                lineno=23,
                                col_offset=23,
                                end_lineno=23,
                                end_col_offset=31),
                            arg(
                                arg='postgres_conn_id',
                                annotation=Name(
                                    id='str',
                                    ctx=Load(),
                                    lineno=23,
                                    col_offset=51,
                                    end_lineno=23,
                                    end_col_offset=54),
                                lineno=23,
                                col_offset=33,
                                end_lineno=23,
                                end_col_offset=54),
                            arg(
                                arg='mode',
                                annotation=Name(
                                    id='str',
                                    ctx=Load(),
                                    lineno=23,
                                    col_offset=62,
                                    end_lineno=23,
                                    end_col_offset=65),
                                lineno=23,
                                col_offset=56,
                                end_lineno=23,
                                end_col_offset=65)],
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(
                            arg='kwargs',
                            lineno=23,
                            col_offset=69,
                            end_lineno=23,
                            end_col_offset=75),
                        defaults=[]),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(
                                            id='super',
                                            ctx=Load(),
                                            lineno=24,
                                            col_offset=8,
                                            end_lineno=24,
                                            end_col_offset=13),
                                        args=[],
                                        keywords=[],
                                        lineno=24,
                                        col_offset=8,
                                        end_lineno=24,
                                        end_col_offset=15),
                                    attr='__init__',
                                    ctx=Load(),
                                    lineno=24,
                                    col_offset=8,
                                    end_lineno=24,
                                    end_col_offset=24),
                                args=[],
                                keywords=[
                                    keyword(
                                        value=Name(
                                            id='kwargs',
                                            ctx=Load(),
                                            lineno=24,
                                            col_offset=27,
                                            end_lineno=24,
                                            end_col_offset=33),
                                        lineno=24,
                                        col_offset=25,
                                        end_lineno=24,
                                        end_col_offset=33)],
                                lineno=24,
                                col_offset=8,
                                end_lineno=24,
                                end_col_offset=34),
                            lineno=24,
                            col_offset=8,
                            end_lineno=24,
                            end_col_offset=34),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(
                                        id='self',
                                        ctx=Load(),
                                        lineno=25,
                                        col_offset=8,
                                        end_lineno=25,
                                        end_col_offset=12),
                                    attr='sql',
                                    ctx=Store(),
                                    lineno=25,
                                    col_offset=8,
                                    end_lineno=25,
                                    end_col_offset=16)],
                            value=Name(
                                id='sql',
                                ctx=Load(),
                                lineno=25,
                                col_offset=19,
                                end_lineno=25,
                                end_col_offset=22),
                            lineno=25,
                            col_offset=8,
                            end_lineno=25,
                            end_col_offset=22),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(
                                        id='self',
                                        ctx=Load(),
                                        lineno=26,
                                        col_offset=8,
                                        end_lineno=26,
                                        end_col_offset=12),
                                    attr='postgres_conn_id',
                                    ctx=Store(),
                                    lineno=26,
                                    col_offset=8,
                                    end_lineno=26,
                                    end_col_offset=29)],
                            value=Name(
                                id='postgres_conn_id',
                                ctx=Load(),
                                lineno=26,
                                col_offset=32,
                                end_lineno=26,
                                end_col_offset=48),
                            lineno=26,
                            col_offset=8,
                            end_lineno=26,
                            end_col_offset=48),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(
                                        id='self',
                                        ctx=Load(),
                                        lineno=27,
                                        col_offset=8,
                                        end_lineno=27,
                                        end_col_offset=12),
                                    attr='mode',
                                    ctx=Store(),
                                    lineno=27,
                                    col_offset=8,
                                    end_lineno=27,
                                    end_col_offset=17)],
                            value=Name(
                                id='mode',
                                ctx=Load(),
                                lineno=27,
                                col_offset=20,
                                end_lineno=27,
                                end_col_offset=24),
                            lineno=27,
                            col_offset=8,
                            end_lineno=27,
                            end_col_offset=24)],
                    decorator_list=[],
                    returns=Constant(
                        value=None,
                        lineno=23,
                        col_offset=80,
                        end_lineno=23,
                        end_col_offset=84),
                    lineno=23,
                    col_offset=4,
                    end_lineno=27,
                    end_col_offset=24),
                FunctionDef(
                    name='push',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(
                                arg='self',
                                lineno=29,
                                col_offset=13,
                                end_lineno=29,
                                end_col_offset=17),
                            arg(
                                arg='context',
                                lineno=29,
                                col_offset=19,
                                end_lineno=29,
                                end_col_offset=26),
                            arg(
                                arg='records',
                                lineno=29,
                                col_offset=28,
                                end_lineno=29,
                                end_col_offset=35)],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[]),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(
                                            id='context',
                                            ctx=Load(),
                                            lineno=30,
                                            col_offset=8,
                                            end_lineno=30,
                                            end_col_offset=15),
                                        slice=Constant(
                                            value='ti',
                                            lineno=30,
                                            col_offset=16,
                                            end_lineno=30,
                                            end_col_offset=20),
                                        ctx=Load(),
                                        lineno=30,
                                        col_offset=8,
                                        end_lineno=30,
                                        end_col_offset=21),
                                    attr='xcom_push',
                                    ctx=Load(),
                                    lineno=30,
                                    col_offset=8,
                                    end_lineno=30,
                                    end_col_offset=31),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Constant(
                                            value='rows',
                                            lineno=30,
                                            col_offset=36,
                                            end_lineno=30,
                                            end_col_offset=42),
                                        lineno=30,
                                        col_offset=32,
                                        end_lineno=30,
                                        end_col_offset=42),
                                    keyword(
                                        arg='value',
                                        value=Name(
                                            id='records',
                                            ctx=Load(),
                                            lineno=30,
                                            col_offset=50,
                                            end_lineno=30,
                                            end_col_offset=57),
                                        lineno=30,
                                        col_offset=44,
                                        end_lineno=30,
                                        end_col_offset=57)],
                                lineno=30,
                                col_offset=8,
                                end_lineno=30,
                                end_col_offset=58),
                            lineno=30,
                            col_offset=8,
                            end_lineno=30,
                            end_col_offset=58)],
                    decorator_list=[],
                    lineno=29,
                    col_offset=4,
                    end_lineno=30,
                    end_col_offset=58),
                FunctionDef(
                    name='execute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(
                                arg='self',
                                lineno=32,
                                col_offset=16,
                                end_lineno=32,
                                end_col_offset=20),
                            arg(
                                arg='context',
                                lineno=32,
                                col_offset=22,
                                end_lineno=32,
                                end_col_offset=29)],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[]),
                    body=[
                        Assign(
                            targets=[
                                Name(
                                    id='postgres_hook',
                                    ctx=Store(),
                                    lineno=33,
                                    col_offset=8,
                                    end_lineno=33,
                                    end_col_offset=21)],
                            value=Call(
                                func=Name(
                                    id='PostgresHook',
                                    ctx=Load(),
                                    lineno=33,
                                    col_offset=24,
                                    end_lineno=33,
                                    end_col_offset=36),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='postgres_conn_id',
                                        value=Attribute(
                                            value=Name(
                                                id='self',
                                                ctx=Load(),
                                                lineno=33,
                                                col_offset=54,
                                                end_lineno=33,
                                                end_col_offset=58),
                                            attr='postgres_conn_id',
                                            ctx=Load(),
                                            lineno=33,
                                            col_offset=54,
                                            end_lineno=33,
                                            end_col_offset=75),
                                        lineno=33,
                                        col_offset=37,
                                        end_lineno=33,
                                        end_col_offset=75)],
                                lineno=33,
                                col_offset=24,
                                end_lineno=33,
                                end_col_offset=76),
                            lineno=33,
                            col_offset=8,
                            end_lineno=33,
                            end_col_offset=76),
                        Expr(
                            value=Call(
                                func=Name(
                                    id='test_function',
                                    ctx=Load(),
                                    lineno=34,
                                    col_offset=8,
                                    end_lineno=34,
                                    end_col_offset=21),
                                args=[],
                                keywords=[],
                                lineno=34,
                                col_offset=8,
                                end_lineno=34,
                                end_col_offset=23),
                            lineno=34,
                            col_offset=8,
                            end_lineno=34,
                            end_col_offset=23),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(
                                        id='self',
                                        ctx=Load(),
                                        lineno=35,
                                        col_offset=12,
                                        end_lineno=35,
                                        end_col_offset=16),
                                    attr='mode',
                                    ctx=Load(),
                                    lineno=35,
                                    col_offset=12,
                                    end_lineno=35,
                                    end_col_offset=21),
                                ops=[
                                    Eq()],
                                comparators=[
                                    Constant(
                                        value='read',
                                        lineno=35,
                                        col_offset=25,
                                        end_lineno=35,
                                        end_col_offset=31)],
                                lineno=35,
                                col_offset=12,
                                end_lineno=35,
                                end_col_offset=31),
                            body=[
                                Assign(
                                    targets=[
                                        Name(
                                            id='records',
                                            ctx=Store(),
                                            lineno=36,
                                            col_offset=12,
                                            end_lineno=36,
                                            end_col_offset=19)],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(
                                                id='postgres_hook',
                                                ctx=Load(),
                                                lineno=36,
                                                col_offset=22,
                                                end_lineno=36,
                                                end_col_offset=35),
                                            attr='get_records',
                                            ctx=Load(),
                                            lineno=36,
                                            col_offset=22,
                                            end_lineno=36,
                                            end_col_offset=47),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='sql',
                                                value=Attribute(
                                                    value=Name(
                                                        id='self',
                                                        ctx=Load(),
                                                        lineno=36,
                                                        col_offset=52,
                                                        end_lineno=36,
                                                        end_col_offset=56),
                                                    attr='sql',
                                                    ctx=Load(),
                                                    lineno=36,
                                                    col_offset=52,
                                                    end_lineno=36,
                                                    end_col_offset=60),
                                                lineno=36,
                                                col_offset=48,
                                                end_lineno=36,
                                                end_col_offset=60)],
                                        lineno=36,
                                        col_offset=22,
                                        end_lineno=36,
                                        end_col_offset=61),
                                    lineno=36,
                                    col_offset=12,
                                    end_lineno=36,
                                    end_col_offset=61),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(
                                                id='self',
                                                ctx=Load(),
                                                lineno=37,
                                                col_offset=12,
                                                end_lineno=37,
                                                end_col_offset=16),
                                            attr='push',
                                            ctx=Load(),
                                            lineno=37,
                                            col_offset=12,
                                            end_lineno=37,
                                            end_col_offset=21),
                                        args=[
                                            Name(
                                                id='context',
                                                ctx=Load(),
                                                lineno=37,
                                                col_offset=22,
                                                end_lineno=37,
                                                end_col_offset=29),
                                            Name(
                                                id='records',
                                                ctx=Load(),
                                                lineno=37,
                                                col_offset=31,
                                                end_lineno=37,
                                                end_col_offset=38)],
                                        keywords=[],
                                        lineno=37,
                                        col_offset=12,
                                        end_lineno=37,
                                        end_col_offset=39),
                                    lineno=37,
                                    col_offset=12,
                                    end_lineno=37,
                                    end_col_offset=39)],
                            orelse=[],
                            lineno=35,
                            col_offset=8,
                            end_lineno=37,
                            end_col_offset=39)],
                    decorator_list=[],
                    lineno=32,
                    col_offset=4,
                    end_lineno=37,
                    end_col_offset=39)],
            decorator_list=[],
            lineno=18,
            col_offset=0,
            end_lineno=37,
            end_col_offset=39),
        Assign(
            targets=[
                Name(
                    id='dag_id',
                    ctx=Store(),
                    lineno=39,
                    col_offset=0,
                    end_lineno=39,
                    end_col_offset=6)],
            value=Attribute(
                value=Call(
                    func=Name(
                        id='Path',
                        ctx=Load(),
                        lineno=39,
                        col_offset=9,
                        end_lineno=39,
                        end_col_offset=13),
                    args=[
                        Name(
                            id='__file__',
                            ctx=Load(),
                            lineno=39,
                            col_offset=14,
                            end_lineno=39,
                            end_col_offset=22)],
                    keywords=[],
                    lineno=39,
                    col_offset=9,
                    end_lineno=39,
                    end_col_offset=23),
                attr='stem',
                ctx=Load(),
                lineno=39,
                col_offset=9,
                end_lineno=39,
                end_col_offset=28),
            lineno=39,
            col_offset=0,
            end_lineno=39,
            end_col_offset=28),
        Assign(
            targets=[
                Name(
                    id='dag',
                    ctx=Store(),
                    lineno=41,
                    col_offset=0,
                    end_lineno=41,
                    end_col_offset=3)],
            value=Call(
                func=Name(
                    id='DAG',
                    ctx=Load(),
                    lineno=41,
                    col_offset=6,
                    end_lineno=41,
                    end_col_offset=9),
                args=[
                    Name(
                        id='dag_id',
                        ctx=Load(),
                        lineno=42,
                        col_offset=4,
                        end_lineno=42,
                        end_col_offset=10)],
                keywords=[
                    keyword(
                        arg='default_args',
                        value=Dict(
                            keys=[
                                Constant(
                                    value='owner',
                                    lineno=44,
                                    col_offset=8,
                                    end_lineno=44,
                                    end_col_offset=15),
                                Constant(
                                    value='depends_on_past',
                                    lineno=45,
                                    col_offset=8,
                                    end_lineno=45,
                                    end_col_offset=25),
                                Constant(
                                    value='start_date',
                                    lineno=46,
                                    col_offset=8,
                                    end_lineno=46,
                                    end_col_offset=20),
                                Constant(
                                    value='email',
                                    lineno=47,
                                    col_offset=8,
                                    end_lineno=47,
                                    end_col_offset=15),
                                Constant(
                                    value='email_on_failure',
                                    lineno=48,
                                    col_offset=8,
                                    end_lineno=48,
                                    end_col_offset=26),
                                Constant(
                                    value='email_on_retry',
                                    lineno=49,
                                    col_offset=8,
                                    end_lineno=49,
                                    end_col_offset=24),
                                Constant(
                                    value='retries',
                                    lineno=50,
                                    col_offset=8,
                                    end_lineno=50,
                                    end_col_offset=17),
                                Constant(
                                    value='retry_delay',
                                    lineno=51,
                                    col_offset=8,
                                    end_lineno=51,
                                    end_col_offset=21)],
                            values=[
                                Constant(
                                    value='Jegath S',
                                    lineno=44,
                                    col_offset=17,
                                    end_lineno=44,
                                    end_col_offset=27),
                                Constant(
                                    value=True,
                                    lineno=45,
                                    col_offset=27,
                                    end_lineno=45,
                                    end_col_offset=31),
                                Call(
                                    func=Name(
                                        id='days_ago',
                                        ctx=Load(),
                                        lineno=46,
                                        col_offset=22,
                                        end_lineno=46,
                                        end_col_offset=30),
                                    args=[
                                        Constant(
                                            value=1,
                                            lineno=46,
                                            col_offset=31,
                                            end_lineno=46,
                                            end_col_offset=32)],
                                    keywords=[],
                                    lineno=46,
                                    col_offset=22,
                                    end_lineno=46,
                                    end_col_offset=33),
                                List(
                                    elts=[
                                        Constant(
                                            value='jegath.suresh@grandvision.com',
                                            lineno=47,
                                            col_offset=18,
                                            end_lineno=47,
                                            end_col_offset=49)],
                                    ctx=Load(),
                                    lineno=47,
                                    col_offset=17,
                                    end_lineno=47,
                                    end_col_offset=50),
                                Constant(
                                    value=False,
                                    lineno=48,
                                    col_offset=28,
                                    end_lineno=48,
                                    end_col_offset=33),
                                Constant(
                                    value=False,
                                    lineno=49,
                                    col_offset=26,
                                    end_lineno=49,
                                    end_col_offset=31),
                                Constant(
                                    value=3,
                                    lineno=50,
                                    col_offset=19,
                                    end_lineno=50,
                                    end_col_offset=20),
                                Call(
                                    func=Name(
                                        id='timedelta',
                                        ctx=Load(),
                                        lineno=51,
                                        col_offset=23,
                                        end_lineno=51,
                                        end_col_offset=32),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='minutes',
                                            value=Constant(
                                                value=5,
                                                lineno=51,
                                                col_offset=41,
                                                end_lineno=51,
                                                end_col_offset=42),
                                            lineno=51,
                                            col_offset=33,
                                            end_lineno=51,
                                            end_col_offset=42)],
                                    lineno=51,
                                    col_offset=23,
                                    end_lineno=51,
                                    end_col_offset=43)],
                            lineno=43,
                            col_offset=17,
                            end_lineno=52,
                            end_col_offset=5),
                        lineno=43,
                        col_offset=4,
                        end_lineno=52,
                        end_col_offset=5),
                    keyword(
                        arg='description',
                        value=Constant(
                            value='\n        Generate datalake from CDR mutations\n    ',
                            lineno=53,
                            col_offset=16,
                            end_lineno=55,
                            end_col_offset=7),
                        lineno=53,
                        col_offset=4,
                        end_lineno=55,
                        end_col_offset=7),
                    keyword(
                        arg='schedule_interval',
                        value=Constant(
                            value='0 0 * * *',
                            lineno=56,
                            col_offset=22,
                            end_lineno=56,
                            end_col_offset=33),
                        lineno=56,
                        col_offset=4,
                        end_lineno=56,
                        end_col_offset=33),
                    keyword(
                        arg='concurrency',
                        value=Constant(
                            value=10,
                            lineno=57,
                            col_offset=16,
                            end_lineno=57,
                            end_col_offset=18),
                        lineno=57,
                        col_offset=4,
                        end_lineno=57,
                        end_col_offset=18),
                    keyword(
                        arg='tags',
                        value=List(
                            elts=[
                                Constant(
                                    value='hashing',
                                    lineno=58,
                                    col_offset=10,
                                    end_lineno=58,
                                    end_col_offset=19)],
                            ctx=Load(),
                            lineno=58,
                            col_offset=9,
                            end_lineno=58,
                            end_col_offset=20),
                        lineno=58,
                        col_offset=4,
                        end_lineno=58,
                        end_col_offset=20)],
                lineno=41,
                col_offset=6,
                end_lineno=59,
                end_col_offset=1),
            lineno=41,
            col_offset=0,
            end_lineno=59,
            end_col_offset=1),
        Assign(
            targets=[
                Name(
                    id='get_entities',
                    ctx=Store(),
                    lineno=60,
                    col_offset=0,
                    end_lineno=60,
                    end_col_offset=12)],
            value=Call(
                func=Name(
                    id='GvPostgresOperator',
                    ctx=Load(),
                    lineno=60,
                    col_offset=15,
                    end_lineno=60,
                    end_col_offset=33),
                args=[],
                keywords=[
                    keyword(
                        arg='dag',
                        value=Name(
                            id='dag',
                            ctx=Load(),
                            lineno=61,
                            col_offset=8,
                            end_lineno=61,
                            end_col_offset=11),
                        lineno=61,
                        col_offset=4,
                        end_lineno=61,
                        end_col_offset=11),
                    keyword(
                        arg='postgres_conn_id',
                        value=Constant(
                            value='postges_developer_hub_dev',
                            lineno=62,
                            col_offset=21,
                            end_lineno=62,
                            end_col_offset=48),
                        lineno=62,
                        col_offset=4,
                        end_lineno=62,
                        end_col_offset=48),
                    keyword(
                        arg='task_id',
                        value=Constant(
                            value='get_entities',
                            lineno=63,
                            col_offset=12,
                            end_lineno=63,
                            end_col_offset=26),
                        lineno=63,
                        col_offset=4,
                        end_lineno=63,
                        end_col_offset=26),
                    keyword(
                        arg='sql',
                        value=Constant(
                            value='SELECT entity_name,is_enabled FROM entities',
                            lineno=64,
                            col_offset=8,
                            end_lineno=64,
                            end_col_offset=53),
                        lineno=64,
                        col_offset=4,
                        end_lineno=64,
                        end_col_offset=53),
                    keyword(
                        arg='mode',
                        value=Constant(
                            value='read',
                            lineno=65,
                            col_offset=9,
                            end_lineno=65,
                            end_col_offset=15),
                        lineno=65,
                        col_offset=4,
                        end_lineno=65,
                        end_col_offset=15)],
                lineno=60,
                col_offset=15,
                end_lineno=66,
                end_col_offset=1),
            lineno=60,
            col_offset=0,
            end_lineno=66,
            end_col_offset=1),
        Assign(
            targets=[
                Name(
                    id='python_task',
                    ctx=Store(),
                    lineno=68,
                    col_offset=0,
                    end_lineno=68,
                    end_col_offset=11)],
            value=Call(
                func=Name(
                    id='PythonOperator',
                    ctx=Load(),
                    lineno=68,
                    col_offset=14,
                    end_lineno=68,
                    end_col_offset=28),
                args=[],
                keywords=[
                    keyword(
                        arg='dag',
                        value=Name(
                            id='dag',
                            ctx=Load(),
                            lineno=69,
                            col_offset=8,
                            end_lineno=69,
                            end_col_offset=11),
                        lineno=69,
                        col_offset=4,
                        end_lineno=69,
                        end_col_offset=11),
                    keyword(
                        arg='python_callable',
                        value=Name(
                            id='test_function',
                            ctx=Load(),
                            lineno=70,
                            col_offset=20,
                            end_lineno=70,
                            end_col_offset=33),
                        lineno=70,
                        col_offset=4,
                        end_lineno=70,
                        end_col_offset=33),
                    keyword(
                        arg='task_id',
                        value=Constant(
                            value='python_test_op',
                            lineno=71,
                            col_offset=12,
                            end_lineno=71,
                            end_col_offset=28),
                        lineno=71,
                        col_offset=4,
                        end_lineno=71,
                        end_col_offset=28)],
                lineno=68,
                col_offset=14,
                end_lineno=72,
                end_col_offset=1),
            lineno=68,
            col_offset=0,
            end_lineno=72,
            end_col_offset=1),
        Expr(
            value=BinOp(
                left=Name(
                    id='get_entities',
                    ctx=Load(),
                    lineno=74,
                    col_offset=0,
                    end_lineno=74,
                    end_col_offset=12),
                op=RShift(),
                right=Name(
                    id='python_task',
                    ctx=Load(),
                    lineno=74,
                    col_offset=16,
                    end_lineno=74,
                    end_col_offset=27),
                lineno=74,
                col_offset=0,
                end_lineno=74,
                end_col_offset=27),
            lineno=74,
            col_offset=0,
            end_lineno=74,
            end_col_offset=27)],
    type_ignores=[])
```

</details>