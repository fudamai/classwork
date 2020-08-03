<!-- Vue组件.md -->
<!-- author:fudamai -->

# 组件

组件系统是 Vue 的另一个重要概念，因为它是一种抽象，允许我们使用小型、独立和通常可复用的组件构建大型应用。仔细想想，几乎任意类型的应用界面都可以抽象为一个组件树：

![组件](./img/components.png)

在 Vue 里，一个组件本质上是一个拥有**预定义选项的一个 Vue 实例**。
为了能从父作用域将数据传到子组件，让我们来修改一下组件的定义，使之能够接受一个 prop。在 Vue 中注册组件很简单：

```html
<div id="app-7">
  <ol>
    <!-- 创建一个 todo-item 组件的实例 -->
    <!--
      现在我们为每个 todo-item 提供 todo 对象
      todo 对象是变量，即其内容可以是动态的。
      我们也需要为每个组件提供一个“key”，稍后再
      作详细解释。
    -->
    <todo-item
      v-for="item in groceryList"
      v-bind:todo="item"
      v-bind:key="item.id"
    ></todo-item>
  </ol>
</div>
```

```js
// 定义名为 todo-item 的新组件
Vue.component('todo-item', {
  // todo-item 组件现在接受一个
  // "prop"，类似于一个自定义 attribute。
  // 这个 prop 名为 todo。
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: '蔬菜' },
      { id: 1, text: '奶酪' },
      { id: 2, text: '随便其它什么人吃的东西' }
    ]
  }
})
```

使用 v-bind 指令将待办项传到循环输出的每个组件中。

尽管这只是一个刻意设计的例子，但是我们已经设法将应用分割成了两个更小的单元。*子单元通过 `prop` 接口与父单元进行了良好的解耦* 。我们现在可以进一步改进 `<todo-item>` 组件，提供更为复杂的模板和逻辑，而不会影响到父单元。

在一个大型应用中，有必要将整个应用程序划分为组件，以使开发更易管理。在后续教程中我们将详述组件，不过这里有一个 (假想的) 例子，以展示使用了组件的应用模板是什么样的：

```html
<div id="app">
  <app-nav></app-nav>
  <app-view>
    <app-sidebar></app-sidebar>
    <app-content></app-content>
  </app-view>
</div>

## 组件名

在注册一个组件的时候，我们始终需要给它一个名字。比如在全局注册的时候：

```js
Vue.component('my-component-name', { /* ... */ })
```

该组件名就是 Vue.component 的第一个参数。

你给予组件的名字可能依赖于你打算拿它来做什么。当**直接在 DOM 中使用**一个组件 (而不是在字符串模板或*单文件组件*) 的时候，我们强烈推荐遵循 W3C 规范中的自定义组件名 (**字母全小写且必须包含一个连字符**)。这会帮助你避免和当前以及未来的 HTML 元素相冲突。

## 组件名大小写

定义组件名的方式有两种：

- 使用 kebab-case

```js
Vue.component('my-component-name', { /* ... */ })
```

当使用 kebab-case (短横线分隔命名) 定义一个组件时，你也必须在引用这个自定义元素时使用 kebab-case，例如 `<my-component-name>`。

- 使用 PascalCase

```js
Vue.component('MyComponentName', { /* ... */ })
```

当使用 PascalCase (首字母大写命名) 定义一个组件时，你在引用这个自定义元素时两种命名法都可以使用。也就是说 `<my-component-name>` 和 `<MyComponentName>` 都是可接受的。注意，尽管如此，直接在 DOM (即非字符串的模板) 中使用时只有 kebab-case 是有效的。

-------

# 组件注册

## 全局注册

```js
Vue.component('my-component-name', {
  // ... 选项 ...
})
```

用 Vue.component 来创建组件,这些组件是全局注册的。也就是说它们在注册之后可以用在任何新创建的 `Vue 根实例 (new Vue) 的模板`中。在所有子组件中也是如此，也就是说这三个组件在各自内部也都可以相互使用。

全局注册的行为必须在根 Vue 实例 (通过 new Vue) 创建之前发生。

## 局部注册

定义时不指定组件名,就是局部注册。

```js
var ComponentA = { /* ... */ }
var ComponentB = { /* ... */ }
var ComponentC = { /* ... */ }
```

然后在 components 选项中定义你想要使用的组件：

```js
new Vue({
  el: '#app',
  components: {
    'component-a': ComponentA,
    'component-b': ComponentB
  }
})
```

对于 components 对象中的每个 property 来说，其 property 名就是自定义元素的名字，其 property 值就是这个组件的选项对象。

注意局部注册的组件在其子组件中不可用。

## 模块系统

通过 import/require 使用一个模块系统

### 在模块系统中局部注册

如果你还在阅读，说明你使用了诸如 Babel 和 webpack 的模块系统。在这些情况下，我们推荐 *创建一个 components 目录，并将每个组件放置在其各自的文件中*。

然后你需要在局部注册之前 *导入* 每个你想使用的组件。例如，在一个假设的 ComponentB.js 或 ComponentB.vue 文件中：

```js
import ComponentA from './ComponentA'
import ComponentC from './ComponentC'

export default {
  components: {
    ComponentA,
    ComponentC
  },
  // ...
}
```

现在 ComponentA 和 ComponentC 都可以在 ComponentB 的模板中使用了。

# 单文件组件

在很多 Vue 项目中，我们使用 Vue.component 来定义全局组件，紧接着用 new Vue({ el: '#container '}) 在每个页面内指定一个容器元素。

这种方式在很多中小规模的项目中运作的很好，在这些项目里 JavaScript 只被用来加强特定的视图。但当在更复杂的项目中，或者你的前端完全由 JavaScript 驱动的时候，下面这些缺点将变得非常明显：

- **全局定义 (Global definitions)** 强制要求每个 component 中的命名不得重复
- **字符串模板 (String templates)** 缺乏语法高亮，在 HTML 有多行的时候，需要用到丑陋的 `\`
- **不支持 CSS (No CSS support)** 意味着当 HTML 和 JavaScript 组件化时，CSS 明显被遗漏
- **没有构建步骤 (No build step)** 限制只能使用 HTML 和 ES5 JavaScript，而不能使用预处理器，如 Pug (formerly Jade) 和 Babel

文件扩展名为 `.vue` 的 **single-file components (单文件组件)** 为以上所有问题提供了解决方法，并且还可以使用 webpack 或 Browserify 等构建工具。

这是一个文件名为 Hello.vue 的简单实例：

![.vue文件](./img/vue-component.png)

*单文件组件中的选项与 普通 Vue 实例中的选项相同* 。

>只有根实例能用的 `el` 选项除外。

# Vue 组件细则

.vue 文件是一个自定义的文件类型，用类 HTML 语法描述一个 Vue 组件。每个 .vue 文件包含三种类型的顶级语言块 `<template>`、`<script>` 和 `<style>`，还允许添加可选的自定义块：

```html
<template>
  <div class="example">{{ msg }}</div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'Hello world!'
    }
  }
}
</script>

<style>
.example {
  color: red;
}
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>
```

vue-loader 会解析文件，提取每个语言块，如有必要会通过其它 loader 处理，最后将他们组装成一个 CommonJS 模块，module.exports 出一个 Vue.js 组件对象。

vue-loader 支持使用非默认语言，比如 CSS 预处理器，预编译的 HTML 模版语言，通过设置语言块的 lang 属性。例如，你可以像下面这样使用 Sass 语法编写样式：

```html
<style lang="sass">
  /* write Sass! */
</style>
```

更多细节可以在预处理器中找到。

语言块
**`<template>`**

- 默认语言：html。
- 每个 .vue 文件最多包含一个 `<template>` 块。
- 内容将被提取为字符串，将编译并用作 Vue 组件的 template 选项。

**`<script>`**

- 默认语言：js (在检测到 babel-loader 或 buble-loader 配置时自动支持ES2015)。
- 每个 .vue 文件最多包含 *一个* `<script>` 块。
- 该脚本在类 CommonJS 环境中执行 (就像通过 webpack 打包的正常 js 模块)，这意味着你可以 require() 其它依赖。在 ES2015 支持下，你也可以使用 import 和 export 语法。
- 脚本必须**导出 Vue.js 组件**对象。也可以导出由 Vue.extend() 创建的扩展对象，但是普通对象是更好的选择。

**`<style>`**

- 默认语言：css。
- 一个 .vue 文件可以包含 *多个* `<style>` 标签。
- `<style>` 标签可以有 scoped 或者 module 属性 (查看 CSS 作用域和 CSS Modules) 以帮助你将样式封装到当前组件。具有不同封装模式的多个 `<style>` 标签可以在同一个组件中混合使用。
- 默认情况下，将会使用 style-loader 提取内容，并通过 `<style>` 标签动态加入文档的 `<head>` 中，也可以配置 webpack 将所有 styles 提取到单个 CSS 文件中。

## 自定义块

只在 vue-loader 10.2.0+ 中支持

可以在 .vue 文件中添加额外的自定义块来实现项目的特定需求，例如 `<docs>` 块。vue-loader 将会使用标签名来查找对应的 webpack loader 来应用在对应的块上。webpack loader 需要在 vue-loader 的选项 loaders 中指定。

更多细节，查看自定义块。

## Src 导入

如果你喜欢分隔你的 .vue 文件到多个文件中，你可以通过 src 属性导入外部文件：

```html
<template src="./template.html"></template>
<style src="./style.css"></style>
<script src="./script.js"></script>
```

需要注意的是 src 导入遵循和 require() 一样的规则，这意味着你相对路径需要以 ./ 开始，你还可以从 NPM 包中直接导入资源，例如：

```html
<!-- import a file from the installed "todomvc-app-css" npm package -->
<style src="todomvc-app-css/index.css">
```

在自定义块上同样支持 src 导入，例如：

```html
<unit-test src="./unit-test.js">
</unit-test>
```

## 语法高亮

目前语法高亮支持 Sublime Text、Atom、Vim、Emacs、Visual Studio Code、Brackets 和 JetBrains products (WebStorm、PhpStorm 等)。非常感谢其他编辑器/IDE 所做的贡献！如果在 Vue 组件中没有使用任何预处理器，你可以把 .vue 文件当作 HTML 对待。

## 注释

在语言块中使用该语言块对应的注释语法 (HTML、CSS、JavaScript、Jade 等)。顶层注释使用 HTML 注释语法：<!-- comment contents here -->

# 单文件组件的复用

复用前导入即可

```js
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
```

# 插槽

HTML `<slot>` 元素 ，作为 Web Components 技术套件的一部分，是Web组件内的一个占位符。该占位符可以在后期使用自己的标记语言填充，这样您就可以创建单独的DOM树，并将它与其它的组件组合在一起。
