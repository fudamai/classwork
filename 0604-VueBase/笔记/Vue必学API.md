<!-- Vue必学API -->
<!-- author:fudamai -->

# API

*选项/数据*

## data

- 类型：`Object | Function`
- 限制：组件的定义只接受 function。
- 详细：

  Vue 实例的数据对象。Vue 将会递归将 data 的 property 转换为 getter/setter，从而让 data 的 property 能够响应数据变化。**对象必须是纯粹的对象 (含有零个或多个的 key/value 对)**：浏览器 API 创建的原生对象，原型上的 property 会被忽略。大概来说，data 应该只能是数据 - 不推荐观察拥有状态行为的对象。

  实例创建之后，可以通过 vm.$data 访问原始数据对象。Vue 实例也代理了 data 对象上所有的 property，因此访问 vm.a 等价于访问 vm.$data.a。

  **当一个组件被定义，data 必须声明为返回一个初始数据对象的函数**，因为组件可能被用来创建多个实例。如果 data 仍然是一个纯粹的对象，则所有的实例将共享引用同一个数据对象！通过提供 data 函数，每次创建一个新实例后，我们能够调用 data 函数，从而返回初始数据的一个全新副本数据对象。

  示例：

    ```js
    var data = { a: 1 }

    // 直接创建一个实例
    var vm = new Vue({
    data: data
    })
    vm.a // => 1
    vm.$data === data // => true

    // Vue.extend() 中 data 必须是函数
    var Component = Vue.extend({
    data: function () {
        return { a: 1 }
    }
    })
    ```

    注意，如果你为 data property 使用了箭头函数，则 this 不会指向这个组件的实例，不过你仍然可以将其实例作为函数的第一个参数来访问。

    ```js
    data: vm => ({ a: vm.myProp })
    ```

- 参考：[深入响应式原理](https://cn.vuejs.org/v2/guide/reactivity.html)

## props

- 类型：`Array<string> | Object`
- 详细：

  props 可以是数组或对象，**用于接收来自父组件的数据**。props 可以是简单的数组，或者使用对象作为替代，对象允许配置高级选项，如类型检测、自定义验证和设置默认值。

  你可以基于对象的语法使用以下选项：

  - type：可以是下列原生构造函数中的一种：String、Number、Boolean、Array、Object、Date、Function、Symbol、任何自定义构造函数、或上述内容组成的数组。会检查一个 prop 是否是给定的类型，否则抛出警告。
  - default：any
    为该 prop 指定一个默认值。如果该 prop 没有被传入，则换做用这个值。对象或数组的默认值必须从一个工厂函数返回。
  - required：Boolean
    定义该 prop 是否是必填项。
  - validator：Function
    自定义验证函数会将该 prop 的值作为唯一的参数代入。
- 示例：

    ```js
    // 简单语法
    Vue.component('props-demo-simple', {
    props: ['size', 'myMessage']
    })

    // 对象语法，提供验证
    Vue.component('props-demo-advanced', {
    props: {
        // 检测类型
        height: Number,
        // 检测类型 + 其他验证
        age: {
        type: Number,
        default: 0,
        required: true,
        validator: function (value) {
            return value >= 0
        }
        }
    }
    })
    ```

- 参考：[Props](https://cn.vuejs.org/v2/guide/components-props.html)

## computed

- 类型：`{ [key: string]: Function | { get: Function, set: Function } }`
- 详细：

    **计算属性**将被混入到 Vue 实例中。所有 getter 和 setter 的 this 上下文自动地绑定为 Vue 实例。

    注意如果你为一个计算属性使用了箭头函数，则 this 不会指向这个组件的实例，不过你仍然可以将其实例作为函数的第一个参数来访问。

    ```js
    computed: {
    aDouble: vm => vm.a * 2
    }
    ```

    计算属性的结果会被缓存，除非依赖的**响应式 property 变化才会重新计算**。注意，如果某个依赖 (比如非响应式 property) 在该实例范畴之外，则计算属性是不会被更新的。
- 示例：

    ```js
    var vm = new Vue({
    data: { a: 1 },
    computed: {
        // 仅读取
        aDouble: function () {
        return this.a * 2
        },
        // 读取和设置
        aPlus: {
        get: function () {
            return this.a + 1
        },
        set: function (v) {
            this.a = v - 1
        }
        }
    }
    })
    vm.aPlus   // => 2
    vm.aPlus = 3
    vm.a       // => 2
    vm.aDouble // => 4
    ```

- 参考：[计算属性](https://cn.vuejs.org/v2/guide/computed.html)

## methods

- 类型：`{ [key: string]: Function }`
- 详细：

    methods 将被混入到 Vue 实例中。可以直接**通过 VM 实例访问这些方法，或者在指令表达式中使用**。方法中的 this 自动绑定为 Vue 实例。

    >注意，不应该使用箭头函数来定义 method 函数 (例如 plus: () => this.a++)。理由是箭头函数绑定了父级作用域的上下文，所以 this 将不会按照期望指向 Vue 实例，this.a 将是 undefined。
- 示例：

    ```js
    var vm = new Vue({
    data: { a: 1 },
    methods: {
        plus: function () {
        this.a++
        }
    }
    })
    vm.plus()
    vm.a // 2
    ```

- 参考：[事件处理器](https://cn.vuejs.org/v2/guide/events.html)

## watch

在这个示例中，使用 watch 选项允许我们执行异步操作 (访问一个 API)，限制我们执行该操作的频率，并在我们得到最终结果前，设置中间状态。这些都是计算属性无法做到的。

- 类型：`{ [key: string]: string | Function | Object | Array }`
- 详细：

  一个对象，键是需要观察的表达式，值是对应回调函数。值也可以是方法名，或者包含选项的对象。Vue 实例将会在实例化时调用 $watch()，遍历 watch 对象的每一个 property。
- 示例：

    ```js
    var vm = new Vue({
    data: {
        a: 1,
        b: 2,
        c: 3,
        d: 4,
        e: {
        f: {
            g: 5
        }
        }
    },
    watch: {
        a: function (val, oldVal) {
        console.log('new: %s, old: %s', val, oldVal)
        },
        // 方法名
        b: 'someMethod',
        // 该回调会在任何被侦听的对象的 property 改变时被调用，不论其被嵌套多深
        c: {
        handler: function (val, oldVal) { /* ... */ },
        deep: true
        },
        // 该回调将会在侦听开始之后被立即调用
        d: {
        handler: 'someMethod',
        immediate: true
        },
        // 你可以传入回调数组，它们会被逐一调用
        e: [
        'handle1',
        function handle2 (val, oldVal) { /* ... */ },
        {
            handler: function handle3 (val, oldVal) { /* ... */ },
            /* ... */
        }
        ],
        // watch vm.e.f's value: {g: 5}
        'e.f': function (val, oldVal) { /* ... */ }
    }
    })
    vm.a = 2 // => new: 2, old: 1
    ```

  >注意，不应该使用箭头函数来定义 watcher 函数 (例如 searchQuery: newValue => this.updateAutocomplete(newValue))。理由同上
- 参考：[实例方法 / 数据 - vm.$watch](https://cn.vuejs.org/v2/api/#vm-watch)

**选项 / DOM**

## el

- 类型：`string | Element`
- 限制：只在用 new 创建实例时生效。
- 详细：

    提供一个在页面上**已存在的 DOM 元素作为 Vue 实例的挂载目标**。可以是 CSS 选择器，也可以是一个 HTMLElement 实例。

    在实例挂载之后，元素可以用 vm.$el 访问。

    **如果在实例化时存在这个选项，实例将立即进入编译过程，否则，需要显式调用 vm.$mount() 手动开启编译。**

    >提供的元素只能作为挂载点。因此不推荐挂载 root 实例到 `<html>` 或者 `<body>` 上。如果 render 函数和 template property 都不存在，挂载 DOM 元素的 HTML 会被提取出来用作模板，此时，必须使用 Runtime + Compiler 构建的 Vue 库。
- 参考：
  - [生命周期图示](https://cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%9B%BE%E7%A4%BA)
  - [运行时 + 编译器 vs. 只包含运行时](https://cn.vuejs.org/v2/guide/installation.html#%E8%BF%90%E8%A1%8C%E6%97%B6-%E7%BC%96%E8%AF%91%E5%99%A8-vs-%E5%8F%AA%E5%8C%85%E5%90%AB%E8%BF%90%E8%A1%8C%E6%97%B6)

## template

- 类型：string
- 详细：

  一个字符串模板作为 Vue 实例的标识使用。**模板将会替换挂载的元素**。挂载元素的内容都将被忽略，除非模板的内容有分发插槽。
- 参考：
  - [生命周期图示](https://cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%9B%BE%E7%A4%BA)
  - [通过插槽分发内容](https://cn.vuejs.org/v2/guide/components.html#%E9%80%9A%E8%BF%87%E6%8F%92%E6%A7%BD%E5%88%86%E5%8F%91%E5%86%85%E5%AE%B9)

用法：

```html
template: '<li>{{ todo.text }}</li>'
```

## render

- 分类：选项/DOM
- 类型：(createElement: () => VNode) => VNode
- 详细：
  字符串模板的代替方案，允许你发挥 JavaScript 最大的编程能力。

  **渲染函数**，一个vue 实例中的 *DOM 选项* 。该渲染函数接收一个 createElement 方法作为第一个参数用来创建 `VNode(虚拟节点)`。

>Vue 选项中的 render 函数若存在，则 Vue 构造函数不会从 template 选项或通过 el 选项指定的挂载元素中提取出的 HTML 模板编译渲染函数。

>将 `h` 作为 `createElement` 的别名是 Vue 生态系统中的一个通用惯例，实际上也是 JSX 所要求的。

**选项 / 其它**

## name

- 类型：string
- 限制：只有**作为组件选项时起作用。**
- 详细：
    单文件组件中，显式声明。

    允许组件模板递归地调用自身。注意，组件在全局用 Vue.component() 注册时，全局 ID 自动作为组件的 name。

    指定 name 选项的另一个好处是便于调试。有名字的组件有更友好的警告信息。另外，当在有 vue-devtools，未命名组件将显示成 `<AnonymousComponent>`，这很没有语义。通过提供 name 选项，可以获得更有语义信息的组件树。

**选项 / 其它**

## components

- 类型：Object
- 详细：
  包含 Vue 实例可用组件的哈希表。
- 参考：[组件](https://cn.vuejs.org/v2/guide/components.html)

**选项/生命周期钩子**

## created

created不会监听数据,监听数据是 watch，computed 通过数据绑定进行数据运算

- 类型：Function
- 详细：
  
  在--实例创建完成后被立即调用--。在这一步，实例已完成以下的配置：数据观测 (data observer)，property 和方法的运算，watch/event 事件回调。然而，挂载阶段还没开始，$el property 目前尚不可用。
- 参考：[生命周期图示](https://cn.vuejs.org/v2/guide/instance.html#%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E5%9B%BE%E7%A4%BA)

## vm.$mount( [elementOrSelector] )

- 分类：实例方法/ 声明周期
- 参数：
  - {Element | string} [elementOrSelector]
  - {boolean} [hydrating]
- 返回值：vm - 实例自身
- 用法：
  如果 Vue 实例在实例化时没有收到 el 选项，则它处于“未挂载”状态，没有关联的 DOM 元素。可以使用 vm.$mount() 手动地挂载一个未挂载的实例。

  如果没有提供 elementOrSelector 参数，模板将被渲染为文档之外的的元素，并且你必须使用原生 DOM API 把它插入文档中。

  这个方法返回实例自身，因而可以链式调用其它实例方法。
