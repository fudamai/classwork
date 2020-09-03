<template>
  <div class="container">
    <h1>确认订单</h1>
    <div class="cart my-5">
      <billing></billing>
    </div>

    <!-- <hr/> -->
    <div class="checkout billing my-5">
      <h3>收货信息</h3>
      <p>姓名：{{ billing.name }}</p>
      <p>地址：{{ billing.address }}</p>
    </div>
    <p>扫码支付，货物将在12个月内发货</p>
    <img class="qr-img" src="../assets/1590505667037.jpg" alt="二维码" />
  </div>
</template>

<script>
import Billing from "@/components/Billing";

export default {
  name: "",
  data() {
    return {};
  },
  components: {
    Billing,
  },
  computed: {
    billing() {
      return this.$store.getters.billing;
    },
  },
};
</script>

<style scoped>
.qr-img {
  width: 300px;
  border-radius: 18px;
}
.checkout {
  text-align: left;
}
.cart,
.billing {
  width: 100%;
  padding: 10px;
}
.billing {
  height: 200px;
}
</style>
