<template>
  <div class>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container">
        <router-link class="navbar-brand" to="/">言墙</router-link>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link to="/new" class="nav-link">新建</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/" class="nav-link">
                主页
                <span class="sr-only">(current)</span>
              </router-link>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <router-link to="/login" class="nav-link">登录</router-link>
            </li>
            <li class="nav-item" v-if="isLogin">
              <!-- <a to="/login" class="nav-link">{{ username }}</a> -->
              <router-link to="/user" class="nav-link">{{ username }}</router-link>
            </li>
            <li class="nav-item" v-if="isLogin">
              <a v-on:click="logout" class="nav-link">退出</a>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <router-link to="/register" class="nav-link">注册</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BlogNav",
  prods: "",
  data() {
    return {};
  },
  mounted() {
    // 载入组件时，自动调用
    // console.log(this.isLogin, this.username);
  },
  computed: {
    ...mapGetters(["isLogin", "username"]),
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
    },
  },
};
</script>

<style scoped>
.router-link-exact-active {
  color: #ffffff !important;
}
.nav-link {
  cursor: pointer;
}
</style>