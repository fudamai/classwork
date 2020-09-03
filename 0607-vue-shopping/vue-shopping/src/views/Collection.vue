<template>
  <div class="collection">
    <h2>收藏夹</h2>
    <div class="container">
      <div class="card">
        <table class="table table-hover shopping-cart-wrap">
          <thead class="text-muted">
            <tr>
              <th scope="col">商品</th>
              <th scope="col" width="150">价格</th>
              <th scope="col" width="150" class="text-right">操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, k, index) in collections" v-bind:key="index">
              <td>
                <router-link :to="{name: 'Detail', params:{id: item.id}}">
                  <figure class="media">
                    <div class="img-wrap">
                      <img v-bind:src="item.imgUrl1" class="img-thumbnail img-sm" alt="产品图片" />
                    </div>
                    <figcaption class="media-body">
                      <h6 class="title text-truncate">{{ item.title }}</h6>
                    </figcaption>
                  </figure>
                </router-link>
              </td>
              <td>
                <div class="price-wrap">
                  <div v-if="item.isOnSale" class="text-muted">{{ item.price | yuan }}</div>
                  <div v-else>无货</div>
                </div>
              </td>
              <td class="text-right">
                <a
                  href
                  class="btn btn-outline-danger"
                  v-on:click.prevent="modifyCollection(item)"
                >&times; 移除</a>
              </td>
            </tr>
          </tbody>
        </table>

        <router-link class="btn btn-primary" to="/">去购物</router-link>
      </div>
      
    </div>
  </div>
</template>

<script>
// import Cabinet from "@/components/Cabinet";

export default {
  components: {
    // Cabinet,
  },
  computed: {
    collections() {
      let colList = this.$store.getters.collections;
      let items = this.$store.getters.items;
      let colItems = [];
      for (let id of colList) {
        colItems.push(
          items.filter((item) => {
            return item.id == id;
          })[0]
        );
      }
      return colItems;
    },
  },
  methods: {
    modifyCollection(item) {
      this.$store.dispatch("modifyCollection", {
        method: "remove",
        mitem: item,
      });
      // console.log("测试删除收藏", item.id);
    },
  },
};
</script>

<style scoped>
.img-sm {
  width: 90px;
  max-height: 75px;
  object-fit: cover;
}
</style>