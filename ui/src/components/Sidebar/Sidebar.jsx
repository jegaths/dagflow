import React from 'react'
import { useRecoilValue, useRecoilState } from "recoil";
import { menuItemState, toggleSidebarState } from "./atoms";
import { FiChevronDown } from "react-icons/fi";
import { FaCircle } from "react-icons/fa";
import { BiCollapseHorizontal } from "react-icons/bi";

const Sidebar = () => {
    const menuItems = useRecoilValue(menuItemState);
    const [toggleSidebar, setToggleSidebar] = useRecoilState(toggleSidebarState);

    return (
        <div className={`min-h-screen flex flex-col ${toggleSidebar ? "w-96" : "w-20"} bg-primary transition-height duration-300 ease-in-out`}>
            <div className='flex flex-col justify-between mt-6 pb-5 px-3'>
                {toggleSidebar && (
                    <div className="logo text-3xl px-3 font-bold text-secondary">
                        dagflow
                    </div>
                )}
                {!toggleSidebar && (
                    <div className='text-primary text-4xl font-bold self-center bg-secondary px-4 py-1 rounded-lg'>d</div>
                )}
            </div>
            <div className='flex flex-col justify-between flex-grow'>
                <ul className='mt-4'>
                    {menuItems.map((item, index) => {
                        return (
                            <div key={index} >
                                <li className={`mb-2 text-xl cursor-pointer ${!toggleSidebar && "flex justify-center"}`}>
                                    <div className={`text-white rounded-md ${toggleSidebar ? "flex items-center justify-between py-3 px-2 mx-3" : "p-4"} ${item.isSelected && "bg-menuItem"}`}>
                                        {toggleSidebar &&
                                            <div className='flex gap-3 items-center'>
                                                <item.icon />
                                                {item.title}
                                            </div>
                                        }
                                        {toggleSidebar && item.haveSubmenu && <FiChevronDown />}
                                        {!toggleSidebar && <span><item.icon /></span>}
                                    </div>
                                </li>
                                {toggleSidebar && item.haveSubmenu && (
                                    <ul className=''>
                                        {item.subMenuItems.map((subItem, subIndex) => {
                                            return (
                                                <li key={subIndex} className={`flex gap-2 items-center pl-12 mb-2 rounded-md py-3 px-2 mx-3 ${subItem.isSelected ? " text-white" : "text-muted"} `}>
                                                    {subItem.isSelected && <FaCircle className='text-white' size="0.5rem" />}
                                                    {subItem.title}
                                                </li>
                                            )
                                        })}
                                    </ul>
                                )}
                            </div>
                        )
                    })}
                </ul >
                <BiCollapseHorizontal className='self-center cursor-pointer text-white mr-2 mb-2' size={30} onClick={() => setToggleSidebar(!toggleSidebar)} />
            </div>
        </div >
    )
}

export default Sidebar


