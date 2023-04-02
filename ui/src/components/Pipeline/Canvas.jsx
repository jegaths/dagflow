import React, { useRef, useCallback } from "react";
import ReactFlow, { ReactFlowProvider, addEdge, useNodesState, useEdgesState, Controls, Background, ControlButton, Panel } from "reactflow";

import { AiFillDelete } from "react-icons/ai";

import "reactflow/dist/style.css";

import Nodes, { nodeTypes } from "./Nodes";

import { useRecoilState, useSetRecoilState, useRecoilValue } from "recoil";
import { pipelineState, selectedNodeState, reactFlowState, importStatementState, initialNodesState, intialEdgesState } from "./atoms";

// TODO:Remove initialNodes and initialEdges after testing and make it an empty array

let id = 0;
const getId = () => `${id++}`;

const Canvas = () => {
  const reactFlowWrapper = useRef(null);
  const initialEdges = useRecoilValue(intialEdgesState);
  const initialNodes = useRecoilValue(initialNodesState);
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const [reactFlowInstance, setReactFlowInstance] = useRecoilState(reactFlowState);
  const setSelectedNodeId = useSetRecoilState(selectedNodeState);
  const [importStatement, setImportStatement] = useRecoilState(importStatementState);
  const [pipelineData, setPipelineData] = useRecoilState(pipelineState);
  const onConnect = useCallback((params) => {
    // Make the edges animated
    params["animated"] = true;
    setEdges((eds) => addEdge(params, eds)), [];
  });

  const onDragOver = useCallback((event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = "move";
  }, []);

  // eslint-disable-next-line no-unused-vars
  const setSelectionChange = useCallback(({ nodes, edges }) => {
    if (nodes[0] != undefined) {
      setSelectedNodeId(nodes[0].id);
    }
  });

  const onNodeDelete = useCallback((nodes) => {
    const updatedPipelineData = { ...pipelineData.operators };
    delete updatedPipelineData[nodes[0].id];
    setPipelineData({
      ...pipelineData,
      operators: updatedPipelineData,
    });
  });

  const onDrop = useCallback((event) => {
    event.preventDefault();

    const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();
    const type = event.dataTransfer.getData("application/reactflow");
    const node_id = event.dataTransfer.getData("id");
    const data = event.dataTransfer.getData("data");

    // check if the dropped element is valid
    if (typeof type === "undefined" || !type) {
      return;
    }

    const position = reactFlowInstance.project({
      x: event.clientX - reactFlowBounds.left,
      y: event.clientY - reactFlowBounds.top,
    });
    let parsedData = JSON.parse(data);
    const id = `${parsedData.name}_${node_id}_${getId()}`;
    const newNode = {
      id: id,
      type,
      position,
      data: id,
    };

    setNodes((nds) => nds.concat(newNode));

    // On drop, add new node to pipeline.operators
    // setPipelineData
    let args = {};
    Object.keys(parsedData.args).map((key) => {
      if (key == "task_id") args["task_id"] = id;
      //TODO: Remove this else if after testing
      else if (key == "python_callable") args["python_callable"] = "test";
      else args[key] = parsedData.args[key].default_argument;
    });

    const operatorDetails = {
      name: `${parsedData.name}`,
      import_path: parsedData.import_path,
      args: args,
      description: "Description about this node.",
    };
    setPipelineData({
      ...pipelineData,
      operators: {
        ...pipelineData.operators,
        [id]: operatorDetails,
      },
    });

    const importStament = `from ${parsedData.import_path} import ${parsedData.name}`;

    if (!importStatement.includes(importStament)) {
      setImportStatement((oldString) => `${oldString}\n${importStament}`);
    }

    setSelectedNodeId(id);
  });

  return (
    <div className="flex flex-col w-full">
      <div className="flex flex-row">
        <ReactFlowProvider>
          <div className="reactflow-wrapper w-full h-full" style={{ height: "82vh", width: "100%" }} ref={reactFlowWrapper}>
            <ReactFlow onNodesDelete={onNodeDelete} nodes={nodes} edges={edges} onNodesChange={onNodesChange} onEdgesChange={onEdgesChange} onConnect={onConnect} onInit={setReactFlowInstance} onDrop={onDrop} onDragOver={onDragOver} nodeTypes={nodeTypes} onSelectionChange={(nodes, edges) => setSelectionChange(nodes, edges)} selectNodesOnDrag fitView>
              <Background className="bg-secondaryLight" variant="dots" size={3} gap={40} />
              <Controls showInteractive={false} position="top-right">
                <ControlButton>
                  <AiFillDelete />
                </ControlButton>
              </Controls>
              <Panel position="top-left" className="bg-white">
                <Nodes />
              </Panel>
            </ReactFlow>
          </div>
        </ReactFlowProvider>
      </div>
    </div>
  );
};

export default Canvas;
