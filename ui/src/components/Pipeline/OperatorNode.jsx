/* eslint-disable react/no-unknown-property */
/* eslint-disable react/react-in-jsx-scope */
/* eslint-disable react/prop-types */
import { Handle, Position } from "reactflow";
import { FiGitCommit } from "react-icons/fi";
import { pipelineState, selectedNodeState } from "./atoms"
import { useRecoilValue } from "recoil"

export default function OperatorNode({ data, isConnectable }) {
    const pipelineData = useRecoilValue(pipelineState);
    const selectedNodeId = useRecoilValue(selectedNodeState);

    let node_style = "bg-white text-black"
    let header_style = "text-primary"
    if (selectedNodeId == data) {
        node_style = "bg-primary text-white"
        header_style = "text-white"
    }
    return (
        <div className="operator">
            <Handle
                type="target"
                id="a"
                position={Position.Left}
                isConnectable={isConnectable}
            />
            <div className={`${node_style} px-3 py-2 rounded-md shadow-lg`}>
                <div className={`${header_style} text-xl flex items-center gap-2`}>
                    <FiGitCommit />
                    <div>
                        {pipelineData.operators[data] != undefined && pipelineData.operators[data]["args"]["task_id"]}
                        {/* {pipelineData.operators[data]["args"]["task_id"]} */}
                    </div>
                </div>
                {pipelineData.operators[data] != undefined && <div className="text-[0.5rem] mb-1 text-muted">{pipelineData.operators[data]["name"]}</div>}
                {/* <div className="text-[0.5rem] mb-1 text-muted">{pipelineData.operators[data]["name"]}</div> */}
                <hr className='w-full bg-primary opacity-10 mb-2' />
                {pipelineData.operators[data] != undefined && <div className="text-[0.7rem] font-light mb- break-normal w-[15rem]">{pipelineData.operators[data]["description"]}</div>}
                {/* <div className="text-[0.7rem] font-light mb- break-normal w-[15rem]">{pipelineData.operators[data]["description"]}</div> */}
            </div>
            <Handle
                type="source"
                position={Position.Right}
                id="a"
                isConnectable={isConnectable}
            />
        </div>
    );
}
