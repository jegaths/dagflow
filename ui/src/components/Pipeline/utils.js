import { BASE_URL } from '../../constants'
import { toast } from 'react-toastify';


const isInputsValid = (formRef,pipelineData) => {
    const form = formRef.current;
    let isValid = true
    form.querySelectorAll("input[required]").forEach((input) => {
        if(input.value.trim() === ""){
            input.classList.add("border")
            input.classList.add("border-error")
            isValid = false
        }
        else{
            input.classList.remove("border")
            input.classList.add("border-error")
        }
        })

        if(pipelineData["dag_statement"]["call"] === ""){
            form.querySelectorAll(".dag-statement-input")[0].classList.add("border")
            form.querySelectorAll(".dag-statement-input")[0].classList.add("border-error")
            isValid = false
        }else{
            form.querySelectorAll(".dag-statement-input")[0].classList.remove("border")
            form.querySelectorAll(".dag-statement-input")[0].classList.remove("border-error")
        }
    return isValid
}

export const savePipeline = (pipelineData, reactFlowInstance,importStatement,formRef) => {

    const isValid = isInputsValid(formRef,pipelineData)

    if(!isValid)
        toast.warn("All the requierd fields are not filled!")

    const _pipelineData = {...pipelineData}
    _pipelineData["react_flow_data"] = reactFlowInstance.toObject()
    _pipelineData["import_statements"] = importStatement
    toast.success("Pipeline saved successfully")

}

export const generate_dag = (pipelineData, reactFlowInstance,importStatement,formRef) => {

    const isValid = isInputsValid(formRef,pipelineData)

    const _pipelineData = {...pipelineData}
    _pipelineData["react_flow_data"] = reactFlowInstance.toObject()
    _pipelineData["import_statements"] = importStatement

    if(!isValid){
        toast.error("Please fill all the required fields")
        return
    }

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