import { BASE_URL } from "../../constants";
import { v4 as uuidv4 } from "uuid";
import { toast } from "react-toastify";

export const handleFileSelect = (e, setInitialEdges, setInitialNodes, setImportStatements, setPipelineData, setIsCanvasEnabled) => {
  e.stopPropagation();
  e.preventDefault();
  var file = e.target.files[0];
  const formdata = new FormData();

  formdata.append("file", file, file.name);

  const requestOptions = {
    method: "POST",
    body: formdata,
  };

  const myPromise = new Promise((resolve, reject) =>
    fetch(`${BASE_URL}/dagflow/generate_flow`, requestOptions)
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
          global_statements: result.global_statements,
          pipeline_name: result.pipeline_name == "" ? "df_pipeline_" + uuidv4().replace(/-/g, "_") : result.pipeline_name,
          pipeline_id: result.pipeline_id,
        }));
        setIsCanvasEnabled(true);
      })
      .catch((err) => {
        console.log(err);
        reject();
      })
  );

  toast.promise(myPromise, {
    pending: "Generating Flow",
    success: "Flow generated successfully",
    error: "Some error occured!",
  });
};

export const handleNewDagflow = (setIsCanvasEnabled, setPipelineData) => {
  setIsCanvasEnabled(true);
  setPipelineData((prev) => ({
    ...prev,
    pipeline_name: "df_pipeline_" + uuidv4().replace(/-/g, "_"),
    pipeline_id: uuidv4(),
    dag_statement: { dag_variable_name: "dag", call: 'DAG(\n"my_dag_id",\ndefault_args={\n"owner": "Jegath S",\n"depends_on_past": True,\n"start_date": days_ago(1),\n"email": ["myemail.com"],\n"email_on_failure": False,\n"email_on_retry": False,\n"retries": 3,\n"retry_delay": timedelta(minutes=5),\n},\ndescription="Dagflow dag descroption",\nschedule_interval="0 0 * * *",\nconcurrency=10,\n)' },
  }));
};

export const getRecentPipelines = (setRecentPipelines) => {
  const requestOptions = {
    method: "GET",
  };

  fetch(`${BASE_URL}/dagflow/get_recent_pipeline_names/5`, requestOptions)
    .then((res) => res.json())
    .then((result) => {
      setRecentPipelines(result);
    })
    .catch((err) => {
      console.log(err);
    });
};

export const handleRecentPipelineClick = (pipelineId, setInitialEdges, setInitialNodes, setImportStatements, setPipelineData, setIsCanvasEnabled) => {
  setIsCanvasEnabled(false);
  const requestOptions = {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify({ pipeline_id: pipelineId }),
  };

  const myPromise = new Promise((resolve, reject) =>
    fetch(`${BASE_URL}/dagflow/get_pipeline`, requestOptions)
      .then((res) => res.json())
      .then((result) => {
        resolve(result);
        setPipelineData({
          operators: result.operators,
          dag_statement: result.dag_statement,
          global_statements: result.global_statements,
          pipeline_name: result.pipeline_name == "" ? "df_pipeline_" + uuidv4().replace(/-/g, "_") : result.pipeline_name,
          pipeline_id: result.pipeline_id,
        });
        setInitialEdges(result.react_flow_data.edges);
        setInitialNodes(result.react_flow_data.nodes);
        setImportStatements(result.import_statements);
        setIsCanvasEnabled(true);
      })
      .catch((err) => {
        console.log(err);
        reject();
      })
  );

  toast.promise(myPromise, {
    pending: "Loading pipeline",
    success: "Pipeline loaded successfully",
    error: "Some error occured!",
  });
};
