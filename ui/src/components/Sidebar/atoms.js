import { atom } from "recoil";

export const toggleSidebarState = atom({
  key: "toggleSidebarState",
  default: false,
});

export const menuItemState = atom({
  key: "menuItemState",
  default: [],
});
