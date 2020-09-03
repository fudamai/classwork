<template>
  <div class="cabinet">
    <div class="product-grid">
      <div class="product-image">
        <a href="#">
          <img class="pic-1" :src="item.imgUrl1" />
          <img class="pic-2" :src="item.imgUrl2" />
        </a>
        <ul class="social">
          <li>
            <a href data-tip="快速查看">
              <router-link :to="{name: 'Detail', params:{id: item.id}}">
                <i class="fa fa-search"></i>
              </router-link>
            </a>
          </li>

          <li>
            <a href data-tip="加入购物车">
              <i class="fa fa-shopping-cart" @click.prevent="addToCart(item)"></i>
            </a>
          </li>
        </ul>
        <span v-if="item.isOnSale" class="product-new-label">打折</span>
        <span v-else class="product-new-label">无货</span>
        <span v-if="item.isOnSale" class="product-discount-label">{{ item.discount }}</span>
      </div>
      <ul class="rating">
        <li v-for="v in item.rating" :key="v.id" class="fa fa-star"></li>
        <li v-for="v in 5-item.rating" :key="v.id" class="fa fa-star disable"></li>
      </ul>
      <div class="product-content">
        <h3 class="title">
          <router-link :to="{name: 'Detail', params:{id: item.id}}">{{item.title}}</router-link>
        </h3>
        <div class="price">
          {{item.price | yuan}}
          <span>{{item.priceOld | yuan}}</span>
        </div>
        <a class="add-to-cart" href @click.prevent="addToCart(item)">+ 加入购物车</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["item"],
  methods: {
    addToCart(item) {
      this.$store.commit("addToCart", item);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
