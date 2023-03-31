import React, { useEffect } from "react";
import { AiOutlineNodeIndex } from "react-icons/ai";

import { nodeListState } from "./atoms";
import { useRecoilState } from "recoil";
import { BASE_URL } from '../../constants';
import OperatorNode from "./OperatorNode";

export const nodeTypes = { operator: OperatorNode };

const Nodes = () => {
    const [nodeList, setNodeList] = useRecoilState(nodeListState);

    useEffect(() => {
        fetch(`${BASE_URL}/operators`)
            .then((res) => res.json())
            .then((result) => {
                setNodeList(result);
            });
    }, []);

    const onDragStart = (event, nodeType, data) => {
        event.dataTransfer.setData("application/reactflow", nodeType);
        event.dataTransfer.effectAllowed = "move";
        event.dataTransfer.setData("id", data.id);
        event.dataTransfer.setData("data", JSON.stringify(data));
    };

    return (
        <div className="overflow-auto">
            <ul className="w-48 text-sm font-medium text-gray-900 bg-white"></ul>
            {nodeList.map((item) => (
                <li
                    key={item.id}
                    className="w-full px-4 py-2 border-b border-gray-200 rounded-t-lg dark:border-gray-600 list-none"
                >
                    <div
                        id={item.id}
                        onDragStart={(event) => onDragStart(event, item.node_type, item)}
                        draggable
                    >
                        <span className="font-medium flex justify-start items-center gap-2">
                            <AiOutlineNodeIndex /> {item.name}
                        </span>
                    </div>
                </li>
            ))}
        </div>
    );
};
export default Nodes;
