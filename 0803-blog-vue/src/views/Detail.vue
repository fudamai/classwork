<template>
  <div class="detail">
    <div class="container">
      <div class="my-5 px-3">
        <div class="" v-if="blogById == '404'">
          <h1>页面不存在</h1>
        </div>
        <div v-else>
          <!-- Page Content -->
          <!-- Post Content Column -->
          <!-- Title -->
          <h1 class="mt-4">{{ blogById.title }}</h1>

          <!-- Author -->
          <p class="lead">
            作者：
            <a href="#">{{ blogById.owner }}</a>
          </p>

          <hr />

          <!-- Date/Time -->
          <p>发布时间 : {{ blogById.created.slice(0, 19) }}</p>

          <hr />
          <el-tag
            v-for="tag in blogById.tags ? blogById.tags : ''"
            v-bind:key="tag"
            >{{ tag }}</el-tag
          >
          <hr />

          <!-- Preview Image -->
          <div v-if="blogById.imgUrl">
            <img
              class="img-fluid rounded"
              v-bind:src="blogById.imgUrl"
              alt="图片"
            />
          </div>
          <div v-else class="text-danger">无图片</div>

          <hr />

          <!-- Post Content -->
          <p class="lead">{{ blogById.content }}</p>

          <hr />
          <br />
          <br />
          <br />

          <!-- Comments Form -->
          <div class="card my-4">
            <h5 class="card-header">留言：</h5>
            <div class="card-body">
              <form>
                <div class="form-group">
                  <textarea
                    class="form-control"
                    rows="3"
                    v-model="commentText"
                    required
                  ></textarea>
                </div>
                <!-- 数据要提交到store中 -->
                <button
                  type="submit"
                  class="btn btn-primary"
                  v-on:click.prevent="addComment"
                >
                  提交
                </button>
              </form>
            </div>
          </div>

          <!-- Single Comment -->

          <div
            class="media mb-1 p-1 row border-bottom bg-light"
            v-for="c in blogById.blog_comment"
            v-bind:key="c.id"
          >
            <!-- <img
              class="d-flex mr-3 rounded-circle"
              src="http://placehold.it/50x50"
              alt
            /> -->
            <div class="col-3 text-center text-info">{{ c.owner }}：</div>
            <div class="media-body border-left">
              <p class="mt-0">{{ c.content }}</p>
              <br />
              <small class="float-right text-info"
                >发布时间：{{ c.created.slice(0, 19) }}</small
              >
              <!-- <input type="text" v-bind:value="c" /> -->
            </div>
          </div>
        </div>
      </div>

      <br />
      <br />
      <br />
      <br />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

// import BlogAside from "@/components/BlogAside.vue";

export default {
  name: "Detail",
  components: {
    // BlogAside,
  },
  data() {
    return {
      commentText: "",
      blogComments: [],
      blog: "",
    };
  },
  created() {
    this.currentBlog();
  },
  computed: {
    ...mapGetters(["blogById", "isLogin"]),
  },
  methods: {
    addComment() {
      if (this.isLogin) {
        this.$store.dispatch("addComment", {
          blog: this.blogById.url,
          content: this.commentText,
        });
        this.commentText = "";
      } else {
        this.$router.push({ name: "Login" });
      }
    },
    currentBlog() {
      const id = this.$route.params.id;
      this.$store.dispatch("getBlogbyId", id);
    },
  },
  filters: {
    toBr: function (value) {
      return value.replace(/\n/g, "<br/>");
    },
  },
};
</script>script

<style lang="scss" scoped>
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>