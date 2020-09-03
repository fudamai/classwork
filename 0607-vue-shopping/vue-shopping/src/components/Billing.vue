<template>
  <div class="billing">
    <h3>订单</h3>
    <p>订单号：{{ billing.number }}</p>
    <h3>商品清单</h3>
    <table class="table table-striped">
      <tr>
        <td>名称</td>
        <td>尺码</td>
        <td>价格</td>
        <td>数量</td>
      </tr>
      <tr v-for="item in cartItems" v-bind:key="item.id">
        <td>{{ item.title }}</td>
        <td>{{ item.size.toUpperCase() }}</td>
        <td>{{ item.price | yuan }}</td>
        <td>{{ item.quantity }}</td>
      </tr>
    </table>
    <div class="total pull-right text-danger">合计：{{ totalPrice | yuan }}</div>
    <hr />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Billing",
  computed: {
    ...mapGetters({
      cartItems: "cart",
      billing: "billing",
      totalPrice: "totalPrice",
    }),
  },
};
</script>

<style scoped>
</style>