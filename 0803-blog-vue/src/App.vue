<template>
  <div id="app">
    <BlogNav />
    <router-view />
    <BlogFooter class="footer" />
  </div>
</template>


<script>
import BlogNav from "./components/BlogNav.vue";
import BlogFooter from "./components/BlogFooter.vue";

export default {
  name: "App",
  components: {
    BlogNav,
    BlogFooter,
  },
};
</script>

<style lang="scss" scope>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}

.footer {
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
