<template>
  <div class="home">
    <div class="container">
      <div class="row">
        <div class="col-md-8 col-sm-12 co-xs-12 gal-item">
          <div class="row h-50">
            <div class="col-md-12 col-sm-12 co-xs-12 gal-item">
              <div class="box">
                <a href="#">
                  <img
                    src="https://source.unsplash.com/random/758x370/?clother,tshirt"
                    class="img-ht img-fluid rounded"
                  />
                </a>
              </div>
            </div>
          </div>

          <div class="row h-50">
            <div class="col-md-6 col-sm-6 co-xs-12 gal-item">
              <div class="box">
                <a href="#">
                  <img
                    src="https://source.unsplash.com/random/371x370/?shirt,pants"
                    class="img-ht img-fluid rounded"
                  />
                </a>
              </div>
            </div>

            <div class="col-md-6 col-sm-6 co-xs-12 gal-item">
              <div class="box">
                <a href="#">
                  <img
                    src="https://source.unsplash.com/random/371x370/?jacket,jeans,coat"
                    class="img-ht img-fluid rounded"
                  />
                </a>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-4 col-sm-6 co-xs-12 gal-item">
          <div class="col-md-12 col-sm-6 co-xs-12 gal-item h-25">
            <div class="box">
              <a href="#">
                <img
                  src="https://source.unsplash.com/random/748x177/?coat,shirt"
                  class="img-ht img-fluid rounded"
                />
              </a>
            </div>
          </div>

          <div class="col-md-12 col-sm-6 co-xs-12 gal-item h-75">
            <div class="box">
              <a href="#">
                <img
                  src="https://source.unsplash.com/random/300x748/?jacket,jeans,coat"
                  class="img-ht img-fluid rounded"
                />
              </a>
            </div>
          </div>
        </div>
      </div>

      <h3 class="h3">特色推荐</h3>
      <recommend></recommend>
    </div>
    <hr />
  </div>
</template>

<script>
// @ is an alias to /src
import Recommend from "@/components/Recommend.vue";

export default {
  name: "Home",
  components: {
    Recommend,
  },
  computed: {
    items() {
      return this.$store.getters.homeSales;
    },
  },
  methods: {
    addToCart(item) {
      this.$store.commit("addToCart", item);
    },
  },
};
</script>

<style>
.gal-item {
  overflow: hidden;
  padding: 8px;
}
.gal-item .box {
  height: 100%;
  overflow: hidden;
}
.box img {
  height: 100%;
  width: auto;
  object-fit: cover;
}

h3.h3 {
  text-align: center;
  margin: 1em;
  text-transform: capitalize;
  font-size: 1.7em;
}

/********************* shopping Demo-1 **********************/
.product-grid {
  font-family: Raleway, sans-serif;
  text-align: center;
  padding: 0 0 72px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  overflow: hidden;
  position: relative;
  z-index: 1;
}
.product-grid .product-image {
  position: relative;
  transition: all 0.3s ease 0s;
}
.product-grid .product-image a {
  display: block;
}
.product-grid .product-image img {
  width: 100%;
  height: auto;
}
.product-grid .pic-1 {
  opacity: 1;
  transition: all 0.3s ease-out 0s;
}
.product-grid:hover .pic-1 {
  opacity: 1;
}
.product-grid .pic-2 {
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  transition: all 0.3s ease-out 0s;
}
.product-grid:hover .pic-2 {
  opacity: 1;
}
.product-grid .social {
  width: 150px;
  padding: 0;
  margin: 0;
  list-style: none;
  opacity: 0;
  transform: translateY(-50%) translateX(-50%);
  position: absolute;
  top: 60%;
  left: 50%;
  z-index: 1;
  transition: all 0.3s ease 0s;
}
.product-grid:hover .social {
  opacity: 1;
  top: 50%;
}
.product-grid .social li {
  display: inline-block;
}
.product-grid .social li a {
  color: #fff;
  background-color: #333;
  font-size: 16px;
  line-height: 40px;
  text-align: center;
  height: 40px;
  width: 40px;
  margin: 0 2px;
  display: block;
  position: relative;
  transition: all 0.3s ease-in-out;
}
.product-grid .social li a:hover {
  color: #fff;
  background-color: #ef5777;
}
.product-grid .social li a:after,
.product-grid .social li a:before {
  content: attr(data-tip);
  color: #fff;
  background-color: #000;
  font-size: 12px;
  letter-spacing: 1px;
  line-height: 20px;
  padding: 1px 5px;
  white-space: nowrap;
  opacity: 0;
  transform: translateX(-50%);
  position: absolute;
  left: 50%;
  top: -30px;
}
.product-grid .social li a:after {
  content: "";
  height: 15px;
  width: 15px;
  border-radius: 0;
  transform: translateX(-50%) rotate(45deg);
  top: -20px;
  z-index: -1;
}
.product-grid .social li a:hover:after,
.product-grid .social li a:hover:before {
  opacity: 1;
}
.product-grid .product-discount-label,
.product-grid .product-new-label {
  color: #fff;
  background-color: #ef5777;
  font-size: 12px;
  text-transform: uppercase;
  padding: 2px 7px;
  display: block;
  position: absolute;
  top: 10px;
  left: 0;
}
.product-grid .product-discount-label {
  background-color: #333;
  left: auto;
  right: 0;
}
.product-grid .rating {
  color: #ffd200;
  font-size: 12px;
  padding: 12px 0 0;
  margin: 0;
  list-style: none;
  position: relative;
  z-index: -1;
}
.product-grid .rating li.disable {
  color: rgba(0, 0, 0, 0.2);
}
.product-grid .product-content {
  background-color: #fff;
  text-align: center;
  padding: 12px 0;
  margin: 0 auto;
  position: absolute;
  left: 0;
  right: 0;
  bottom: -27px;
  z-index: 1;
  transition: all 0.3s;
}
.product-grid:hover .product-content {
  bottom: 0;
}
.product-grid .title {
  font-size: 13px;
  font-weight: 400;
  letter-spacing: 0.5px;
  text-transform: capitalize;
  margin: 0 0 10px;
  transition: all 0.3s ease 0s;
}
.product-grid .title a {
  color: #828282;
}
.product-grid .title a:hover,
.product-grid:hover .title a {
  color: #ef5777;
}
.product-grid .price {
  color: #333;
  font-size: 17px;
  font-family: Montserrat, sans-serif;
  font-weight: 700;
  letter-spacing: 0.6px;
  margin-bottom: 8px;
  text-align: center;
  transition: all 0.3s;
}
.product-grid .price span {
  color: #999;
  font-size: 13px;
  font-weight: 400;
  text-decoration: line-through;
  margin-left: 3px;
  display: inline-block;
}
.product-grid .add-to-cart {
  color: #000;
  font-size: 13px;
  font-weight: 600;
}
@media only screen and (max-width: 990px) {
  .product-grid {
    margin-bottom: 30px;
  }
}

/********************* Shopping Demo-3 **********************/
.product-grid3 {
  font-family: Roboto, sans-serif;
  text-align: center;
  position: relative;
  z-index: 1;
}
.product-grid3:before {
  content: "";
  height: 81%;
  width: 100%;
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.1);
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  transition: all 0.5s ease 0s;
}
.product-grid3:hover:before {
  opacity: 1;
  height: 100%;
}
.product-grid3 .product-image3 {
  position: relative;
}
.product-grid3 .product-image3 a {
  display: block;
}
.product-grid3 .product-image3 img {
  width: 100%;
  height: auto;
}
.product-grid3 .pic-1 {
  opacity: 1;
  transition: all 0.5s ease-out 0s;
}
.product-grid3:hover .pic-1 {
  opacity: 0;
}
.product-grid3 .pic-2 {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
  transition: all 0.5s ease-out 0s;
}
.product-grid3:hover .pic-2 {
  opacity: 1;
}
.product-grid3 .social {
  width: 120px;
  padding: 0;
  margin: 0 auto;
  list-style: none;
  opacity: 0;
  position: absolute;
  right: 0;
  left: 0;
  bottom: -23px;
  transform: scale(0);
  transition: all 0.3s ease 0s;
}
.product-grid3:hover .social {
  opacity: 1;
  transform: scale(1);
}
.product-grid3:hover .product-discount-label,
.product-grid3:hover .product-new-label,
.product-grid3:hover .title {
  opacity: 0;
}
.product-grid3 .social li {
  display: inline-block;
}
.product-grid3 .social li a {
  color: #e67e22;
  background: #fff;
  font-size: 18px;
  line-height: 50px;
  width: 50px;
  height: 50px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  margin: 0 2px;
  display: block;
  transition: all 0.3s ease 0s;
}
.product-grid3 .social li a:hover {
  background: #e67e22;
  color: #fff;
}
.product-grid3 .product-discount-label,
.product-grid3 .product-new-label {
  background-color: #e67e22;
  color: #fff;
  font-size: 17px;
  padding: 2px 10px;
  position: absolute;
  right: 10px;
  top: 10px;
  transition: all 0.3s;
}
.product-grid3 .product-content {
  z-index: -1;
  padding: 15px;
  text-align: left;
}
.product-grid3 .title {
  font-size: 14px;
  text-transform: capitalize;
  margin: 0 0 7px;
  transition: all 0.3s ease 0s;
}
.product-grid3 .title a {
  color: #414141;
}
.product-grid3 .price {
  color: #000;
  font-size: 16px;
  letter-spacing: 1px;
  font-weight: 600;
  margin-right: 2px;
  display: inline-block;
}
.product-grid3 .price span {
  color: #909090;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0;
  text-decoration: line-through;
  text-align: left;
  display: inline-block;
  margin-top: -2px;
}
.product-grid3 .rating {
  padding: 0;
  margin: -22px 0 0;
  list-style: none;
  text-align: right;
  display: block;
}
.product-grid3 .rating li {
  color: #ffd200;
  font-size: 13px;
  display: inline-block;
}
.product-grid3 .rating li.disable {
  color: #dcdcdc;
}
@media only screen and (max-width: 1200px) {
  .product-grid3 .rating {
    margin: 0;
  }
}
@media only screen and (max-width: 990px) {
  .product-grid3 {
    margin-bottom: 30px;
  }
  .product-grid3 .rating {
    margin: -22px 0 0;
  }
}
@media only screen and (max-width: 359px) {
  .product-grid3 .rating {
    margin: 0;
  }
}
</style>
