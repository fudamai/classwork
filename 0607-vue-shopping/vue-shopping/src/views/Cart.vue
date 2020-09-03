<template>
  <div class="container cart">
    <br />
    <h3 class="text-center">我的购物车</h3>
    <hr />

    <div class="card">
      <table class="table table-hover shopping-cart-wrap">
        <thead class="text-muted">
          <tr>
            <th scope="col">商品</th>
            <th scope="col" width="100">数量</th>
            <th scope="col" width="150">价格</th>
            <th scope="col" width="150" class="text-right">操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, k, index) in cartItems" v-bind:key="index">
            <td>
              <figure class="media">
                <div class="img-wrap">
                  <img v-bind:src="item.image" class="img-thumbnail img-sm" alt="产品图片" />
                </div>
                <figcaption class="media-body">
                  <h6 class="title text-truncate">{{ item.title }}</h6>
                  <dl class="param param-inline small">
                    <dt>尺码：</dt>
                    <dd>{{ item.size.toUpperCase() }}</dd>
                  </dl>
                </figcaption>
              </figure>
            </td>
            <td>
              <select class="form-control" v-model="item.quantity">
                <option v-for="s in 10" v-bind:key="s.id">{{ s }}</option>
              </select>
            </td>
            <td>
              <div class="price-wrap">
                <var class="price">总价：{{ item.price * item.quantity | yuan}}</var>
                <small class="text-muted">(单价： {{ item.price | yuan }})</small>
              </div>
            </td>
            <td class="text-right">
              <a
                href
                title
                class="btn btn-outline-success"
                data-toggle="tooltip"
                data-original-title="添加到收藏"
                v-on:click.prevent="modifyCollection(item)"
              >
                <i class="fa fa-heart"></i>
              </a>
              <a
                href
                class="btn btn-outline-danger"
                v-on:click.prevent="removeFromCart(item)"
              >&times; 移除</a>
            </td>
          </tr>
        </tbody>
      </table>

      <router-link v-if="cartItems.length" class="btn btn-primary" to="/checkout">去结算</router-link>
      <router-link v-else class="btn btn-primary" to="/">去购物</router-link>
    </div>

    <h3 class="h3">你可能也喜欢</h3>
    <recommend></recommend>
  </div>
</template>

<script>
import Recommend from "@/components/Recommend.vue";

export default {
  components: {
    Recommend,
  },
  computed: {
    cartItems() {
      return this.$store.getters.cart;
    },
  },
  methods: {
    removeFromCart(item) {
      this.$store.commit("removeFromCart", item);
    },
    modifyCollection(item) {
      this.$store.dispatch("modifyCollection", {
        method: "add",
        mitem: item,
      });
      // console.log("测试收藏",item.id);
    },
  },
};
</script>

<style scoped>
.cart {
  min-height: 700px;
}
.param {
  margin-bottom: 7px;
  line-height: 1.4;
}
.param-inline dt {
  display: inline-block;
}
.param dt {
  margin: 0;
  margin-right: 7px;
  font-weight: 600;
}
.param-inline dd {
  vertical-align: baseline;
  display: inline-block;
}
.param dd {
  margin: 0;
  vertical-align: baseline;
}
.shopping-cart-wrap .price {
  color: #007bff;
  font-size: 18px;
  font-weight: bold;
  margin-right: 5px;
  display: block;
}
var {
  font-style: normal;
}
.media img {
  margin-right: 1rem;
}
.img-sm {
  width: 90px;
  max-height: 75px;
  object-fit: cover;
}
</style>
