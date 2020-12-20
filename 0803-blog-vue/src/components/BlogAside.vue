<template>
  <div class="aside">
    <!-- TODO:完成侧边栏的组件化 -->
    <!-- Sidebar Widgets Column -->
    <!-- <div class="col-md-4"> -->
    <!-- Search Widget -->
    <div class="card my-4">
      <h5 class="card-header">搜索</h5>
      <!-- TODO:在未搜索到内容的时候，显示无匹配项 -->
      <div class="card-body">
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            placeholder="关键词。。。"
            v-model="keywords"
            v-on:keyup.enter="onSearch"
          />
          <span class="input-group-btn">
            <button class="btn btn-primary" type="button" v-on:click="onSearch">Go!</button>
          </span>
        </div>
      </div>
    </div>

    <!-- Categories Widget -->
    <div class="card my-4">
      <h5 class="card-header">标签展示
        <button type="button" class="btn btn-light allpage" v-on:click="getBlogList">全部文章</button>
        <!-- <router-link to="/" class="btn btn-light allpage">
          全部文章
        </router-link> -->
      </h5>
      <!-- TODO:完成分类提取 -->
      <div class="card-body">
        <div v-for="(tag, index) in tagLog" :key="index" class="tag">
          <el-button v-on:click="getFilterBlogsByTag(tag)">{{ tag }}</el-button>
        </div>
      </div>
    </div>

    <!-- Side Widget -->
    <div class="card my-4">
      <h5 class="card-header">个人站</h5>
      <div class="card-body">
        <ol class="list-unstyled">
          <li>
            <a href="https://github.com/fudamai">GitHub</a>
          </li>
          <li>
            <a href="https://weibo.com/u/2960465301?is_all=1">Weibo</a>
          </li>
        </ol>
      </div>
    </div>
    <!-- </div> -->
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "BlogAside",
  data() {
    return {
      keywords: "",
      currentPage: 1,
    };
  },
  created() {
  },
  computed: {
    ...mapGetters([
      'tagLog'
    ]),
  },
  methods: {
    onSearch() {
      if (!this.keywords) {
        return;
      } // 搜索关键词为空时，直接跳出
      this.$store.dispatch("getFilterBlogs", {
        keywords: this.keywords,
      });
    },
    getFilterBlogsByTag(tag) {
      // console.log(tag);
      this.$store.dispatch("getFilterBlogsByTag", {
        tag: tag
      })
    },
    getBlogList() {
      this.$store.dispatch("getBlogs", {
        // currentPage: this.currentPage,
      });
    },
  },
};
</script>

<style lang="scss" scoped>

.tag {display: inline-block}
.allpage {
  float: right;
}
</style>