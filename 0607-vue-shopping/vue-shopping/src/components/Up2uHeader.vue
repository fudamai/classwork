<template>
    <div class="header">
        <header class="container">
        <div class="logo">
            <router-link to="/"><strong>汴京贸</strong></router-link>
        </div>
        <div class="nav">
            <router-link to="/">首页</router-link> | 
            <router-link to="/cart">购物车<span v-if="$store.getters.cartQuantity" class="badge badge-danger">{{ $store.getters.cartQuantity }}</span></router-link> | 
            <router-link to="/collection">收藏夹</router-link>
        </div>
        </header>
    </div>
</template>

<style lang="scss" scoped>

header{
    display: flex;
    height: 60px;
    flex-flow: row;
    align-items: center;
    justify-content: space-between;
}
.header{
    background-color: #eeeeee;
    .logo{
        border: 1px solid orange;
        padding: 5px;
    }
}

hr{
    margin: 0;
}
#nav{
    padding: 10px;
    a{
        font-weight: bold;
        color: #2c3e50;
        &.router-link-exact-active{
            color: orange;
        }
    }
}

</style>