import { BASE_URL } from "../../constants";
import { TiFlowMerge } from "react-icons/ti";

export const getSidebarData = (setMenuItems) => {
  const requestOptions = {
    method: "GET",
  };

  fetch(`${BASE_URL}/dagflow/get_recent_pipeline_names/0`, requestOptions)
    .then((res) => res.json())
    .then((result) => {
      const subMenuItems = result.map((item) => {
        return { title: item.pipeline_name, isSelected: false, id: item.pipeline_id };
      });
      setMenuItems([
        {
          title: "Pipelines",
          icon: TiFlowMerge,
          isSelected: true,
          haveSubmenu: true,
          subMenuItems: subMenuItems,
        },
      ]);
    })
    .catch((err) => {
      console.log(err);
    });
};

export const handleExpandMainmenuItem = (index, setMenuItems) => {
  setMenuItems((prevItems) => [
    {
      ...prevItems[index], // spread the properties of the first element
      isSelected: !prevItems[index]["isSelected"], // update the isSelected property
    },
    ...prevItems.slice(1), // spread the remaining elements
  ]);
};
