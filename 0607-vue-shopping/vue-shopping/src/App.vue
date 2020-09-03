<template>
  <div id="app">
    <Up2uHeader/>
    <Menu/>
    <router-view/>
    <Up2uFooter/>
  </div>
</template>

<script>
import Up2uHeader from "@/components/Up2uHeader";
import Up2uFooter from "@/components/Up2uFooter";
import Menu from "@/components/Menu";

export default {
  components: {
    Up2uHeader,
    Up2uFooter,
    Menu
  }
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
