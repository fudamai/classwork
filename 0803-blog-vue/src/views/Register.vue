<template>
  <div class="register">
    <div class="row">
      <div class="col-lg-10 col-xl-9 mx-auto my-5">
        <div class="card-body">
          <h5 class="card-title text-center">注册</h5>
          <div class="form-signin">
            <div class="form-label-group">
              <input
                type="text"
                id="inputUserame"
                class="form-control"
                placeholder="用户名"
                required
                autofocus
                minlength="3"
                maxlength="15"
                v-model="newname"
              />
              <label for="inputUserame">用户名
                <span class="text-danger">{{ isNameRegular ? '' : '长度限制在4-15位,只能包含中文字符、数字、字母' }}</span>
                <span class="text-danger">{{ isResgiterDone ? '' : '用户名被占用' }}</span>
              </label>
            </div>

            <div class="form-label-group">
              <input
                type="email"
                id="inputEmail"
                class="form-control"
                placeholder="邮箱"
                required
                v-model="emailaddress"
              />
              <label for="inputEmail">电子邮箱
                <span class="text-danger">{{ isEmailRegular ? '' : '邮箱格式：xx@xx.xx' }}</span>
              </label>
            </div>

            <hr />

            <div class="form-label-group">
              <input
                type="password"
                id="inputPassword"
                class="form-control"
                placeholder="密码"
                required
                minlength="6"
                v-model="password"
              />
              <label for="inputPassword">密码
                <span class="text-danger">{{ isPwRegular ? '' : '最短六位，只能包含数字、字母' }}</span>
              </label>
            </div>

            <!-- <el-tooltip :disabled=isPwEqual content="两次输入密码不一致"> -->
            <div class="form-label-group">
              <input
                type="password"
                id="inputConfirmPassword"
                class="form-control"
                placeholder="Password"
                required
                v-model="confirmpassword"
              />
              <label for="inputConfirmPassword">
                确认密码
                <span class="text-danger">{{ isPwEqual ? '' : '两次密码不一致' }}</span>
              </label>
            </div>
            <!-- </el-tooltip> -->

            <button
              class="btn btn-lg btn-dark btn-block text-uppercase"
              type="submit"
              v-on:click.prevent="register"
            >注册</button>
            <!-- <a class="d-block text-center mt-2 small" href="#">登录</a> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

let formData = new FormData();

export default {
  name: "Register",
  data() {
    return {
      newname: "",
      emailaddress: "",
      password: "",
      confirmpassword: "",
      // issubmit: false,
    };
  },
  components: {},
  computed: {
    ...mapGetters([
      "isResgiterDone",
    ]),
    isPwEqual() {
      let a = this.password == this.confirmpassword;
      return a;
    },
    isPwRegular() {
      let a = this.password.length >= 6;
      let reg = /[^a-zA-Z0-9]/;
      let b = reg.test(this.password);
      return a && !b;
    },
    isNameRegular() {
      let a = this.newname.length >3 && this.newname.length < 15;
      let reg = /[^a-zA-Z0-9\u4e00-\u9fa5]/
      let b = reg.test(this.newname)
      return a && !b;
    },
    isEmailRegular() {
      let reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
      let b = reg.test(this.emailaddress);
      return b;
    },
    submitPermit() {
      // 判断输入是否合法
      // console.log(this.isPwEqual && this.isPwRegular && this.isNameRegular && this.isEmailRegular);
      return this.isPwEqual && this.isPwRegular && this.isNameRegular && this.isEmailRegular;
    }
  },
  methods: {
    register() {
      formData.append('username', this.newname);
      formData.append('email', this.emailaddress);
      formData.append('password', this.confirmpassword);
      if (this.submitPermit) {
        this.$store.dispatch("register", formData)
        // console.log("send");
      } else {
        window.alert('注册信息不完整')
      }
    },
  },
};
</script>script

<style lang="scss" scoped>
:root {
  --input-padding-x: 1.5rem;
  --input-padding-y: 0.75rem;
}

.card-signin {
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-signin .card-title {
  margin-bottom: 2rem;
  font-weight: 300;
  font-size: 1.5rem;
}

// .card-signin .card-img-left {
//   width: 45%;
//   /* Link to your background image using in the property below! */
//   background: scroll center url('https://source.unsplash.com/WEQbe2jBg40/414x512');
//   background-size: cover;
// }

.card-signin .card-body {
  padding: 2rem;
}

.form-signin {
  width: 100%;
}

.form-signin .btn {
  font-size: 80%;
  border-radius: 5rem;
  letter-spacing: 0.1rem;
  font-weight: bold;
  padding: 1rem;
  transition: all 0.2s;
}

.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}

.form-label-group input {
  border-radius: 0.2rem;
  line-height: 2.5rem;
}

.form-label-group > input,
.form-label-group > label {
  padding: var(--input-padding-y) var(--input-padding-x);
}

.form-label-group > label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0;
  /* Override default `<label>` margin */
  line-height: 1.3;
  color: #495057ab;
  border: 1px solid transparent;
  border-radius: 0.1rem;
  transition: all 0.1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}

.form-label-group input:-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-moz-placeholder {
  color: transparent;
}

.form-label-group input::placeholder {
  color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
  padding-top: calc(var(--input-padding-y) + var(--input-padding-y) * (2 / 3));
  padding-bottom: calc(var(--input-padding-y) / 3);
}

.form-label-group input:not(:placeholder-shown) ~ label {
  padding-top: calc(var(--input-padding-y) / 3);
  padding-bottom: calc(var(--input-padding-y) / 3);
  font-size: 8px;
  color: #777;
}
</style>