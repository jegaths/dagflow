import React from "react";
// import Canvas from "./components/Canvas/Canvas";
import Pipeline from "./components/Pipeline/Pipeline";
import Details from "./components/Pipeline/Details";
import Sidebar from "./components/Sidebar/Sidebar"
import 'react-toastify/dist/ReactToastify.css';

export default function App() {
    return (
        <>
            <div className="flex font-display justify-between">
                <Sidebar />
                <Pipeline />
                {/* <Details /> */}
            </div>
        </>

    );
}
