<!-- JavaScript工作原理 -->
<!-- author：傅大麦 -->

原文链接：https://dzone.com/articles/how-javascript-actually-works-part-1  

原文标题：How JavaScript Actually Works

[解读 JavaScript 之引擎、运行时和堆栈调用](https://www.oschina.net/translate/how-does-javascript-actually-work-part-1)

[解读 JavaScript 之 V8 引擎及优化代码的 5 个技巧](https://www.oschina.net/translate/how-does-javascript-actually-work-part-2?lang=chs&p=1)

## 概述

几乎所有人都听说过 V8引擎的概念，大多数人都知道JavaScript是**单线程**  
的，或者它使用的是**回调队列**。

在这篇文章中，我们将详细讨论所有这些概念，并解释JavaScript实际上是如何  
运行的。通过了解这些细节，您将能够编写更好的、无阻塞的应用程序，能更好地  
利用所提供的api。

如果你是JavaScript的新手，这篇博客文章将帮助你理解为什么JavaScript与其  
他语言相比如此“怪异”。

如果你是一个有经验的JavaScript开发者，希望它会给你一些关于你每天使用的  
JavaScript运行时是如何工作的新鲜见解。

## The JavaScript Engine

一个较流行的JavaScript引擎是谷歌的 V8 引擎。V8 引擎是内置在chrome 和  
Node.js中。构造图：![JavaScript Engine](https://dzone.com/storage/temp/6257496-1-onh-dlbnapvb9klxucymsa.png)

引擎由两个主要部件组成：

- Memory Heap（内存堆） —— 分配内存
- Call Stack（调用栈）—— 代码执行时栈帧所在的位置

## The Runtime

几乎所有的 JavaScript 开发者都使用过浏览器中的 API（例如“setTimeout”）。    
然而这些API并不是由引擎提供的。

那么，它们从何而来。

实际上，事实要更复杂一点。

![JavaScript Engine runing](https://dzone.com/storage/temp/6257503-1-4lhhyfehvb0lnq3hlhss8g.png)
我们有了引擎，但实际上还有更多。我们有那些被称为**Web api**的东西，它们是由*浏览器提供的，比如DOM、AJAX、setTimeout等等。*

而且，我们还拥有非常流行的 event loop（事件循环） 和 callback queue（回  
调队列）。

## The Call Stack
JavaScript是一种*单线程编程*语言，这意味着它只有一个Call Stack（调用栈）。  
因此，它只能在同一时间作一件事。

调用栈是一个数据结构，它记录了我们在程序中的位置。如果我们将进入  
一个函数，我们把它放在堆栈的顶部。如果我们从一个函数返回，我们将弹出堆栈  
的顶部。这就是堆栈所能做的。

让我们看看一个例子。请阅读以下代码
~~~

function multiply(x, y) {
    return x * y;
}
function printSquare(x) {
    var s = multiply(x, x);
    console.log(s);
}
printSquare(5);
~~~
当引擎开始执行这段代码时，调用栈将为空。然后，步骤如下：

![call stack running](https://dzone.com/storage/temp/6257586-1-yp1kot-uj47hchms9y7kxw.png)

调用栈（call stack）中的每个条目被称为**栈帧（stack frame）**。

当抛出异常时，栈流程（stack trace）就是下面这样构造的——它基本上是异常发生时调用栈的状态。  
阅读以下代码：
~~~
function foo() {
    throw new Error('SessionStack will help you resolve crashes :)');
}
function bar() {
    foo();
}
function start() {
    bar();
}
start();
~~~

如果这是在Chrome中执行的(假设这段代码在一个名为foo.js的文件中)，将生成以  
下栈流程:

![stack trace](https://dzone.com/storage/temp/6257594-1-t-w-ihvl-9rg4dn18kp3qw.png)

“**Blowing the stack**”—当达到最大的调用栈时会发生这种情况。使用递归而  
不进行大量的代码测试，就容易出现这种情况。阅读以下代码：
~~~
function foo() {
    foo();
}
foo();
~~~

当引擎开始执行这段代码时，它开始调用函数“foo”。然后，这个函数开始迭代，并  
在没有终止条件的情况下调用自己。随着调用的不断执行，相同的函数被一遍遍的  
添加到调用栈。就像下面这个示意图一样：

![call stack recursive](https://dzone.com/storage/temp/6257599-1-aycfmdy9tldmnoc5lxd9-g.png)

在某个时刻，调用栈调用的函数数量超出了调用栈的实际大小，浏览器将会采取行动，如抛出错误，如下所示：  

![exceeds size error](https://dzone.com/storage/temp/6257624-1-e0ned59rpkz9coyy8fx-uw.png)

在单线程上运行代码非常容易，因为你不必处理多线程环境中会出现的复杂场景——  
例如：deadlocks。

但单线程运行也有很大的限制。由于JavaScript只有一个调用堆栈，那么运行缓慢  
时发生了什么?

## Concurrency and the Event Loop（并发性和事件循环）
当调用栈中的函数调用需要大量时间处理时，会发生什么情况?例如，假设你希望在  
浏览器中使用JavaScript进行一些复杂的图像转换。

你也许会问——为什么这也算是个问题？问题在于，当调用栈执行函数时，浏览器将  
会被阻塞（block)，也就是不能再执行其他事务。这意味着浏览器被卡住了，不能  
再执行渲染，或者运行其他代码。如果你想要再你的APP中拥有流畅的UI，这  
将是个问题。

而且，这并不是唯一的问题。一旦你的浏览器开始再调用栈执行如此多的任务，它  
可能会停止相应很长一段时间。然后，大多数浏览器都会生成一个错误，询问你是  
否要终止页面。  

![page unresponsive](https://dzone.com/storage/temp/6257631-1-wlmxk3rs-scqktrv41au7g.jpeg)

这明显不是最好的用户体验。

那么，我们如何才能在执行大量代码的同时，不阻塞UI以使浏览器正常响应呢?解  
决方案是： **asynchronous callbacks**（异步回调）。

