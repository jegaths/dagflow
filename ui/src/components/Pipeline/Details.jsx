import React, { useCallback, useRef, useEffect } from "react";
import FloatingEditor from "../FloatingEditor";
import FloatingLabelInput from "../FloatingLabelInput";
import { pipelineState, selectedNodeState, isDetailsPaneOpenState, selectedTabState, importStatementState, nodeListState, formRefState } from "./atoms";
import { useRecoilState, useRecoilValue, useSetRecoilState } from "recoil";
import { FiChevronUp } from "react-icons/fi";

const Details = () => {
  const selectedNodeId = useRecoilValue(selectedNodeState);
  const [pipelineData, setPipelineData] = useRecoilState(pipelineState);
  const [importStatement, setImportStatement] = useRecoilState(importStatementState);
  const [isDetailsPaneOpen, setIsDetailsPaneOpen] = useRecoilState(isDetailsPaneOpenState);
  const [selectedTab, setSelectedTab] = useRecoilState(selectedTabState);
  const nodeDetails = useRecoilValue(nodeListState);
  const setFormRef = useSetRecoilState(formRefState);
  const ref = useRef();

  useEffect(() => {
    setFormRef(ref.current);
  }, [ref]);

  const handlePipelineDetailsChange = (data, key) => {
    setPipelineData({
      ...pipelineData,
      [key]: data,
    });
  };

  const handleOperatorDetailsChange = (data, key) => {
    setPipelineData({
      ...pipelineData,
      operators: {
        ...pipelineData.operators,
        [selectedNodeId]: {
          ...pipelineData.operators[selectedNodeId],
          [key]: data,
        },
      },
    });
  };

  const handleArgsChange = (data, key) => {
    setPipelineData({
      ...pipelineData,
      operators: {
        ...pipelineData.operators,
        [selectedNodeId]: {
          ...pipelineData.operators[selectedNodeId],
          ["args"]: {
            ...pipelineData.operators[selectedNodeId]["args"],
            [key]: data,
          },
        },
      },
    });
  };

  const handleDetailsPaneClick = () => {
    if (selectedTab == 0 && isDetailsPaneOpen == false) setSelectedTab(1);
    setIsDetailsPaneOpen(!isDetailsPaneOpen);
  };

  const handleTabClick = (tabId) => {
    if (isDetailsPaneOpen == false) setIsDetailsPaneOpen(true);
    setSelectedTab(tabId);
  };

  const handleImportStatementChange = useCallback(
    // eslint-disable-next-line no-unused-vars
    (value, arg) => {
      setImportStatement(value);
    },
    [setImportStatement]
  );

  const handleDagDetailsChange = (data, key) => {
    setPipelineData({
      ...pipelineData,
      [key]: {
        ...pipelineData[key],
        ["call"]: data,
      },
    });
  };

  return (
    <div className="absolute bottom-0 bg-secondary w-full">
      <div className="flex px-10 flex-row justify-between items-center">
        <div className="flex flex-row gap-4">
          <div className={`py-3 px-2 cursor-pointer ${isDetailsPaneOpen == true && selectedTab == 1 && "bg-primary text-white"}`} onClick={() => handleTabClick(1)}>
            General
          </div>
          <div className={`py-3 px-2 cursor-pointer ${isDetailsPaneOpen == true && selectedTab == 2 && "bg-primary text-white"}`} onClick={() => handleTabClick(2)}>
            Node Details
          </div>
          <div className={`py-3 px-2 cursor-pointer ${isDetailsPaneOpen == true && selectedTab == 3 && "bg-primary text-white"}`} onClick={() => handleTabClick(3)}>
            Dag Details
          </div>
          <div className={`py-3 px-2 cursor-pointer ${isDetailsPaneOpen == true && selectedTab == 4 && "bg-primary text-white"}`} onClick={() => handleTabClick(4)}>
            Imports
          </div>
        </div>
        <FiChevronUp size={25} onClick={handleDetailsPaneClick} className={`cursor-pointer duration-300 ${isDetailsPaneOpen && "rotate-180"}`} />
      </div>
      <form ref={ref}>
        <div className={`${isDetailsPaneOpen == true ? "h-80" : "h-0"} transition-height duration-300 ease-in-out`}>
          <div className={`bg-secondaryLight px-10 overflow-y-auto ${selectedTab == 1 ? "h-full" : "h-0 hidden"}`}>
            <FloatingLabelInput label={"Pipeline Name"} arg_name="pipeline_name" className="mt-4 mb-4 text-primary" value={pipelineData.pipeline_name} onchange={handlePipelineDetailsChange} required={true} />
            <FloatingEditor label={"Global"} arg_name={"global_statements"} className="mb-6 text-primary" data={pipelineData.global_statements} onchange={handlePipelineDetailsChange} height={"30vh"} />
          </div>

          <div className={`bg-secondaryLight px-10 overflow-y-auto ${selectedTab == 3 ? "h-full" : "h-0 hidden"}`}>
            <FloatingEditor label={"Dag Details"} arg_name={"dag_statement"} className="mb-6 text-primary dag-statement-input" data={pipelineData.dag_statement.call} onchange={handleDagDetailsChange} height={"30vh"} required={true} />
          </div>
          <div className={`bg-secondaryLight px-10 overflow-y-auto ${selectedTab == 4 ? "h-full" : "h-0 hidden"}`}>
            <FloatingEditor label={"Imports"} arg_name={"import_statements"} className="mb-6 text-primary" data={importStatement} onchange={handleImportStatementChange} height={"30vh"} />
          </div>
          <div className={`bg-secondaryLight px-10 overflow-y-auto ${selectedTab == 2 ? "h-full " : "h-0 hidden"}`}>
            {selectedNodeId != undefined && pipelineData.operators[selectedNodeId] != undefined && (
              <div className="">
                {Object.keys(pipelineData.operators[selectedNodeId]["args"]).map((arg, key) => {
                  let isRequierd = false;
                  let datatype = "string";
                  const item = nodeDetails.find((obj) => obj.name == pipelineData.operators[selectedNodeId]["name"]);
                  if (item != undefined && item["args"][arg] != undefined) {
                    isRequierd = item["args"][arg]["required"];
                    datatype = item["args"][arg]["data_type"];
                  }
                  return <FloatingLabelInput key={key} label={arg} className="mt-4 mb-4 text-primary" value={pipelineData.operators[selectedNodeId]["args"][arg]} onchange={handleArgsChange} required={isRequierd} type={datatype == "int" ? "number" : "text"} />;
                })}

                <FloatingLabelInput arg_name={"description"} label={"Description"} className="mb-4 text-primary" value={pipelineData.operators[selectedNodeId]["description"]} onchange={handleOperatorDetailsChange} />
              </div>
            )}
          </div>
        </div>
      </form>
    </div>
  );
};

export default Details;
