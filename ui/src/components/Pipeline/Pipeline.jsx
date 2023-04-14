import React from "react";
import Canvas from "./Canvas";
import { pipelineState, reactFlowState, importStatementState, formRefState, refreshSidebarState } from "./atoms";
import { useRecoilValue, useSetRecoilState } from "recoil";
import { savePipeline, generate_dag } from "./utils";
import Details from "./Details";

// eslint-disable-next-line react/prop-types
const Pipeline = () => {
  const pipelineData = useRecoilValue(pipelineState);
  const rectFlowInstance = useRecoilValue(reactFlowState);
  const importStatement = useRecoilValue(importStatementState);
  const formRef = useRecoilValue(formRefState);
  const setRefreshSidebarState = useSetRecoilState(refreshSidebarState);
  return (
    <div className={`w-full relative flex`}>
      <div className="mt-4 mx-10 w-full flex flex-col gap-6">
        <div className="flex justify-between">
          <span className="text-4xl font-medium">{pipelineData.pipeline_name}</span>
          <div>
            <button className="bg-spot text-white px-4 py-2 rounded-md mr-8" onClick={() => savePipeline(pipelineData, rectFlowInstance, importStatement, formRef, setRefreshSidebarState)}>
              save
            </button>
            <button className="bg-primary text-white px-4 py-2 rounded-md" onClick={() => generate_dag(pipelineData, rectFlowInstance, importStatement, formRef)}>
              Generate dag
            </button>
          </div>
        </div>
        <Canvas />
      </div>
      <Details />
    </div>
  );
};

export default Pipeline;
