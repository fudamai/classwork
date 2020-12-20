import axios from 'axios'


const HOST = 'http://127.0.0.1:8000/api/v1'

export default {
    login: payload => {
        // 用户登录
        return axios.post(`${HOST}/token/`, payload)
    },
    register: payload => {
        // 注册用户
        return axios.post(`${HOST}/users/`, payload)
    },
    getAll: () => {
        // 获取所有博客
        return axios.get(`${HOST}/blogs/`)
    },
    getBlogbyId: (payload) => {
        // 获取所有博客
        return axios.get(`${HOST}/blogs/${payload}/`)
    },
    getUser: () => {
        // 获取所有用户
        return axios.get(`${HOST}/users/`, {
            headers: {'Authorization': 'Bearer ' + localStorage.getItem('token')}
        })
    },
    addOne: (payload) => {
        // 创建
        return axios.post(`${HOST}/blogs/`, payload, {
            headers: {'Authorization': 'Bearer ' + localStorage.getItem('token'), 'Content-Type': 'multipart/form-data'}
        })
    },
    updateOne: (payload) => {
        // 更新
        return axios.put(`${HOST}/blogs/${payload.id}/`, payload.formdata, {
            headers: {'Authorization': 'Bearer ' + localStorage.getItem('token'), 'Content-Type': 'multipart/form-data'}
        })
    },
    deleteOne: (payload) => {
        // 删除
        return axios.delete(`${HOST}/blogs/${payload.id}/`, {
            headers: {'Authorization': 'Bearer ' + localStorage.getItem('token')}
        })
    },
    addComment: (payload) => {
        // 创建
        return axios.post(`${HOST}/comments/`, payload, {
            headers: {'Authorization': 'Bearer ' + localStorage.getItem('token')}
        })
    },
}