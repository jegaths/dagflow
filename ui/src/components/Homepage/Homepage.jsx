import React, { useRef } from "react";
import { toast } from "react-toastify";
import { BASE_URL } from "../../constants";

import { useSetRecoilState } from "recoil";
import { initialNodesState, intialEdgesState, pipelineState, importStatementState } from "../Pipeline/atoms";
import { isCanvasEnabledState } from "../../atoms";

import { v4 as uuidv4 } from "uuid";

const Homepage = () => {
  const setInitialEdges = useSetRecoilState(intialEdgesState);
  const setInitialNodes = useSetRecoilState(initialNodesState);
  const setPipelineData = useSetRecoilState(pipelineState);
  const setIsCanvasEnabled = useSetRecoilState(isCanvasEnabledState);
  const setImportStatements = useSetRecoilState(importStatementState);

  const inputFile = useRef(null);

  const handleFileSelect = (e) => {
    e.stopPropagation();
    e.preventDefault();
    var file = e.target.files[0];
    const formdata = new FormData();

    formdata.append("file", file, file.name);

    const requestOptions = {
      method: "POST",
      body: formdata,
    };

    const myPromise = new Promise((resolve) =>
      fetch(`${BASE_URL}/generate_flow`, requestOptions)
        .then((res) => res.json())
        .then((result) => {
          resolve(result);
          setInitialEdges(result.react_flow_data.edges);
          setInitialNodes(result.react_flow_data.nodes);
          setImportStatements(result.import_statements);
          setPipelineData((prev) => ({
            ...prev,
            operators: result.operators,
            dag_statement: result.dag_statement,
            global: result.global,
            pipeline_name: result.pipeline_name == "" ? "df_pipeline_" + uuidv4().replace(/-/g, "_") : result.pipeline_name,
          }));
          setIsCanvasEnabled(true);
        })
    );

    toast.promise(myPromise, {
      pending: "Generating Flow",
      success: "Flow generated successfully",
      error: "Some error occured!",
    });
  };

  const handleNewDagflow = () => {
    setIsCanvasEnabled(true);
    setPipelineData((prev) => ({
      ...prev,
      pipeline_name: "df_pipeline_" + uuidv4().replace(/-/g, "_"),
      dag_statement: { dag_variable_name: "dag", call: 'DAG(\n"my_dag_id",\ndefault_args={\n"owner": "Jegath S",\n"depends_on_past": True,\n"start_date": days_ago(1),\n"email": ["myemail.com"],\n"email_on_failure": False,\n"email_on_retry": False,\n"retries": 3,\n"retry_delay": timedelta(minutes=5),\n},\ndescription="Dagflow dag descroption",\nschedule_interval="0 0 * * *",\nconcurrency=10,\n)' },
    }));
  };

  return (
    <div className="w-full relative flex items-center">
      <div className="mt-4 mx-10 w-full flex flex-col gap-6">
        <div className="flex flex-col">
          <span className="text-6xl font-bold text-primary tracking-widest">dagflow</span>
          <span className="mt-8 text-3xl text-muted">Build complex workflows</span>
          <span className="mt-2 text-3xl text-primary">easily & reliably</span>
          <span className="mt-8 text-2xl">Import your existing dag to dagflow</span>
          <div>
            <input type="file" ref={inputFile} className="hidden" onChange={handleFileSelect} />
            <button className="bg-spot text-white py-2 rounded-md px-4 mt-4" onClick={() => inputFile.current.click()}>
              Load Dag to dagflow pipeline
            </button>
          </div>
          <span className="mt-8 text-2xl">Create a new dag easily and reliably using dagflow</span>
          <div>
            <button className="bg-primary text-white py-2 rounded-md px-4 mt-4" onClick={handleNewDagflow}>
              New Dagflow
            </button>
          </div>
        </div>
      </div>
      <img className="w-auto mx-auto" src="homepage_illustration2.png" alt="Image Description"></img>
    </div>
  );
};

export default Homepage;
