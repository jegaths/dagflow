import { BASE_URL } from '../../constants'
import { toast } from 'react-toastify';

const deepCopyAndExtend = ({ data, extra_data, extra_data_key }) => {
    let _data = JSON.parse(JSON.stringify(data))
    _data[extra_data_key] = extra_data
    return _data;
}

export const savePipeline = (pipelineData, reactFlowInstance) => {
    // Deep copying pipelineData since it is not extensible
    console.log(deepCopyAndExtend({
        data: pipelineData,
        extra_data: reactFlowInstance.toObject(),
        extra_data_key: "react_flow_data"
    }))
    toast.success("Pipeline saved successfully")

}

export const generate_dag = (pipelineData, reactFlowInstance) => {
    const _pipelineData = deepCopyAndExtend({
        data: pipelineData,
        extra_data: reactFlowInstance.toObject(),
        extra_data_key: "react_flow_data"
    })

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