import { BASE_URL } from '../../constants'
import { toast } from 'react-toastify';


export const savePipeline = (pipelineData, reactFlowInstance,importStatement) => {
    const _pipelineData = {...pipelineData}
    _pipelineData["react_flow_data"] = reactFlowInstance.toObject()
    _pipelineData["import_statements"] = importStatement
    console.log(_pipelineData)
    toast.success("Pipeline saved successfully")

}

export const generate_dag = (pipelineData, reactFlowInstance,importStatement) => {

    const _pipelineData = {...pipelineData}
    _pipelineData["react_flow_data"] = reactFlowInstance.toObject()
    _pipelineData["import_statements"] = importStatement


    const requestOptions = {
        method: 'POST',
        headers: { "Content-type": "application/json" },
        body: JSON.stringify({ "data": _pipelineData })
    };

    const myPromise = new Promise((resolve) =>
        fetch(`${BASE_URL}/generate_dag`, requestOptions)
            .then((res) => res.json())
            .then((result) => {
                resolve(result)
                console.log(result)
            })
    );

    toast.promise(myPromise, {
        pending: "Generating Dag",
        success: "Dag generated successfully",
        error: "Some error occured!"
    });
}