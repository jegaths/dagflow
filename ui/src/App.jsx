import React from "react";
import Pipeline from "./components/Pipeline/Pipeline";
import Homepage from "./components/Homepage/Homepage";
import Sidebar from "./components/Sidebar/Sidebar";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer } from "react-toastify";
import { useRecoilValue } from "recoil";
import { isCanvasEnabledState } from "./atoms";

export default function App() {
  const isCanvasEnabled = useRecoilValue(isCanvasEnabledState);
  return (
    <>
      <ToastContainer />
      <div className="flex font-display w-full">
        <Sidebar />
        {isCanvasEnabled ? <Pipeline /> : <Homepage />}
      </div>
    </>
  );
}
