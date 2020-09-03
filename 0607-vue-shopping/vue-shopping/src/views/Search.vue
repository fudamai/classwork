<template>
  <div class="search">
    <div class="container">
      <h3>搜索结果</h3>
      <div class="row">
        <cabinet
          v-for="item in searchResult"
          :key="item.id"
          :item="item"
          class="col-md-3 col-sm-7 my-3"
        ></cabinet>
      </div>
    </div>
  </div>
</template>

<script>
import Cabinet from "@/components/Cabinet.vue";

export default {
  components: {
    Cabinet,
  },
  data() {
    return {};
  },
  computed: {
    searchResult() {
      let keyword = this.$store.getters.searchKeyword;
    //   console.log(keyword);
      let result = "";
      if (keyword.length > 0) {
        result = this.$store.getters.items.filter((i) => {
          return i.title.includes(keyword);
        });
      }
      return result;
    },
  },
  methods: {
  },
};
</script>