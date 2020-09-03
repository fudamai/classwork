import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    items: [
      // 商品信息
      {
      id: 1,
      imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-1.jpg",
      imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-2.jpg",
      price: 16,
      priceOld: 20,
      size: 'm',
      isNew: true,
      title: '新款女士上衣',
      rating: 4,
      isOnSale: true,
      discount: '20%',
      type: 'women'
      },
      {
        id: 2,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-3.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-4.jpg",
        price: 100,
        priceOld: 200,
        size: 'm',
        isNew: true,
        title: '男士凉爽T恤',
        rating: 4,
        isOnSale: true,
        discount: '50%',
        type: 'men'
      },
      {
        id: 3,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-5.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-6.jpg",
        price: 50,
        priceOld: 100,
        size: 'm',
        isNew: true,
        title: '女士碎花衬衫',
        rating: 4,
        isOnSale: true,
        discount: '50%',
        type: 'women'
      },
      {
        id: 4,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-7.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-8.jpg",
        price: 60,
        priceOld: 100,
        size: 'm',
        isNew: true,
        title: '新款男士上衣',
        rating: 5,
        isOnSale: true,
        discount: '40%',
        type: 'men'
      },
      {
        id: 5,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-1.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-2.jpg",
        price: 16,
        priceOld: 20,
        size: 'm',
        isNew: true,
        title: '新款女士上衣',
        rating: 4,
        isOnSale: false,
        discount: '20%',
        type: 'women'
      }, {
        id: 6,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-3.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-4.jpg",
        price: 100,
        priceOld: 200,
        size: 'm',
        isNew: false,
        title: '男士凉爽T恤',
        rating: 4,
        isOnSale: false,
        discount: '50%',
        type: 'men'
      }, {
        id: 7,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-5.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-6.jpg",
        price: 50,
        priceOld: 100,
        size: 'm',
        isNew: true,
        title: '女士碎花衬衫',
        rating: 4,
        isOnSale: false,
        discount: '50%',
        type: 'women'
      }, {
        id: 8,
        imgUrl1: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-7.jpg",
        imgUrl2: "http://bestjquery.com/tutorial/product-grid/demo9/images/img-8.jpg",
        price: 60,
        priceOld: 100,
        size: 'm',
        isNew: true,
        title: '新款男士上衣',
        rating: 5,
        isOnSale: false,
        discount: '40%',
        type: 'men'
      }],
    cart: [],
    categories: {
      'all': '所有',
      'men': '男装',
      'women': '女装',
    },
    billing: {
      number: Date.parse(new Date()),
      name: 'fubai',
      address: '江南省凤阳府颍州道'
    },
    vogue: [1,2,3,4,5],
    collections: [6,7,8],
    searchKeyword: "",
  },
  getters: {
    cartQuantity: (state) => {
      // 购物车内商品的数量
      let quantity = 0;
      // console.log(state);
      for (let item of state.cart) {
        quantity += parseInt(item.quantity);
      }
      return quantity;
    },
    categories: state => {
      return state.categories;
    },
    billing: (state) => {
      return state.billing;
    },
    items: (state) => {
      return state.items;
    },
    cart: (state) => {
      return state.cart;
    },
    totalPrice: (state) => {
      let total = 0;
      for (let item of state.cart) {
        total += item.price * parseInt(item.quantity);
      }
      return total;
    },
    vogue: (state) => {
      return state.vogue;
    },
    collections: (state) => {
      return state.collections;
    },
    searchKeyword: (state) => {
      return state.searchKeyword;
    },
  },
  mutations: {
    addToCart: (state, item) => {
      // console.log('store: add cart', item);
      let product = state.cart.find(p => {
        if (p.title == item.title && p.size == item.size) {
          // 选中商品，更改商品的数量
          // console.log('addToCart:', p.quantity, item.quantity);
          if (Object.prototype.hasOwnProperty.call(item, "quantity")) {
            p.quantity = parseInt(item.quantity) + parseInt(p.quantity)
          } else {
            p.quantity++;
          }
          return p;
        }
      });

      if (!product) {
        // 往购物车里添加商品
        state.cart.push({
          id: item.id,
          title: item.title,
          type: item.type,
          size: item.size,
          image: item.imgUrl1,
          quantity: Object.prototype.hasOwnProperty.call(item, "quantity") ? item.quantity : 1,
          price: item.price
        });
      }
    },
    removeFromCart: (state, item) => {
      state.cart.splice(state.cart.indexOf(item), 1)
    },
    modifyCollection(state, payload) {
      // console.log("modifycoll", payload);
      if (payload.method == "add") {
        if (!state.collections.some(c => {return c == payload.mitem.id})) {
          state.collections.push(payload.mitem.id)
          // console.log(payload.mitem.id);
        }
      } else if (payload.method == "remove") {
        if (state.collections.some(c => {return c == payload.mitem.id})) {
          state.collections.splice(state.collections.indexOf(payload.mitem.id), 1)
          // console.log(state.collections);
        }
      }
    },
    submitKeyword(state, payload) {
      // console.log(payload.keyword);
      state.searchKeyword = payload.keyword;
    }
  },
  actions: {
    modifyCollection({commit}, payload) {
      commit('modifyCollection', payload)
    },
    submitKeyword({commit}, payload) {
      commit('submitKeyword', payload)
    }
  },

})
