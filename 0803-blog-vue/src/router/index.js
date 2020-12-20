import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import store from '@/store'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/new',
    name: 'New',
    component: () => import('../views/New.vue')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import('../views/User.vue')
  },
  {
    path: '/:id',
    name: 'Detail',
    component: () => import('../views/Detail.vue')
  },
  {
    path: '/update/:id',
    name: 'Update',
    component: () => import('../views/Update.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 路由守卫，判断是否登录
router.beforeEach((to, from, next) => {
  let isLogin = store.state.isLogin;
  // 下一步要判断目标路由是否需要登录
  // 注意，路由名设置为了首字母大写
  const toUrls = ['New', 'Update'];
  const target = to.name;
  // console.log(target);
  if (toUrls.indexOf(target) >= 0) {
    if (!isLogin) {
      router.push({name: 'Login'})
    }
  }

  // 对已经登录的页面，在login时，跳回home
  if (target === 'login') {
    if (isLogin) {
      router.push({name: 'Home'})
    }
  }

  // 执行next，继续其他操作
  next()
})

export default router