import { atom } from "recoil";
import { TiFlowMerge } from "react-icons/ti";
import { IoSettingsOutline } from "react-icons/io5";

export const toggleSidebarState = atom({
    key: "toggleSidebarState",
    default: true,
})

export const menuItemState = atom({
    key: "menuItemState",
    default: [
        {
            title: "Projects",
            icon: TiFlowMerge,
            isSelected: true,
            haveSubmenu: true,
            subMenuItems: [
                { title: "first pipeline", isSelected: true },
                { title: "second pipeline", isSelected: false }
            ]
        },
        {
            title: "Settings",
            icon: IoSettingsOutline,
            isSelected: false
        }
    ],
})