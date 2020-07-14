<!-- gulp.md -->
<!-- author:fudamai -->

# Gulp

[nodejs网站](https://nodejs.org/zh-cn/)  
[gulp网站](https://gulpjs.com/)
[gulp插件](https://gulpjs.com/plugins/)

# 一 what

自动化的工具包，改善你的工作流

# 二 why

dev => product

将开发环境代码转化为生产环境代码。

作用

- 构建
- 压缩
- 校验
- 合并

## 1.前端开发

前端工程化必备阶段：构建，优化

开发（测试）环境：dev  
一般为 src 文件夹  
线上（生产）环境：product  
一般为 dist 或者 build 等文件夹。

### 构建

在开发环境构建代码。将代码进行打包

### 优化

优化为生产环境代码

具体操作

- 代码压缩
  - 取出空格、换行
  - 将长串的变量名换为短字符
- 构建
  - 指出错误代码
- 合并
  - 将多个Javascript代码进行合并

# 三 how

# 1.安装gulp

## 1-1.安装nodejs

官网下载，[nodejs网站](https://nodejs.org/zh-cn/)  
控制台使用代码检测nodejs 是否安装成功

```nodejs
> node -v
v12.16.3

> npm -v
6.14.4

> npx -v
6.14.4
```

## 1-2.安装Gulp

安装gulp

```nodejs
npm install -g gulp
```

安装控制台命令行工具

```nodejs
npm install gulp-cli -g
```

将npm替换为国内源，命令改为**cnpm**

```nodejs
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

# 2.简单使用

1.进入工程文件夹

```cmd
cd gulp-project
```

2.初始化工程文件

```cmd
npm init
```

- 会自动创建 package.json 文件，保存开发环境配置

>根据package.json文件复原开发环境  
```npm install```

3.在工程目录安装gulp

```cmd
npm install --save-dev gulp
```

>--save-dev ，将安装的包保存到开发环境

4.核实gulp 版本

```cmd
gulp -v
```

5.创建一个gulpfile

- 使用文本编辑器创建一个名为 gulpfile.js 的文件。文件位于工程目录的根位置
- gulpfile.js 是任务配置文件

```js
function defaultTask(cb) {
    // place code for your default task here
    cb();
}
  
exports.default = defaultTask
```

6.启动gulp

```cmd
gulp [taskname]
```

# 3.PIPE

pipe的作用

- 作为一个文件流管道，通常用在src() 与 dest() 方法之间。文件流在管道内执行不同的gulp插件定义的文件转换行为。

# 4.五个API

一些概念

vinyl

- Vinyl是一个描述文件的元数据对象。vinyl实例的主要属性是路径和内容

vinyl adapters | vinyl适配器

- 虽然vinyl提供了一种描述文件的方法，但是需要一种访问这些文件的方法。
- 例如：src(glob, [options])方法，返回一个生成vinyl对象的流。dest(folder, [options])方法，返回一个消耗vinyl对象的流

globs

- 通配符。如*、**或!，用于匹配文件路径。

## 4-1.gulp.src(globs, [options])

创建从文件系统读取vinyl对象的流。

参数

- globs:监视文件系统
- options:其它参数

用法

```js
const { src, dest } = require('gulp');

function copy() {
  return src('input/*.js')
    .pipe(dest('output/'));
}

exports.copy = copy;
```

返回值

- 数据流，可用于管道的开头或中间，以根据给定的全局变量添加文件。

## 4-2.gulp.dest(directory, [options])

创建将vinyl对象写入文件系统的流。

用法

```js
const { src, dest } = require('gulp');

function copy() {
  return src('input/*.js')
    .pipe(dest('output/'));
}

exports.copy = copy;
```

参数

- directory:输出文件保存的目录，必须是可用目录
- options:其它参数

返回值

- 数据流，可以在管道中间或末尾使用，用于在文件系统上创建文件。

## 4-3.gulp.task([taskName], taskFunction)

>提醒:这个API不再是推荐的模式-导出你的任务。4.0版本不推荐。**导出的都是公共任务**，可直接用gulp 命令调用。

在任务系统中定义任务。然后可以通过命令行和series()、parallel()和lastRun() api访问该任务。每个gulp任务都是一个异步JavaScript函数。

用法

```js
// 将一个命名函数注册为任务
const { task } = require('gulp');

function build(cb) {
  // body omitted
  cb();
}

task(build);

// 将匿名函数注册为任务
const { task } = require('gulp');

task('build', function(cb) {
  // body omitted
  cb();
});
```

参数

- taskName
  - 类型：字符串
  - 任务系统中任务函数的函数的别名。当任务函数使用命名函数时，可以省略。
- taskFunction，必需
  - 类型：函数
  - 任务函数、组合任务————由series() 和 parallel() 生成。理想情况下是命名函数。任务元数据可以被附加，以向命令行提供额外的信息。

返回值

注册任务时，不返回任何内容。

## 4-4.gulp.series(...tasks)

series：串行  
parallel：并行

Combines task functions and/or composed operations into larger operations that will be executed one after another, in sequential order. There are no imposed limits on the nesting depth of composed operations using series() and parallel().

用法

```js
const { series } = require('gulp');

function javascript(cb) {
  // body omitted
  cb();
}
function css(cb) {
  // body omitted
  cb();
}
exports.build = series(javascript, css);
```

参数

- tasks，必需
  - 类型：function、string
  - 可以将任意数量的任务函数作为单独的参数传递。如果之前已经注册了任务，可以使用字符串，但不建议这样做。

返回值

一个组合操作将被注册为一个任务或被嵌套进其它的 series 和/或 parallel 操作。

当执行组合操作时，所有任务将按顺序运行。如果在一个任务中发生错误，则不会运行后续任务。

## 4-5.gulp.watch(globs, [options], [task])

允许监听 globs 并在改变发生时运行任务。任务与任务系统的其余部分同一处理。

用法

```js
const { watch } = require('gulp');

watch(['input/*.js', '!input/something.js'], function(cb) {
  // body omitted
  cb();
});
```

参数

- globs，必需
  - 类型：字符串、数组
  - 用于监视文件系统。
- options：其它参数
- task
  - 类型：函数、字符串
  - 任务函数、组合任务——由 series() 和 parallel() 生成。

返回值

一个 chokidar 实例，用于精细的控制你的监听设置。

# 5.三个插件plugins

## 5-1.gulp-sass

将sacc、scss文件编译为css文件。  

安装

```cmd
npm install node-sass gulp-sass --save-dev
```

使用演示

```js
'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

sass.compiler = require('node-sass');

gulp.task('sass', function () {
  return gulp.src('./sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./sass/**/*.scss', ['sass']);
});
```

## 5-2.gulp-concat

合并多个js 文件  

安装

```cmd
npm install --save-dev gulp-concat
```

使用演示

```js
var concat = require('gulp-concat');

gulp.task('scripts', function() {
  return gulp.src('./lib/*.js')
    .pipe(concat('all.js'))
    .pipe(gulp.dest('./dist/'));
});
```

## 5-3.gulp-uglify

将js文件转化为最小版min.js文件  
安装

```cmd
npm install --save-dev gulp-uglify
```

使用演示

```js
var gulp = require('gulp');
var uglify = require('gulp-uglify');
var pipeline = require('readable-stream').pipeline;

gulp.task('compress', function () {
  return pipeline(
        gulp.src('lib/*.js'),
        uglify(),
        gulp.dest('dist')
  );
});
```

>为了帮助正确处理节点流的错误情况，本项目建议使用pipeline，从readable-stream。

>安装readable-stream  
npm install --save-dev readable-stream

# 6.项目案例

在项目目录下建立文件夹src、dist

## 6-1.插件需求

gulp-sass、node-sass、gulp-concat、gulp-uglify、readable-stream

## 6-2.开发环境代码

开发环境目录以src命名。代码修改在开发目录完成。

src/js/index.js

```js
console.log('index.js');
console.log('run in index.js');
onsole.log('测试pipeline');
console.log('测试exports');
```

src/js/main.js

```js
console.log('main.js');
console.log('运行main');
```

src/sass/style.scss

```scss
@charset 'UTF-8';

$body-bgc : yellow;

body {
    background-color: $body-bgc;
}
```

src/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>gulp 练习</title>
</head>
<body>
    <h2>gulp 的示例</h2>
    <p>新时代来临了gulp4.0</p>
    <p>js合并，最小化</p>
    <p>gulp监听</p>
    <p>测试</p>
    <p>更改测试</p>
    <!-- <script src="js/index.js"></script> -->
    <!-- <script src="js/main.js"></script> -->
    <script src="js/fubai.min.js"></script>
</body>
</html>
```

## 6-3.生产环境代码

生产环境目录以dist命名。生产环境所有代码都可自动生成

dist/css/style.css

```css
body { background-color: yellow; }
```

dist/js/fubai.min.js

```js
console.log("index.js"),console.log("run in index.js"),console.log("测试pipeline"),console.log("测试exports"),console.log("main.js"),console.log("运行main");
```

dist/index.html

HTML与开发代码相同

## 6-4.配置文件

gulpfile.js

```js
const gulp = require('gulp');
const sass = require('gulp-sass');  // 导入gulp-sass插件，用于将scss文件转换为css文件
const concat = require('gulp-concat');  // 导入gulp-concat插件，用于将多个js文件合并为一个js文件
const uglify = require('gulp-uglify');  // 导入gulp-uglify插件，将js文件转化为最小版min.js
var pipeline = require('readable-stream').pipeline;

// hello
gulp.task('hello', function () {
    return console.log('hello in gulp ...');
})

// src -> dist
// html文件
// 每个任务都需要return才能执行下一个任务
gulp.task('html', function () {
    return gulp.src('src/*.html').pipe(gulp.dest('dist'));
});

// sass -> css文件
sass.compiler = require('node-sass');

gulp.task('sass', function () {
    return gulp.src('src/sass/*.scss')// 开发目录
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('dist/css'));// 产品目录
});

// js:合并多个js -> fubai.min.js
gulp.task('js', function () {
    // return gulp.src('src/js/*.js')
    // .pipe(concat('fubai.min.js'))
    // .pipe(uglify())
    // .pipe(gulp.dest('dist/js'))

    return pipeline(
        gulp.src('src/js/*.js'),
        concat('fubai.min.js'),
        uglify(),
        gulp.dest('dist/js')
    )
})

// 设置执行gulp命令时，默认执行的任务
// 注意：此处演示的是4.0版本gulp的语法。与3.X版本语法不同
gulp.task('default', gulp.series(['html', 'sass', 'js']));

// 启动监听，修改后自动执行语句
// 一个任务监听一个任务
// gulp.task('watch', function() {
//     gulp.watch('src/*.html', gulp.series('html'));
//     gulp.watch('src/sass/style.scss', gulp.series('sass'));
//     gulp.watch('src/js/*.js', gulp.series('js'));
// })

// TODO:4.0版本任务输出
exports.watch = function() {
    // ignoreInitial设置为false，调用watch时就执行任务
    gulp.watch('src/*.html', { ignoreInitial: false }, gulp.series('html'));
    gulp.watch('src/sass/style.scss', { ignoreInitial: false }, gulp.series('sass'));
    gulp.watch('src/js/*.js', { ignoreInitial: false }, gulp.series('js'));
};
```

## 6-5.运行结果

执行命令

```cmd
gulp watch
```

按给定配置执行完毕后文件结构

```cwd
  gulp-demo
  |- node_modules
  |- dist
    |- css
      |- style.css
    |- js
      |- fubai.min.js
    |- index.html
  |- src
    |- js
      |- index.js
      |- main.js
    |- sass
      |- style.scss
    |- index.html
  |- gulpfile.js
  |- package.json
  |- package-lock.json
```
