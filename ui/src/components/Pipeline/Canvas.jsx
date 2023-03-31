import React, { useRef, useCallback } from "react";
import ReactFlow, {
    ReactFlowProvider,
    addEdge,
    useNodesState,
    useEdgesState,
    Controls,
    Background,
    ControlButton,
    Panel,
} from "reactflow";

import { AiFillDelete } from "react-icons/ai";

import "reactflow/dist/style.css";

import Nodes, { nodeTypes } from "./Nodes";

import { useRecoilState, useSetRecoilState } from "recoil";
import { pipelineState, selectedNodeState, reactFlowState } from "./atoms";

// TODO:Remove initialNodes and initialEdges after testing and make it an empty array
let initialNodes = [
    {
        data: "PythonOperator_1_0",
        dragging: false,
        id: "PythonOperator_1_0",
        position: { x: 153.203125, y: -4.5 },
        positionAbsolute: { x: 153.203125, y: -4.5 },
        selected: false,
        type: "pythonOperator",
        width: 264,
        height: 86
    },
    {
        data: "PythonOperator_1_1",
        dragging: false,
        id: "PythonOperator_1_1",
        position: { x: 170.3046875, y: 155.75 },
        positionAbsolute: { x: 170.3046875, y: 155.75 },
        selected: true,
        type: "pythonOperator",
        width: 264,
        height: 86
    },
    {
        data: "PythonOperator_1_2",
        dragging: false,
        id: "PythonOperator_1_2",
        position: { x: 180.8046875, y: 250.25 },
        positionAbsolute: { x: 180.8046875, y: 250.25 },
        selected: false,
        type: "pythonOperator",
        width: 264,
        height: 86
    }

];

let initialEdges = [
    {
        animated: true,
        id: "reactflow__edge-PythonOperator_1_0a-PythonOperator_1_1a",
        source: "PythonOperator_1_0",
        sourceHandle: "a",
        targetHandle: "a",
        target: "PythonOperator_1_1"
    },
    {
        animated: true,
        id: "reactflow__edge-PythonOperator_1_1a-PythonOperator_1_2a",
        source: "PythonOperator_1_1",
        sourceHandle: "a",
        targetHandle: "a",
        target: "PythonOperator_1_2"
    }
];

initialNodes = []
initialEdges = []

let id = 0;
const getId = () => `${id++}`;

const Canvas = () => {
    const reactFlowWrapper = useRef(null);
    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
    const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
    const [reactFlowInstance, setReactFlowInstance] = useRecoilState(reactFlowState);
    const setSelectedNodeId = useSetRecoilState(selectedNodeState);
    const [pipelineData, setPipelineData] = useRecoilState(pipelineState);
    const onConnect = useCallback(
        (params) => {
            // Make the edges animated
            params["animated"] = true
            setEdges((eds) => addEdge(params, eds)), []
        }

    );

    const onDragOver = useCallback((event) => {
        event.preventDefault();
        event.dataTransfer.dropEffect = "move";
    }, []);

    // eslint-disable-next-line no-unused-vars
    const setSelectionChange = useCallback(({ nodes, edges }) => {
        if (nodes[0] != undefined) {
            setSelectedNodeId(nodes[0].id)
        }
    })

    const onNodeDelete = useCallback((nodes) => {
        const updatedPipelineData = { ...pipelineData.operators };
        delete updatedPipelineData[nodes[0].id]
        setPipelineData({
            ...pipelineData, operators: updatedPipelineData
        })
    })

    const onDrop = useCallback(
        (event, _pipelineData, _setPipelineData, _setSelectedNodeId) => {
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
            let parsedData = JSON.parse(data)
            const id = `${parsedData.name}_${node_id}_${getId()}`
            const newNode = {
                id: id,
                type,
                position,
                data: id,
            };

            setNodes((nds) => nds.concat(newNode));

            // On drop, add new node to pipeline.operators
            // setPipelineData
            let args = {}
            Object.keys(parsedData.args).map(key => {
                if (key == "task_id")
                    args["task_id"] = id;
                //TODO: Remove this else if after testing
                else if (key == "python_callable")
                    args["python_callable"] = "test"
                else
                    args[key] = parsedData.args[key].default_argument;

            })

            const operatorDetails = {
                name: `${parsedData.name}`,
                import_path: parsedData.import_path,
                args: args,
                description: "Description about this node."
            }
            _setPipelineData({
                ..._pipelineData,
                operators: {
                    ..._pipelineData.operators,
                    [id]: operatorDetails,
                },
            })
            _setSelectedNodeId(id)

        },
        [reactFlowInstance]
    );


    return (
        <div className="flex flex-col w-full">
            <div className="flex flex-row">
                <ReactFlowProvider>
                    <div
                        className="reactflow-wrapper w-full h-full"
                        style={{ height: "82vh", width: "100%" }}
                        ref={reactFlowWrapper}
                    >
                        <ReactFlow
                            onNodesDelete={onNodeDelete}
                            nodes={nodes}
                            edges={edges}
                            onNodesChange={onNodesChange}
                            onEdgesChange={onEdgesChange}
                            onConnect={onConnect}
                            onInit={setReactFlowInstance}
                            onDrop={(event) => onDrop(event, pipelineData, setPipelineData, setSelectedNodeId)}
                            onDragOver={onDragOver}
                            nodeTypes={nodeTypes}
                            onSelectionChange={(nodes, edges) => setSelectionChange(nodes, edges)}
                            selectNodesOnDrag
                            fitView
                        >
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
