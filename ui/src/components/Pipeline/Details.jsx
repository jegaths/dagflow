import React from 'react'
import FloatingEditor from '../FloatingEditor';
import FloatingLabelInput from '../FloatingLabelInput';
import { pipelineState, selectedNodeState, isDetailsPaneOpenState, selectedTabState } from "./atoms"
import { useRecoilState, useRecoilValue } from "recoil";
import { FiChevronUp } from "react-icons/fi";

const Details = () => {
    const selectedNodeId = useRecoilValue(selectedNodeState);
    const [pipelineData, setPipelineData] = useRecoilState(pipelineState);
    const [isDetailsPaneOpen, setIsDetailsPaneOpen] = useRecoilState(isDetailsPaneOpenState);
    const [selectedTab, setSelectedTab] = useRecoilState(selectedTabState);

    const handlePipelineDetailsChange = (data, key) => {
        setPipelineData({
            ...pipelineData, [key]: data
        })
    }

    const handleOperatorDetailsChange = (data, key) => {
        setPipelineData({
            ...pipelineData, operators: {
                ...pipelineData.operators, [selectedNodeId]: {
                    ...pipelineData.operators[selectedNodeId], [key]: data
                }
            }
        })
    }

    const handleArgsChange = (data, key) => {
        setPipelineData(
            {
                ...pipelineData,
                operators: {
                    ...pipelineData.operators,
                    [selectedNodeId]: {
                        ...pipelineData.operators[selectedNodeId],
                        ["args"]: {
                            ...pipelineData.operators[selectedNodeId]["args"],
                            [key]: data
                        }
                    },
                },
            }
        )
    }

    const handleDetailsPaneClick = () => {
        if (selectedTab == 0 && isDetailsPaneOpen == false)
            setSelectedTab(1)
        setIsDetailsPaneOpen(!isDetailsPaneOpen)
    }

    const handleTabClick = (tabId) => {
        if (isDetailsPaneOpen == false)
            setIsDetailsPaneOpen(true)
        setSelectedTab(tabId)

    }

    return (
        <div className='absolute bottom-0 bg-secondary w-full'>
            <div className='flex px-10 flex-row justify-between items-center'>
                <div className='flex flex-row gap-4'>
                    <div className={`py-3 px-2 cursor-pointer ${isDetailsPaneOpen == true && selectedTab == 1 && "bg-primary text-white"}`} onClick={() => handleTabClick(1)}>General</div>
                    <div className={`py-3 px-2 cursor-pointer ${isDetailsPaneOpen == true && selectedTab == 2 && "bg-primary text-white"}`} onClick={() => handleTabClick(2)}>Node Details</div>
                </div>
                <FiChevronUp size={25} onClick={handleDetailsPaneClick} className={`cursor-pointer duration-300 ${isDetailsPaneOpen && "rotate-180"}`} />
            </div>
            <div className={`${isDetailsPaneOpen == true ? "h-80" : "h-0"} transition-height duration-300 ease-in-out`}>
                <div className={`bg-secondaryLight px-10 overflow-y-auto ${selectedTab == 1 ? "h-full" : "h-0 hidden"}`}>
                    <FloatingLabelInput label={"Pipeline Name"} arg_name="pipeline_name" className="mt-4 mb-4 text-primary" value={pipelineData.pipeline_name} onchange={handlePipelineDetailsChange} />
                    <FloatingEditor label={"Global"} arg_name={"global"} className="mb-6 text-primary" value={pipelineData.global} onchange={handlePipelineDetailsChange} height={"30vh"} />
                </div>
                <div className={`bg-secondaryLight px-10 overflow-y-auto ${selectedTab == 2 ? "h-full " : "h-0 hidden"}`}>
                    {selectedNodeId != undefined && pipelineData.operators[selectedNodeId] != undefined && (
                        <div className=''>
                            {/* <hr className='w-full bg-primary opacity-10 mb-3' /> */}
                            {Object.keys(pipelineData.operators[selectedNodeId]["args"]).map((arg, key) => {
                                return (
                                    <FloatingLabelInput key={key} label={arg} className="mt-4 mb-4 text-primary" value={pipelineData.operators[selectedNodeId]["args"][arg]} onchange={handleArgsChange} />
                                )
                            })}
                            <FloatingLabelInput arg_name={"description"} label={"Description"} className="mb-4 text-primary" value={pipelineData.operators[selectedNodeId]["description"]} onchange={handleOperatorDetailsChange} />
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}

export default Details;
