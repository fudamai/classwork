<template>
    <div class="container checkout">
        <h1>结算页</h1>
        <p>填写并核算订单信息</p>
        
        <div class="cart my-5">
            <billing></billing>
        </div>

        <div class="billing my-5">
            <h3>收货信息</h3>
            <form v-on:submit.prevent="submitForm()">
                <fieldset>
                    <label for="billingName">姓名：</label>
                    <input type="text" id="billingName" v-model="billing.name">
                    <label for="billingAddress">地址：</label>
                    <input type="text" id="billingAddress" v-model="billing.address">
                </fieldset>

                <input type="submit" class="btn btn-primary pull-right" value="提交订单">
                <!-- TODO:完善确认页 -->
            </form>
        </div>
    </div>
</template>

<script>
import Billing from "@/components/Billing"

export default {
    name: 'Checkout',
    data() {
        return {}
    },
    components: {
        Billing
    },
    computed: {
        // cartItems() {
        //     return this.$store.getters.cart;
        // },
        billing() {
            return this.$store.getters.billing;
        },
        // totalPrice() {
        //     return this.$store.getters.totalPrice;
        // }
    },
    methods: {
        submitForm() {
            this.$router.push({name: 'Confirm'})
            // 导航到一个新的URL
        }
    }
}
</script>

<style scoped>
.checkout{
    text-align: left;
    border: 1px solid gray;
}
/* .cart .billing{
    width: 100%;
    padding: 10px;
} */
</style>
