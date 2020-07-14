<!-- readme.md -->
<!-- author:fudamai -->

# shopping

文件入口:[商城页面](./dist/product/product.html)

将上一章的页面样式文件改成SASS格式，使用gulp打包。

# 51memo

文件入口:[备忘录页面](./webpack-51memo/dist/51memo.html)

51memo代码在将原有代码打包后出现报错：

```cmdout
Uncaught ReferenceError: box_type is not defined
```

排查后发现，在调用函数过程中。给默认参数传值时，无法指定参数名。只能按位置传入参数。此问题只出现在webpack打包后的代码中。

代码是在0601-jquery里memo代码的基础上，加上*删除单条备忘*的功能形成的。

代码使用webpack打包后JS代码文件大了一倍。233
