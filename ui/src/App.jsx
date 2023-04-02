import React from "react";
import Pipeline from "./components/Pipeline/Pipeline";
import Homepage from "./components/Homepage/Homepage";
import Sidebar from "./components/Sidebar/Sidebar";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer } from "react-toastify";

export default function App() {
  return (
    <>
      <ToastContainer />
      <div className="flex font-display justify-between">
        <Sidebar />

        <Homepage />

        {/* <Pipeline /> */}
      </div>
    </>
  );
}
