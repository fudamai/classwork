<template>
  <div class="recommend">
    <div class="row">
      <cabinet v-for="item in recommendItems" :key="item.id" :item="item" class="col-md-3 col-sm-7"></cabinet>
    </div>
  </div>
</template>

<script>
import Cabinet from "@/components/Cabinet.vue";

export default {
  name: "Recommend",
  components: { Cabinet },
  computed: {
    recommendItems() {
      let items = this.$store.getters.items;
      let vogue = this.$store.getters.vogue;
      let recoItems = [];
      for (let id of vogue) {
        recoItems.push(
          items.filter((item) => {
            return item.id == id;
          })[0]
        );
      }
      return recoItems.slice(0, 4);
    },
  },
  methods: {},
};
</script>

<style scoped>
</style>