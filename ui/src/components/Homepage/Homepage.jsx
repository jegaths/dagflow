import React, { useRef, useEffect } from "react";
import { useSetRecoilState, useRecoilState } from "recoil";
import { initialNodesState, intialEdgesState, pipelineState, importStatementState } from "../Pipeline/atoms";
import { isCanvasEnabledState } from "../../atoms";
import { handleFileSelect, handleNewDagflow, getRecentPipelines, handleRecentPipelineClick } from "./utils";
import { recentPipelinesState } from "./atoms";

const Homepage = () => {
  const setInitialEdges = useSetRecoilState(intialEdgesState);
  const setInitialNodes = useSetRecoilState(initialNodesState);
  const setImportStatements = useSetRecoilState(importStatementState);
  const setPipelineData = useSetRecoilState(pipelineState);
  const setIsCanvasEnabled = useSetRecoilState(isCanvasEnabledState);
  const [recentPipelines, setRecentPipelines] = useRecoilState(recentPipelinesState);

  const inputFile = useRef(null);

  useEffect(() => {
    getRecentPipelines(setRecentPipelines);
  }, []);

  return (
    <div className="w-full relative flex items-center bg-white justify-around px-32">
      <div className="mt-4 flex flex-col gap-16 flex-grow">
        <div className="flex flex-col">
          <span className="text-6xl font-bold text-primary tracking-widest">dagflow</span>
          <span className="mt-8 text-3xl text-muted">
            Build complex workflows <span className="mt-2 text-3xl text-primary">easily & reliably</span>
          </span>
          <div className="flex gap-8">
            <input type="file" ref={inputFile} className="hidden" onChange={(e) => handleFileSelect(e, setInitialEdges, setInitialNodes, setImportStatements, setPipelineData, setIsCanvasEnabled)} />
            <button className="bg-spot text-white py-2 rounded-md px-4 mt-4" onClick={() => inputFile.current.click()}>
              Load Dag to dagflow pipeline
            </button>
            <button className="bg-primary text-white py-2 rounded-md px-4 mt-4" onClick={() => handleNewDagflow(setIsCanvasEnabled, setPipelineData)}>
              New Dagflow
            </button>
          </div>
        </div>
        <div className="flex flex-col">
          <div className="text-4xl text-primary mb-2">Recents</div>
          <ul className="inline-block">
            {recentPipelines.map((pipeline, index) => (
              <li key={index} className="mt-2 cursor-pointer text-xl" onClick={() => handleRecentPipelineClick(pipeline.pipeline_id, setInitialEdges, setInitialNodes, setImportStatements, setPipelineData, setIsCanvasEnabled)}>
                {pipeline.pipeline_name}
                {index !== recentPipelines.length - 1 && <hr className="mt-2 bg-primary opacity-10" />}
              </li>
            ))}
          </ul>
        </div>
      </div>
      <img className="w-[50rem] mx-auto" src="homepage_illustration2.png" alt="Image Description"></img>
    </div>
  );
};

export default Homepage;
