import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// 注册一个全局过滤器
Vue.filter('yuan', value => {
  return `￥${value.toFixed(2)}`;
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
