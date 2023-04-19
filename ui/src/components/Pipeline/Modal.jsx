import React from "react";
import { AiOutlineWarning } from "react-icons/ai"; // Import the AiOutlineWarning icon from react-icons library

const DeletePipelineModal = ({ setCancel, setDone }) => {
  return (
    <div className="fixed z-10 inset-0 bg-black bg-opacity-25 backdrop-blur-sm backdrop-brightness-50 flex items-center justify-center">
      <div className="bg-white p-2 rounded w-96 py-5 px-5">
        <div className="flex items-center justify-center">
          <AiOutlineWarning className="text-red-500 text-5xl mr-4" />
          <h2 className="text-2xl font-semibold">Are you sure to delete this pipeline?</h2>
        </div>
        <p className="text-gray-600 mt-4 mb-8">This action cannot be undone. Please confirm if you want to delete this pipeline.</p>
        <div className="flex justify-around">
          <button className="bg-primary text-white px-4 py-2 rounded-md cursor-pointer" onClick={setDone}>
            Delete
          </button>
          <button className="bg-spot text-white px-4 py-2 rounded-md cursor-pointer" onClick={() => setCancel(false)}>
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};

export default DeletePipelineModal;
