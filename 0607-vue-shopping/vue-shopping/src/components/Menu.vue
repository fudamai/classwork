<template>
  <div class="container">
    <div class="category-menu">
      <span v-for="(v, k) in categories" v-bind:key="v.id">
        <router-link v-bind:to="{name: 'Category', params:{name: k}}">{{ v }}</router-link>
      </span>

      <label for="search">
        搜索：
        <input
          type="text"
          id="search"
          placeholder="输入关键词，按回车"
          v-model="keyword"
          v-on:keyup.enter="submitKeyword"
        />
      </label>
    </div>
    <hr />
  </div>
</template>

<script>
export default {
  data() {
    return {
      categories: {},
      keyword: "",
    };
  },
  created() {
    this.categories = this.$store.getters.categories;
    // console.log("menu", this.categories);
  },
  methods: {
    submitKeyword() {
      this.$store.dispatch("submitKeyword", {
        keyword: this.keyword.trim(),
      });
      this.$router.push("/search");
    },
  },
};
</script>

<style lang="scss" scoped>
.category-menu {
  padding: 25px;
  a {
    display: inline-block;
    width: 100px;
    color: orange;
  }
}
</style>
