import { BASE_URL } from "../../constants";
import { TiFlowMerge } from "react-icons/ti";

export const handleLogoClick = (setIsCanvasEnabled, setInitialNodes, setInitialEdges, setImportStatements, setPipelineData) => {
  setInitialNodes([]);
  setInitialEdges([]);
  setImportStatements("from airflow import DAG\nfrom airflow.utils.dates import days_ago\nfrom datetime import timedelta");
  setPipelineData({
    pipeline_name: "",
    pipeline_id: "",
    global_statements: "",
    operators: {},
    react_flow_data: {},
    dag_statement: {},
  });
  setIsCanvasEnabled(false);
};

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
          isSelected: false,
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

export const handleSubmenuItemSelection = (index, subIndex, setMenuItems) => {
  // Set the state of submenu item with subIndex to true and rest to false
  setMenuItems((prevItems) => [
    {
      ...prevItems[index], // spread the properties of the first element
      subMenuItems: prevItems[index]["subMenuItems"].map((item, i) => {
        return { ...item, isSelected: i === subIndex };
      }),
    },
    ...prevItems.slice(1), // spread the remaining elements
  ]);
};
