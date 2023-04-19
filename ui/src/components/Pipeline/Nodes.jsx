import React, { useEffect } from "react";
import { AiOutlineNodeIndex } from "react-icons/ai";

import { nodeListState, nodesSearchState } from "./atoms";
import { useRecoilState } from "recoil";
import { BASE_URL } from "../../constants";
import OperatorNode from "./OperatorNode";
import { BiSearchAlt } from "react-icons/bi";

export const nodeTypes = { operator: OperatorNode };

const Nodes = () => {
  const [nodeList, setNodeList] = useRecoilState(nodeListState);
  const [searchTerm, setSearchTerm] = useRecoilState(nodesSearchState);

  useEffect(() => {
    fetch(`${BASE_URL}/dagflow/operators`)
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

  const filteredItems = nodeList.filter((item) => item.name.toLowerCase().includes(searchTerm.toLowerCase()));

  return (
    <div className="overflow-auto max-h-96">
      <div className="sticky top-0 z-10 flex items-center bg-secondary rounded-md p-2 mx-2 my-2">
        <BiSearchAlt className="text-primary mr-2" />
        <input type="text" placeholder="Search..." className="bg-transparent focus:outline-none bg-secondary text-primary" onChange={(e) => setSearchTerm(e.target.value)} />
      </div>
      <ul className="w-48 text-sm font-medium text-gray-900 bg-white"></ul>
      {filteredItems.map((item, index) => (
        <li key={index} className="w-full px-4 list-none">
          <div id={item.id} onDragStart={(event) => onDragStart(event, item.node_type, item)} draggable>
            <span className="font-medium flex justify-start items-center gap-2 py-2">
              <AiOutlineNodeIndex /> {item.name}
            </span>
            {index !== nodeList.length - 1 && <hr className="w-full bg-primary opacity-10" />}
          </div>
        </li>
      ))}
    </div>
  );
};
export default Nodes;
