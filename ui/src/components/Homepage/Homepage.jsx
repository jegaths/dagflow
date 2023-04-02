import React, { useRef } from "react";
import { toast } from "react-toastify";
import { BASE_URL } from "../../constants";

import { useSetRecoilState } from "recoil";
import { initialNodesState, intialEdgesState, pipelineState } from "../Pipeline/atoms";

const Homepage = () => {
  const setInitialEdges = useSetRecoilState(intialEdgesState);
  const setInitialNodes = useSetRecoilState(initialNodesState);
  const setPipelineData = useSetRecoilState(pipelineState);

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
          console.log(result);
          setInitialEdges(result.react_flow_data.edges);
          setInitialNodes(result.react_flow_data.nodes);
          setPipelineData((prev) => ({
            ...prev,
            operators: result.operators,
            dag_statement: result.dag_statement,
            pipeline_name: "",
          }));
        })
    );

    toast.promise(myPromise, {
      pending: "Generating Flow",
      success: "Flow generated successfully",
      error: "Some error occured!",
    });
  };
  return (
    <div className="w-full relative flex">
      <div className="mt-4 mx-10 w-full flex flex-col gap-6">
        <div className="flex justify-between">
          <span className="text-4xl font-medium">Home</span>
          <div>
            <input type="file" ref={inputFile} className="hidden" onChange={handleFileSelect} />
            <button className="bg-spot text-white px-4 py-2 rounded-md mr-8" onClick={() => inputFile.current.click()}>
              Load Dag to Dagflow
            </button>
            <button className="bg-primary text-white px-4 py-2 rounded-md">New Pipeline</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Homepage;
