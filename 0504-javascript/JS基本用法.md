<!-- JS基本用法 -->
<!-- author：fudamai -->

[MDN web docs javascript](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript)

# JavaScript

JavaScript ( JS ) 是一种具有函数优先的轻量级，解释型或即时编译型的编程语言。虽然它是作为开发Web 页面的脚本语言而出名的，但是它也被用到了很多非浏览器环境中，例如 Node.js、 Apache CouchDB 和 Adobe Acrobat。JavaScript 是一种基于原型编程、多范式的动态脚本语言，并且支持面向对象、命令式和声明式（如函数式编程）风格。

这里会讨论一部分在web中的用法。

## JavaScript可以做什么

客户端（client-side）JavaScript 语言的核心包含一些普遍的编程特性，以让你可以做到如下的事情：

- 在变量中储存有用的值。比如上文的示例中，我们请求客户输入一个新名字，然后将其储存到 name 变量中。
- 操作一段文本（在编程中称为“字符串”（string））。上文的示例中，我们取字符串 "玩家1："，然后把它和 name 变量连结起来，创造出完整的文本标签，比如："玩家1：小明"。
- 运行代码以响应网页中发生的特定事件。上文的示例中，我们用一个 click 事件来检测按钮什么时候被点击，然后运行代码更新文本标签。
- 以及更多！

>JavaScript语言也可用于服务器端（server-side）

JavaScript 语言核心之上所构建的功能更令人兴奋。**应用程序接口（Application Programming Interfaces（API））**将为你的代码提供额外的超能力。

**浏览器 API** 内建于 web 浏览器中，它们可以将数据从周边计算机环境中筛选出来，还可以做实用的复杂工作。例如：

- **文档对象模型 API（DOM（Document Object Model）API）** 能通过创建、移除和修改 HTML，为页面动态应用新样式等手段来操作 HTML 和 CSS。比如当某个页面出现了一个弹窗，或者显示了一些新内容（像上文小 demo 中看到那样），这就是 DOM 在运行。
- **地理位置 API（Geolocation API）** 获取地理信息。这就是为什么 谷歌地图 可以找到你的位置，而且标示在地图上。
- **画布（Canvas） 和 WebGL API** 可以创建生动的 2D 和 3D 图像。人们正运用这些 web 技术制作令人惊叹的作品。参见 Chrome Experiments 以及 webglsamples。
- 诸如 HTMLMediaElement 和 WebRTC 等 影音类 API 让你可以利用多媒体做一些非常有趣的事，比如在网页中直接播放音乐和影片，或用自己的网络摄像头获取录像，然后在其他人的电脑上展示（试用简易版 截图 demo 以理解这个概念）。

**第三方 API** 并没有默认嵌入浏览器中，一般要从网上取得它们的代码和信息。比如：

- Twitter API、新浪微博 API 可以在网站上展示最新推文之类。
- 谷歌地图 API、高德地图 API 可以在网站嵌入定制的地图等等。

# 怎样向页面添加 JavaScript？

使用`<script>`标签向HTML中添加JavaScript

具体形式：

- 内部JavaScript
- 外部JavaScript
- 内联JavaScript处理器

## 内部JavaScript

放在HTML文件中，在 </body> 标签结束前插入以下代码：

```css
<script>

  // 在此编写 JavaScript 代码

</script>
```

## 外部JavaScript

使用路径引用，将 `<script>` 元素替换为：

```css
<script src="script.js" async></script>
```

src指向js文件

## 内联JavaScript处理器

注意，有时候你会遇到在 HTML 中存在着一丝真实的 JavaScript 代码。它或许看上去像这样：

```js
function createParagraph() {
  const para = document.createElement('p');
  para.textContent = '你点击了这个按钮！';
  document.body.appendChild(para);
}
```

```css
<button onclick="createParagraph()">点我呀</button>

```

这个 demo 与之前的两个功能完全一致，只是在 `<button>` 元素中包含了一个**内联的 onclick 处理器**，使得函数在按钮被按下时运行。

然而请不要这样做。 这将使 JavaScript 污染到 HTML，而且效率低下。对于每个需要应用 JavaScript 的按钮，你都得手动添加 onclick="createParagraph()" 属性。

可以使用纯 JavaScript 结构来通过一个指令选取所有按钮。下文的这段代码即实现了这一目的：

```js
const buttons = document.querySelectorAll('button');

for(let i = 0; i < buttons.length ; i++) {
  buttons[i].addEventListener('click', createParagraph);
}
```

这样写乍看去比 onclick 属性要长一些，但是这样写会对页面上所有按钮生效，无论多少个，或添加或删除，完全无需修改 JavaScript 代码。

----
----

# JavaScript基本概念

- 变量
- 函数
- 对象
- 操作浏览器对象
- 运算符
- 条件语句
- 循环
- 事件

----
----

## 变量

变量类型,又称数据类型：

- Number
- String
- underfine
- null
- Boolean
- Object
- Array
- function

### 声明变量

声明一个变量的语法是在 var 或 let 关键字之后加上这个变量的名字：

```js
let myName;
let myAge;
```

>注意：推荐使用let声明变量。使用const声明常量

### 初始化变量

一旦你定义了一个变量，你就能够初始化它. 方法如下，在变量名之后跟上一个“=”，然后是数值:

```js
myName = 'Chris';
myAge = 37;
```

你可以像这样在声明变量的时候给变量初始化:

```js
let myName = 'Chris';
```

>但提升操作不再适用于 let 。

----

### Number

分为整数和浮点数。在JavaScript内部，所有数字都是以64位浮点数的形式储存。

数值的表示方法：科学计数法、直接表示法

数值的进制：十进制、八进制（0o)、十六进制(0x)、二进制(0b)

#### 特殊数值

正零：+0  
负零：-0

除作分母外。意义相同

NaN（not a number），主要出现在将字符串解析成数字出错的场合

Infinity，无穷。用来表示两种场景：一种是一个正的数值太大，或一个负的数值太小，无法表示；另一种是非0数值除以0，得到Infinity。

#### 与数值有关的全局方法

- parseInt(string,radix);
  - 用于将字符串转为整数
  - 用于进制转换
- parseFloat(string);
  - 解析一个参数（必要时先转换为字符串）并返回一个浮点数。
- isNaN(value);
  - 用来确定一个值是否为NaN 。
- isFinite(testValue);
  - 判断被传入的参数值是否为一个有限数值（finite number）。

----

### String

字符串就是零个或多个排在一起的字符，放在单引号或双引号之中。

```js
'abc'
"abc"
```

字符串可以被视为**字符数组**，因此可以使用数组的方括号运算符，用来返回某个位置的字符（位置编号从0开始）。

**length属性**返回字符串的长度，该属性也是无法改变的。

----

### null和underfine

null与undefined都可以表示“没有”，含义非常相似。千万不要把两个概念弄混淆了，“一个变量存在，但是没有数值”和“一个变量并不存在” — 他们完全是两回事 — 在前面你看到的盒子的类比中，不存在意味着没有可以存放变量的“盒子”。没有定义的值意味着有一个“盒子”，但是它里面没有任何值。

----

### Boolean

布尔值代表“真”和“假”两个状态。“真”用关键字true表示，“假”用关键字false表示。布尔值只有这两个值。

----

### Object

#### 1.概述

对象就是一组“键值对”（key-value）的集合，是一种无序的复合数据集合。

```js
var obj = {
  foo: 'Hello',
  bar: 'World'
};
```

#### 2.属性的操作

##### 2.1属性的读取

- 点操作符 .
- 方括号运算符 []

##### 2.2属性的赋值

点运算符和方括号运算符，不仅可以用来读取值，还可以用来赋值。

```js
var obj = {};

obj.foo = 'Hello';
obj['bar'] = 'World';
```

上面代码中，分别使用点运算符和方括号运算符，对属性赋值。

JavaScript 允许属性的“后绑定”，也就是说，你可以在任意时刻新增属性，没必要在定义对象的时候，就定义好属性。

##### 2.3属性的查看

查看一个对象本身的所有属性，可以使用Object.keys方法。

```js
Object.keys(obj);
```

##### 2.4属性的删除

delete命令用于删除对象的属性，删除成功后返回true。

```js
delete object.property 
delete object['property']
```

##### 2.5属性是否存在

in操作符

hasOwnProperty方法

##### 2.6属性的遍历

for...in...循环读取键名，也就是属性， for...of...循环读取键值

-----

### Function

#### 1.概述

##### 1.1函数声明

1.function 命令

```js
function name([param[, param[, ... param]]]) { statements }
```

2.函数表达式

除了用function命令声明函数，还可以采用变量赋值的写法。

var print = function(s) {
  console.log(s);
};
这种写法将一个**匿名函数**赋值给变量。这时，这个匿名函数又称函数表达式（Function Expression），因为赋值语句的等号右侧只能放表达式。

3.Function 构造函数

```js
new Function ([arg1[, arg2[, ...argN]],] functionBody)
```

1.2函数的重复声明

如果一个函数被多次声明，后面的声明就会覆盖前面的声明

1.3 圆括号运算符，return语句和递归

调用函数时，要使用括号运算符。圆括号之中，加入函数的参数。

函数体内部的return 语句，表示返回。return语句不是必需的，如果没有给定，该函数就不返回任何值，或者说返回underfined。

函数调用自身，称为递归。

1.4第一等公民

JavaScript 语言将函数看作一种值，与其它值（数值、字符串、布尔值等等）地位相同。**凡是可以使用值的地方，就能使用函数**。比如，可以把函数赋值给变量和对象的属性，也可以当作参数传入其他函数，或者作为函数的结果返回。函数只是一个可以执行的值，此外并无特殊之处。

由于函数与其他数据类型地位平等，所以在 JavaScript 语言中又称函数为第一等公民。

```js
function add(x, y) {
  return x + y;
}

// 将函数赋值给一个变量
var operator = add;

// 将函数作为参数和返回值
function a(op){
  return op;
}
a(add)(1, 1)
// 2
```

1.5 函数名的提升
JavaScript 引擎将函数名视同变量名，所以采用function命令声明函数时，整个函数会像变量声明一样，被提升到代码头部。所以，下面的代码不会报错。

```js
f();

function f() {}
```

#### 2.函数的属性和方法

2.1 name属性

函数的name属性返回函数的名字。
使用函数表达式定义的匿名函数，name属性，返回声明被指定的变量名。
使用函数表达式定义的具名函数，name属性返回函数名

2.2 length 属性

函数的length属性返回函数预期传入的参数个数，即函数定义之中的参数个数。

----

### Array

#### 1.定义

数组（array）是按次序排列的一组值。每个值的位置都有编号（从0开始），整个数组用方括号表示。

```js
var arr = ['a', 'b', 'c'];
```

数组可以先定义后赋值。

任何类型的数据，都可以放入数组。

#### 2.数组的本质

本质上，数组属于一种特殊的对象。typeof运算符会返回数组的类型是object。

```js
typeof [1, 2, 3] // "object"
```

上面代码表明，typeof运算符认为数组的类型就是对象。

数组的特殊性体现在，它的键名是按次序排列的一组整数（0，1，2...）。

数组的遍历
forEach()方法

**数组的空位**

当数组的某个位置是空元素，即两个逗号之间没有任何值，我们称该数组存在空位（hole）。

```js
var a = [1, , 1];
a.length // 3
```

上面代码表明，数组的空位不影响length属性。

需要注意的是，如果最后一个元素后面有逗号，并不会产生空位。也就是说，有没有这个逗号，结果都是一样的。

```js
var a = [1, 2, 3,];

a.length // 3
a // [1, 2, 3]
```

上面代码中，数组最后一个成员后面有一个逗号，这不影响length属性的值，与没有这个逗号时效果一样。

数组的空位是可以读取的，返回undefined。

```js
var a = [, , ,];
a[1] // undefined
```

使用delete命令删除一个数组成员，会形成空位，并且不会影响length属性。

```js
var a = [1, 2, 3];
delete a[1];

a[1] // undefined
a.length // 3
```

上面代码用delete命令删除了数组的第二个元素，这个位置就形成了空位，但是对length属性没有影响。也就是说，length属性不过滤空位。所以，使用length属性进行数组遍历，一定要非常小心。

数组的某个位置是空位，与某个位置是undefined，是不一样的。如果是空位，使用数组的forEach方法、for...in结构、以及Object.keys方法进行遍历，**空位都会被跳过**。

**类数组对象**

如果一个对象的所有键名都是正整数或零，并且有length属性，那么这个对象就很像数组，语法上称为“类似数组的对象”（array-like object）。

但是，“类似数组的对象”并不是数组，因为它们不具备数组特有的方法。

典型的“类似数组的对象”是函数的arguments对象，以及大多数 DOM 元素集，还有字符串。

 from 方法可以将一个对象转换为真正的数组（虽然老的浏览器可能不支持）：

```js
if (Array.from(str).every(isLetter)) { 
  console.log("The string '" + str + "' contains only letters!"); 
}
```

----

## 动态类型

JavaScript是一种“动态类型语言”，这意味着不同于其他一些语言(译者注：如C、JAVA)，您不需要指定变量将包含什么数据类型（例如number或string）

JavaScript默认将变量转换为字符串操作

----
----

## 运算符

JavaScript 拥有二元和一元运算符， 和一个特殊的三元运算符（条件运算符）。一个二元运算符需要两个操作数，分别在运算符的前面和后面：

>操作数1 运算符 操作数2
例如, 3+4 或 x*y。

一个一元运算符需要一个操作数，在运算符前面或后面：

>运算符 操作数

或

>操作数 运算符
例如, x++ 或 ++x。

JavaScript 拥有如下类型的运算符。

- 赋值运算符(Assignment operators)
  - =
- 比较运算符(Comparison operators)
  - 比较运算符比较它的操作数并返回一个基于表达式是否为真的逻辑值。
  - ==,!=,>,<,>=,<=
  - ===, !==。此二操作符会将类型加入判断。
- 算数运算符(Arithmetic operators)
  - +,-,*,/
  - %, ++, --, -, +, **
- 位运算符(Bitwise operators)
- 逻辑运算符(Logical operators)
  - &&与, ||或, !非
  - 能被转换为false的值有null, 0, NaN, 空字符串("")和undefined。
- 字符串运算符(String operators)
  - 结合两个操作数串
  - +, +=
- 条件（三元）运算符(Conditional operator)
  - 如果条件为真，则结果取值1。否则为值2。你能够在任何允许使用标准运算符的地方使用条件运算符。
  - >条件 ? 值1 : 值2
- 逗号运算符(Comma operator)
  - 当你想要在期望一个表达式的位置包含多个表达式时，可以使用逗号操作符。
  - ,
  - >expr1, expr2, expr3...
- 一元运算符(Unary operators)
  - delete
    - delete操作符，删除一个对象或一个对象的属性或者一个数组中某一个键值。语法
  - typeof
    - typeof 操作符返回一个表示 operand 类型的字符串值。operand 可为字符串、变量、关键词或对象，其类型将被返回。
  - void
    - void运算符,表明一个运算**没有返回值**。

    ```js
    void (expression)
    void expression
    ```

- 关系运算符(Relational operator)
  - in
    - in操作符，如果所指定的属性确实存在于所指定的对象中，则会返回true。否则，返回false。
    >propNameOrNumber in objectName
  - instanceof
    - 如果所判别的对象确实是所指定的类型，则返回true。
    >objectName instanceof objectType

- **new 运算符**
  - new 运算符创建一个**用户定义的对象类型的实例**或具有构造函数的内置对象的实例。

  ```js
    new constructor[([arguments])]
  ```

----
----

## 条件语句

- if...else
- switch

### if...else语句

当一个逻辑条件为真，用if语句执行一个语句。当这个条件为假，使用可选择的 else 从句来执行这个语句。

```js
if (条件) {
  当条件为真的时候，执行语句1;
  当条件为真的时候，执行语句2;
} else {
  当条件为假的时候，执行语句3;
  当条件为假的时候，执行语句4;
}
```

### switch语句

switch 语句允许一个程序求一个表达式的值并且尝试去匹配表达式的值到一个 case 标签。如果匹配成功，这个程序执行相关的语句。switch 语句如下所示：

```js
switch (expression) {
   case label_1:
      statements_1
      [break;]
   case label_2:
      statements_2
      [break;]
   ...
   default:
      statements_def
      [break;]
}
```

程序首先查找一个**与 expression 匹配的 case 语句，然后将控制权转移到该子句，执行相关的语句。** 如果没有匹配值， 程序会去找 default 语句，如果找到了，控制权转移到该子句，执行相关的语句。如果没有找到 default，程序会继续执行 switch 语句后面的语句。default 语句通常出现在switch语句里的最后面，当然这不是必须的。

----

## 异常处理

- throw语句
- try...catch语句

### throw语句

使用throw语句抛出一个异常。当你抛出异常，你规定一个含有值的表达式要被抛出。

```js
throw expression;
```

你可以抛出任意表达式而不是特定一种类型的表达式。如：字符串、数字、布尔值、对象

### try...catch语句

try...catch 语句有一个包含一条或者多条语句的try代码块，0个或1个的catch代码块，catch代码块中的语句会在try代码块中抛出异常时执行。

```js
try {
   throw "myException" // generates an exception
}
catch (e) {
// statements to handle any exceptions
   logMyErrors(e) // pass exception object to error handler
}
```

----
----

## 循环

JavaScript中提供了这些循环语句：

- for 语句
- do...while 语句
- while 语句
- labeled 语句
- break 语句
- continue 语句
- for...in 语句
- for...of 语句

----

### for 语句

一个 for 循环会一直重复执行，直到指定的循环条件为 false。

```js
for ([initialExpression]; [condition]; [incrementExpression])
  statement
```

### do...while 语句

do...while 语句一直重复直到指定的条件求值得到假值（false）。

```js
do
  statement
while (condition);
```

### while 语句

一个 while 语句只要指定的条件求值为真（true）就会一直执行它的语句块。

```js
while (condition)
  statement
```

### labeled 语句

一个 label 提供了一个让你在程序中其他位置引用它的标识符。例如，你可以用 label 标识一个循环， 然后使用 break 或者 continue 来指出程序是否该停止循环还是继续循环。

label 语句的语法看起来像这样：

```js
label :
   statement
```

**label 的值可以是任何的非保留字的 JavaScript 标识符**， statement 可以是任意你想要标识的语句（块）。

### break 语句

使用 break 语句来**终止循环**，switch， 或者是链接到 label 语句。

当你使用不带 label 的 break 时， 它会立即终止当前所在的 while，do-while，for，或者 switch 并把控制权交回这些结构后面的语句。
当你使用带 label 的 break 时，它会终止指定的带标记（label）的语句。
break 语句的语法看起来像这样：

```js
break [label];
```

在语法中，被 [] 包裹的内容是可省略的，也就是 label 可以省略。若省略，则终止当前所在的循环或 switch；若不省略，则终止指定的 label 语句。

### continue 语句

continue 语句可以用来继续执行（跳过代码块的剩余部分并进入下一循环）一个 while、do-while、for，或者 label 语句。

当你使用不带 label 的 continue 时， **它终止当前 while，do-while，或者 for 语句到结尾的这次的循环并且继续执行下一次循环。**
当你使用带 label 的 continue 时， 它会应用被 label 标识的循环语句。
continue 语句的语法看起来像这样：

```js
continue [label];
```

### for...in 语句

for...in 语句循环一个指定的变量来循环一个对象所有**可枚举的属性**。JavaScript 会为每一个不同的属性执行指定的语句。

```js
for (variable in object) {
  statements
}
```

### for...of 语句

for...of 语句在可迭代对象（包括Array、Map、Set、arguments 等等）上创建了一个循环，对值的每一个独特属性调用一次迭代。

```js
for (variable of object) {
  statement
}
```

>注意： for...in 循环遍历的结果是数组元素的下标，而 for...of 遍历的结果是元素的值。for...in 语句迭代的是**自定义的属性**，而不是数组的元素。迭代取数组元素，最好使用 forEach()方法

----
----

## 事件

Event 接口表示在 DOM 中发生的任何事件; 一些是用户生成的（例如鼠标或键盘事件），而其他由 API 生成（例如指示动画已经完成运行的事件，视频已被暂停等等）。事件通常由外部源触发，同样也会以编程方式触发，例如执行一个 element 的一个 HTMLElement.click( ) 方法，或通过定义事件，然后使用 EventTarget.dispatchEvent( ) 将其派发到一个指定的目标。有许多类型的事件，其中一些使用基于主要事件接口的其他接口。事件本身包含所有事件通用的属性和方法。

操作浏览器对象
