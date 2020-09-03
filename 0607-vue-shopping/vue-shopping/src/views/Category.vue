<template>
  <div class="container">
    <h3 class="h3">{{ title }}</h3>
    <div class="row">
      <cabinet
        v-for="item in filterItemByType"
        :key="item.id"
        :item="item"
        class="col-md-3 col-sm-7 my-3"
      ></cabinet>
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
    filterItemByType() {
      let typeName = this.$route.params.name;
      if (typeName == "all") {
        return this.$store.getters.items;
      }
      return this.$store.getters.items.filter((item) => {
        return item.type == typeName;
      });
    },
    title() {
      return this.$store.getters.categories[this.$route.params.name];
    },
  },
  methods: {
    addToCart(item) {
      this.$store.commit("addToCart", item);
    },
  },
};
</script>
