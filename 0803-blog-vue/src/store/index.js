import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

import router from '@/router'
import api from '../api/index.js'


Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    // 放置需要的参数
    blogs: [],
    nextPage: 0,
    filterBlogs: [],
    blogById: '',
    username: '',
    isLogin: false,
    tagLog: [],
    authMessage: '',
    isResgiterDone: true,
  },
  getters: {
    // 用于子组件映射
    blogs: (state) => {
      return state.blogs
    },
    blogById: (state) => {
      return state.blogById
    },
    nextPage: (state) => {
      return state.nextPage
    },
    filterBlogs: (state) => {
      return state.filterBlogs
    },
    username: (state) => {
      return state.username
    },
    isLogin: (state) => {
      return state.isLogin
    },
    tagLog: (state) => {
      return state.tagLog
    },
    authMessage: (state) => {
      return state.authMessage
    },
    isResgiterDone: (state) => {
      return state.isResgiterDone
    },
  },
  mutations: {
    autologin (state) {
      var msg = JSON.parse(localStorage.getItem('refresh_token'));
      if (msg) {
      // 如果没有refresh_token，不执行登录操作
      Vue.axios.post('http://127.0.0.1:8000/api/v1/token/refresh/', {refresh: msg.token})
      .then(response => {
        // console.log(response);
        localStorage.setItem('token', response.data.access);
        state.isLogin = true;
        state.username = msg.username;
      })
      .catch(error => {
        console.log(error);
      })
      }
    },
    login(state, payload) {
      api.login(payload)
      .then(response => {
        console.log(response);
        localStorage.setItem('token', response.data.access);
        var msg = {'token':response.data.refresh, 'username':payload.username};
        localStorage.setItem('refresh_token', JSON.stringify(msg));
        state.isLogin = true;
        state.username = payload.username;
        router.push({name: 'Home'})
      })
      .catch(error => {
        console.log(error);
        state.authMessage = "用户信息不匹配"
      })
    },
    logout(state) {
      // 退出
      localStorage.removeItem('token');
      localStorage.removeItem('refresh_token');
      state.isLogin = false;
      state.username = "";
      // router.push({name: 'Home'});

    },
    // 处理state 传入的值
    getBlogs(state) {
      api.getAll()
      .then(response => {
        state.blogs = response.data;
        state.filterBlogs= [];
        // console.log(response.data);
        for (let blog of state.blogs) {          
          blog.tags = JSON.parse(blog.tags)
          // console.log(blog.tags);
          for (let tag of blog.tags) {
            if (!state.tagLog.includes(tag)){
              state.tagLog.push(tag)
            }
          }
        }        
      })
      .catch(error => {
        console.log(error);
      })
    },
    getBlogbyId(state, payload){
      api.getBlogbyId(payload)
      .then(response => {
        // console.log(response);
        state.blogById = response.data
        state.blogById.tags = JSON.parse(state.blogById.tags)
        const comlist = []
        for (let u of state.blogById.blog_comment) {
          // console.log(u);
          axios
            .get(u)
            .then((response) => {
              comlist.push(response.data)
            })
            .catch((error) => {
              console.log(error);
            });
          // return comment;
        }
        state.blogById.blog_comment = comlist

      })
      .catch(error => {
        console.log(error);
        state.blogById = '404'
      })
    },
    getFilterBlogs(state, payload) {
      state.filterBlogs = state.blogs.filter(b => {
        // console.log(b.tags);
        return b.title.includes(payload.keywords)  || b.content.includes(payload.keywords) || b.tags.includes(payload.keywords)
      })
    },
    getFilterBlogsByTag(state, payload) {
      state.filterBlogs = state.blogs.filter(b => {
        // console.log(b.tags);
        // console.log(payload);
        return b.tags.includes(payload.tag)
      })
    },
    addComment(state, payload) {
      var d = new Date();
      api.addComment(payload)
      .then(
        state.blogById.blog_comment.unshift({'owner':state.username, 'content':payload.content, 'created':d.toLocaleString('zh-CN')})
        )
      // .then(response => {
      //   console.log(response);
      //   state.blogById.blog_comment.unshift({'owner':state.username, 'content':payload.content})
      // })
      .catch(error => {
        console.log(error);
      })
    },
    addBlog(state, payload) {
      console.log(payload);
      api.addOne(payload)
      .then(response => {
        console.log(response);
        router.push({name: 'Home'})
        // 添加成功，显示成功提示
      })
      .catch(error => {
        console.log(error);
      });
    },
    deleteBlog(state, payload) {
      const delete_id = payload.id;
      api.deleteOne(payload)
      .then(response => {
        console.log('删除成功',response);
        window.alert(`删除博客成功，此博客id为：${delete_id}`)
        let index = state.blogs.indexOf(state.blogs.filter(b => {b.id == delete_id})[0])
        console.log('删除博客的索引', index);
        state.blogs.splice(index)
      })
      .catch(error => {
        console.log(error);
      })
    },
    updateBlog(state, payload) {
      api.updateOne(payload)
      .then(response => {
        console.log(response);
        window.alert(`更新博客成功，此博客id为：${payload.id}`)
        router.push({name: 'User'})
      })
      .catch(error => {
        console.log(error);
      })
    },
    register(state, payload) {
      api.register(payload)
      .then(response => {
        // console.log(response);
        if (response) {
        window.alert(`注册成功，用户名：${response.data.username}`);
        router.push({name: 'Login'})
      }
      })
      .catch(error => {
        console.log(error);
        window.alert('已存在一位使用该名字的用户。');
      })
    }
   },
  actions: {
    // 接收组件的请求，调用mutations 中的方法
    // action 中定义的getPost 是组件中可调用的
    // pyload接收子组件传过来的参数
    getBlogs({
      commit
    }, payload) {
      commit('getBlogs', payload)
    },
    getBlogbyId({commit}, payload) {
      commit('getBlogbyId', payload)
    },
    getFilterBlogs({
      commit
    }, payload) {
      commit('getFilterBlogs', payload)
    },
    getFilterBlogsByTag({commit}, payload) {
      commit('getFilterBlogsByTag', payload)
    },
    addComment({
      commit
    }, payload) {
      commit('addComment', payload)
    },
    login({commit}, payload) {
      commit('login', payload)
    },
    logout({commit}) {
      commit('logout')
    },
    autologin({commit},) {
      commit('autologin')
    },
    addBlog({commit}, payload) {
      commit('addBlog', payload)
    },
    deleteBlog({commit}, payload) {
      commit('deleteBlog', payload)
    },
    updateBlog({commit}, payload) {
      commit('updateBlog', payload)
    },
    register({commit}, payload) {
      commit('register', payload)
    }
  },
  modules: {}
})