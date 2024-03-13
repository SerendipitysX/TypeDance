import axios from 'axios';

const T_URL = 'http://127.0.0.1:88';


export function startBrainStorm(param, callback) {
    const url = `${T_URL}/brainstorm`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function imageSegment(param, callback) {
    const url = `${T_URL}/image_segment`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function startImageExtract(param, callback) {
    const url = `${T_URL}/image_extract`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function startGenerate(param, callback) {
    const url = `${T_URL}/generate`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function startRetreiveInfo(param, callback) {
    const url = `${T_URL}/show_info`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function ConvertToSvg(param, callback) {
    const url = `${T_URL}/convert_to_svg`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function startEvaluate(param, callback) {
    const url = `${T_URL}/evaluate_element`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

export function startRefine(param, callback) {
    const url = `${T_URL}/refine_element`;
    axios.post(url, param)
    .then(response => {
        callback(response.data)
    }, errResponnse => {
        console.log(errResponnse);
    })
}

