<template>
  <div class="home">
    <!-- Page Content -->
    <div class="container">
      <div class="row my-5">
        <div class="col-md-8">
          <!-- Blog Entries Column -->
          <!-- Blog blog -->
          <div
            class="card mb-4"
            v-for="blog in (filterBlogs.length ? filterBlogs : blogs)"
            v-bind:key="blog.id"
          >
            <img class="card-img-top" v-bind:src="blog.imgUrl" alt="Card image cap" />
            <div class="card-body">
              <h2 class="card-title">{{ blog.title }}</h2>
              <p class="card-text">{{ blog.content.slice(0,20) }}...</p>
              <router-link v-bind:to="{name: 'Detail', params:{id: blog.id}}" class="btn btn-primary">阅读全文</router-link>
            </div>
            <div class="card-footer text-muted">
              {{ blog.date }} 作者：
              <a href="#">{{ blog.owner }}</a>
            </div>
          </div>

          <!-- Pagination -->
          <!-- <ul class="pagination justify-content-center mb-4">
            <li class="page-item" v-bind:class="{'disabled': currentPage <= 1}">
              <a class="page-link" v-on:click="onPageUp">&larr; 上一页</a>
            </li>
            <li class="page-item" v-bind:class="{'disabled': nextPage < 1}">
              <a class="page-link" v-on:click="onPageDown">下一页 &rarr;</a>
            </li>
          </ul> -->

          <!-- /.row -->
          <!-- /.container -->
        </div>
        <div class="col-md-4 my-4">
          <BlogAside />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex";
import BlogAside from "@/components/BlogAside.vue";

export default {
  name: "Home",
  components: {
    BlogAside,
  },
  data() {
    return {
      currentPage: 1,
      keywords: "",
    };
  },
  computed: {
    ...mapGetters([
      // 这里是直接映射store 中的参数
      "blogs",
      "nextPage",
      "filterBlogs",
    ]),
  },
  created() {
    // 组件生命周期第一个调用的函数
    this.getBlogList();
    this.$store.dispatch("autologin");
    // console.log("filterBlogs: ", this.filterBlogs);
  },
  methods: {
    // Action 通过 store.dispatch 方法触发：
    // 以载荷形式分发
    getBlogList() {
      this.$store.dispatch("getBlogs");
      // this.$store.dispatch("getBlogs", {
      //   currentPage: this.currentPage,
      // });
    },
    onPageDown() {
      this.currentPage += 1;
      this.getBlogList();
    },
    onPageUp() {
      this.currentPage -= 1;
      this.getBlogList();
    },
    onSearch() {
      if (!this.keywords) {
        return;
      } // 搜索关键词为空时，直接跳出
      this.$store.dispatch("getFilterBlogs", {
        keywords: this.keywords,
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.card-img-top {
  max-height: 200px;
  width: auto;
}
</style>