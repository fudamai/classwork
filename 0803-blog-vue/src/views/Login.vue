<template>
  <!-- Page Content -->
  <div class="login">
      <div class="col-sm-9 col-md-7 col-lg-8 my-5 mx-auto">
        <div class="card card-signin my-5">
          <div class="card-body">
            <h5 class="card-title text-center">登录</h5>
            测试用户admin，密码admin123。
            <br>
            <br>
            <form class="form-signin">
              <div class="form-label-group">
                <input
                  type="email"
                  id="inputName"
                  class="form-control"
                  v-model="username"
                  placeholder="用户名"
                  required
                  autofocus
                />
                <label for="inputEmail">用户名
                  <span class="text-danger">{{ authMessage ? authMessage : '' }}</span>
                </label>
              </div>

              <div class="form-label-group">
                <input
                  type="password"
                  id="inputPassword"
                  class="form-control"
                  v-model="password"
                  placeholder="密码"
                  required
                />
                <label for="inputPassword">密码</label>
              </div>

              <button
                class="btn btn-lg btn-dark btn-block text-uppercase"
                type="submit"
                v-on:click.prevent="login"
              >确认登录</button>
            </form>
          </div>
        </div>
      </div>
  </div>
  <!-- /.container -->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Login",
  components: {
    // BlogFooter
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  created() {
  },
  computed: {
    // 载入组件时，自动调用
    ...mapGetters([
      "isLogin",
      "authMessage",
    ])
  },
  methods: {
    login() {
      this.$store.dispatch("login", {
        username: this.username,
        password: this.password,
        // SavePw: this.SavePw
      });
    }
  }
};
</script>script

<style lang="scss" scoped>
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>