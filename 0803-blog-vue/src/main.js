 // 导入
 import Vue from 'vue'
 import axios from 'axios'
 import VueAxios from 'vue-axios'
 import App from './App.vue'
 import router from './router'
 import store from './store'
 import './plugins/element.js'

 // 引用

 Vue.use(VueAxios, axios)
 Vue.config.productionTip = false

 new Vue({
   router,
   store,
   render: h => h(App)
 }).$mount('#app')
