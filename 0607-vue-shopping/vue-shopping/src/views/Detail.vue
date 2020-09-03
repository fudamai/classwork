<template>
  <div class="container">
    <h1>商品id：{{ $route.params.id }}</h1>
    <div class="card">
      <div class="container-fliud">
        <div class="wrapper row">
          <div class="preview col-md-6">
            <div class="preview-pic tab-content">
              <div class="tab-pane active" id="pic-1">
                <img v-bind:src="item.imgUrl1" alt="产品图片" />
              </div>
              <div class="tab-pane" id="pic-2">
                <img v-bind:src="item.imgUrl2" alt="产品图片" />
              </div>
            </div>

            <ul class="preview-thumbnail nav nav-tabs">
              <li class="active">
                <a data-target="#pic-1" data-toggle="tab">
                  <img v-bind:src="item.imgUrl1" alt />
                </a>
              </li>
              <li>
                <a data-target="#pic-2" data-toggle="tab">
                  <img v-bind:src="item.imgUrl2" alt />
                </a>
              </li>
            </ul>
          </div>

          <div class="details col-md-6">
            <h3 class="product-title">{{ item.title }}</h3>
            <div class="rating">
              <div class="stars">
                <li v-for="v in item.rating" v-bind:key="v.id" class="fa fa-star checked"></li>
                <li v-for="v in 5-item.rating" v-bind:key="v.id" class="fa fa-star"></li>
              </div>
            </div>

            <h4 class="price">
              当前价格：
              <span>{{ item.price | yuan }}</span>
            </h4>
            <h5 class="sizes">
              大小：
              <span
                v-bind:class="v.className"
                v-for="v in sizeItems"
                v-bind:key="v.id"
                data-toggle="tooltip"
                v-on:click="changeSize(v)"
                v-bind:title="v.title"
              >{{ v.size }}</span>
            </h5>

            <dl class="param param-inline">
              <dt>数量：</dt>
              <dd>
                <select v-model="quantity" class="form-control form-control-sm" style="width:70px;">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                  <option>6</option>
                  <option>7</option>
                  <option>8</option>
                  <option>9</option>
                  <option>10</option>
                </select>
              </dd>
            </dl>

            <div class="action">
              <button
                class="add-to-cart btn btn-default"
                type="button"
                v-on:click.prevent="addToCart()"
              >加入购物车</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sizeItems: [
        { size: "s", title: "小号", className: "size" },
        { size: "m", title: "中号", className: "size size-active" },
        { size: "l", title: "大号", className: "size" },
        { size: "xl", title: "特大号", className: "size" }
      ],
      quantity: 1
    };
  },
  computed: {
    item() {
      let id = this.$route.params.id;
      // console.log("detail id:", id);
      return this.$store.getters.items.find(item => id == item.id);
    }
  },
  methods: {
    changeSize(v) {
      for (let s of this.sizeItems) {
        s.className = "size";
      }
      v.className = "size size-active";
      this.item.size = v.size;
      // console.log("change size: ", this.item);
    },
    addToCart() {
      this.item.quantity = this.quantity;
      // console.log("detail page: ", this.item.quantity);
      this.$store.commit("addToCart", this.item);
    }
  },
};
</script>

<style scoped>
img {
  max-width: 100%;
}

.preview {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
}
@media screen and (max-width: 996px) {
  .preview {
    margin-bottom: 20px;
  }
}

.preview-pic {
  -webkit-box-flex: 1;
  -webkit-flex-grow: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
}

.preview-thumbnail.nav-tabs {
  border: none;
  margin-top: 15px;
}
.preview-thumbnail.nav-tabs li {
  width: 18%;
  margin-right: 2.5%;
}
.preview-thumbnail.nav-tabs li img {
  max-width: 100%;
  display: block;
}
.preview-thumbnail.nav-tabs li a {
  padding: 0;
  margin: 0;
}
.preview-thumbnail.nav-tabs li:last-of-type {
  margin-right: 0;
}

.tab-content {
  overflow: hidden;
}
.tab-content img {
  /* width: 100%; */
  height: 250px;
  -webkit-animation-name: opacity;
  animation-name: opacity;
  -webkit-animation-duration: 0.3s;
  animation-duration: 0.3s;
}

.card {
  margin-top: 50px;
  background: #eee;
  padding: 3em;
  line-height: 1.5em;
}

@media screen and (min-width: 997px) {
  .wrapper {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
  }
}

.details {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  text-align: left;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
  -ms-flex-direction: column;
  flex-direction: column;
}

.colors {
  -webkit-box-flex: 1;
  -webkit-flex-grow: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
}

.product-title,
.price,
.sizes,
.colors {
  text-transform: UPPERCASE;
  font-weight: bold;
}

.checked,
.price span {
  color: #ff9f1a;
}

.product-title,
.rating,
.product-description,
.price,
.vote,
.sizes {
  margin-bottom: 15px;
}

.product-title {
  margin-top: 0;
}

.size {
  margin-right: 10px;
}
.size:first-of-type {
  margin-left: 40px;
}
.size-active {
  background-color: orange;
}

.color {
  display: inline-block;
  vertical-align: middle;
  margin-right: 10px;
  height: 2em;
  width: 2em;
  border-radius: 2px;
}
.color:first-of-type {
  margin-left: 20px;
}

.add-to-cart,
.like {
  background: #ff9f1a;
  padding: 1.2em 1.5em;
  border: none;
  text-transform: UPPERCASE;
  font-weight: bold;
  color: #fff;
  -webkit-transition: background 0.3s ease;
  transition: background 0.3s ease;
}
.add-to-cart:hover,
.like:hover {
  background: #b36800;
  color: #fff;
}

.not-available {
  text-align: center;
  line-height: 2em;
}
.not-available:before {
  font-family: fontawesome;
  content: "\f00d";
  color: #fff;
}

.orange {
  background: #ff9f1a;
}

.green {
  background: #85ad00;
}

.blue {
  background: #0076ad;
}

.tooltip-inner {
  padding: 1.3em;
}

@-webkit-keyframes opacity {
  0% {
    opacity: 0;
    -webkit-transform: scale(3);
    transform: scale(3);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

@keyframes opacity {
  0% {
    opacity: 0;
    -webkit-transform: scale(3);
    transform: scale(3);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}
</style>
