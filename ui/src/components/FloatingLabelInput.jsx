import React from "react";

// eslint-disable-next-line react/prop-types
const FloatingLabelInput = ({ label, onchange, arg_name = undefined, value = "", className = "", type = "text", required = false }) => {
  arg_name = arg_name == undefined ? label : arg_name;
  return (
    <div className={`relative ${className} break-normal`}>
      <input type={type} className="block rounded-md px-2.5 pb-2.5 pt-5 w-full text-md peer focus:outline-none bg-white" placeholder=" " required={required} value={value} onChange={(e) => onchange(e.target.value, arg_name)} />
      <label className="absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-4 scale-75 top-4 z-10 origin-[0] left-2.5 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-4">{label}</label>
    </div>
  );
};

export default FloatingLabelInput;
