<template>
  <div class="user">
    <div class="container">
      <div class="m-6 p-4">
        <div></div>
        <h2 class="head">欢迎，{{ username }}</h2>
        <div class="text-warning" v-if="userBlogs.length == 0">还没有发布博客。</div>
        <ul v-for="blog in userBlogs" v-bind:key="blog.id" class="list-group m-4">
          <li class="list-group-item">
            <h2 class="card-title">{{ blog.title }}</h2>
            <p class="card-text">{{ blog.content.slice(0, 20) }}...</p>
            <button type="button" class="btn btn-danger float-right" v-on:click=deleteOne(blog.id)>
              删除
            </button>
            <router-link
              v-bind:to="{ name: 'Update', params: { id: blog.id } }"
              class="btn btn-primary float-right"
              >编辑</router-link>
          </li>
        </ul>
        <br>
        <br>
        <br>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "User",
  data() {
    return {
      userBlogs: "",
    };
  },
  computed: {
    ...mapGetters(["blogs", "username"]),
  },
  created() {
    this.getUserBlogs();
  },
  methods: {
    getUserBlogs() {
      this.userBlogs = this.blogs.filter((b) => {
        return b.owner == this.username;
      });
    },
    deleteOne(id) {
      this.$store.dispatch("deleteBlog", {
        id: id,
      });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>