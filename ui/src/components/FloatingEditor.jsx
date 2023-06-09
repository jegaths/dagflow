/* eslint-disable react/prop-types */
import React from "react";
import Editor from "@monaco-editor/react";

// eslint-disable-next-line react/prop-types
const FloatingEditor = ({ label, onchange, arg_name = undefined, data = "", className = "", height = "20vh", required = false, language = "python" }) => {
    arg_name = arg_name == undefined ? label : arg_name;

    return (
        <div className={`relative ${className}`}>
            <Editor
                height={height}
                defaultLanguage={language}
                value={data}
                // eslint-disable-next-line no-unused-vars
                onChange={(value, _event) => onchange(value, arg_name)}
                options={{
                    minimap: {
                        enabled: false,
                    },
                    automaticLayout: true,
                    formatOnPaste: true,
                    formatOnType: true,
                }}
                className="block rounded-md pb-2.5 pt-8 w-full text-md peer focus:outline-none bg-white"
            />
            {required && (
                <label className="absolute text-md text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4">
                    {label} <span className="italic text-muted">({language})</span> <span className="text-error"> (requierd)</span>
                </label>
            )}
            {!required && <label className="absolute text-md text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4">{label} <span className="italic text-muted">({language})</span></label>}
        </div>
    );
};

export default FloatingEditor;
