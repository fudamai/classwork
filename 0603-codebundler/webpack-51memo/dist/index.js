/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/js/memo.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/css/memo.scss":
/*!***************************!*\
  !*** ./src/css/memo.scss ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("// removed by extract-text-webpack-plugin\n\n//# sourceURL=webpack:///./src/css/memo.scss?");

/***/ }),

/***/ "./src/js/memo.js":
/*!************************!*\
  !*** ./src/js/memo.js ***!
  \************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _css_memo_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../css/memo.scss */ \"./src/css/memo.scss\");\n/* harmony import */ var _css_memo_scss__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_css_memo_scss__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var jquery__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! jquery */ \"jquery\");\n/* harmony import */ var jquery__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(jquery__WEBPACK_IMPORTED_MODULE_1__);\n// memo.js\r\n// author: fudami\r\n// power by jQuery\r\n\r\n\r\n\r\n\r\n// 输入部分\r\njquery__WEBPACK_IMPORTED_MODULE_1___default()(\r\n    // 找到添加按钮的节点，监控click事件\r\n    jquery__WEBPACK_IMPORTED_MODULE_1___default()('input[type=submit]').on('click',\r\n        function () {\r\n            addTodo()\r\n        })\r\n)\r\n\r\nfunction addTodo() {\r\n    // 抓取输入框的元素，保存，更新到页面中\r\n\r\n    let todo = jquery__WEBPACK_IMPORTED_MODULE_1___default()('#new-item').val();\r\n    // console.log(todo);\r\n    let important = jquery__WEBPACK_IMPORTED_MODULE_1___default()('input[type=\"radio\"]:checked').val()\r\n    // console.log(important);\r\n    addItem(todo, status = 'todo', important = important);\r\n    initTodos();\r\n}\r\n\r\nfunction addItem(memo, status = 'todo', important = 1) {\r\n    // 对输入备忘进行整形并添加到localStorage\r\n    let todo_list = [];\r\n\r\n    let old_list = localStorage.getItem('fubaitodo-1');\r\n    // console.log(old_list);\r\n    if (old_list) {\r\n        todo_list = JSON.parse(old_list);\r\n    }\r\n\r\n    let todo = {};\r\n    todo.id = 1;\r\n    if (old_list) {\r\n        todo.id += parseInt(todo_list[todo_list.length - 1].id);\r\n    }\r\n    todo.text = memo;\r\n    todo.status = status;\r\n    todo.important = important;\r\n\r\n    todo_list.push(todo)\r\n\r\n    localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));\r\n    // console.log(localStorage.getItem('fubaitodo-1'));\r\n}\r\n\r\n// 提取部分\r\njquery__WEBPACK_IMPORTED_MODULE_1___default()(\r\n    // 打开页面时，调用此方法，自动填充页面\r\n    initTodos()\r\n)\r\n\r\nfunction getTodoList() {\r\n    // 从localStorage 中提取所有备忘\r\n    return JSON.parse(localStorage.getItem('fubaitodo-1'));\r\n}\r\n\r\nfunction initTodos() {\r\n    // 获取备忘，分析备忘，根据优先级分成四类，调用填充到DOM的方法\r\n    let todo_list = getTodoList();\r\n    if (todo_list.length) {\r\n        let fq_todos = todo_list.filter(x => x.important == 1);\r\n        let sq_todos = todo_list.filter(x => x.important == 2);\r\n        let tq_todos = todo_list.filter(x => x.important == 3);\r\n        let foq_todos = todo_list.filter(x => x.important == 4);\r\n        // console.log(fq_todos, sq_todos, tq_todos, foq_todos);\r\n        \r\n        insertTodo(fq_todos);\r\n        insertTodo(sq_todos, \"second-quadrant\",);\r\n        insertTodo(tq_todos, \"third-quadrant\",);\r\n        insertTodo(foq_todos, \"fourth-quadrant\",);\r\n        \r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()('.todo-info').attr('class', 'todo-info hidden');\r\n    }\r\n    \r\n    updateDoneList();\r\n}\r\n\r\nfunction insertTodo(todos, box_type = 'first-quadrant') {\r\n    // 接收输入的备忘，根据分类生成不同的HTML代码，并填充到DOM树中\r\n    if (!todos.length) {\r\n        return\r\n    }\r\n    let box = jquery__WEBPACK_IMPORTED_MODULE_1___default()(`#${box_type}`);\r\n    // box.append(`<div class=\"todo-title\">${html}</div>`);// 添加标题节点\r\n    for (let todo of todos) {\r\n        // console.log(todo.status);\r\n        if (todo.status == 'todo') {\r\n            box.append(`<li><input type=\"checkbox\" name=\"item\" id=${todo.id}>${todo.text}<button class=\"hidden\" id=\"deleteone\">删除</button></li>`);\r\n            updateDoneStyle(todo);\r\n        }\r\n    }\r\n    \r\n}\r\n\r\nfunction updateDoneStyle(todo) {\r\n    // 插入备忘时，完成状态不同样式不同\r\n    if (todo.status == 'done') {\r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()(`#${todo.id}`).parent().css('textDecoration', 'line-through');\r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()(`#${todo.id}`).prop('checked', true);\r\n    } else {\r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()(`#${todo.id}`).parent().css('textDecoration', '');\r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()(`#${todo.id}`).prop('checked', false);\r\n    }\r\n}\r\n\r\nfunction updateDoneList() {\r\n    // 将已完成备忘添加到已完成列表中\r\n    let box = jquery__WEBPACK_IMPORTED_MODULE_1___default()('#done-list');\r\n    box.html('');\r\n    let done_list = getTodoList().filter(x => x.status == 'done');\r\n\r\n    for (let todo of done_list) {\r\n        box.append(`<li>${todo.text}</li>`);\r\n    }\r\n}\r\n\r\n// 备忘样式修改部分\r\njquery__WEBPACK_IMPORTED_MODULE_1___default()(\r\n    // 找到备忘的checkbox，监听click事件\r\n    jquery__WEBPACK_IMPORTED_MODULE_1___default()('input[name=item]').on('click',\r\n        function () {\r\n            checkItem(this)\r\n        }\r\n    )\r\n)\r\n\r\nfunction checkItem(item) {\r\n    // 选中时添加删除线，并修改进行状态，更新已完成列表\r\n    let id = jquery__WEBPACK_IMPORTED_MODULE_1___default()(item).attr('id');\r\n    // console.log(id);\r\n    let bool = jquery__WEBPACK_IMPORTED_MODULE_1___default()(item).prop('checked');\r\n    // console.log(bool);\r\n    if (bool) {\r\n        // console.log($(item).parent());\r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()(item).parent().css('textDecoration', 'line-through');\r\n        changeStatus(id, 'done');\r\n    } else {\r\n        jquery__WEBPACK_IMPORTED_MODULE_1___default()(item).parent().css('textDecoration', '');\r\n        changeStatus(id, 'todo');\r\n\r\n    }\r\n    updateDoneList();\r\n}\r\n\r\nfunction changeStatus(id, status) {\r\n    // 根据选中与否，更改完成状态，保存\r\n    let todo_list = getTodoList();\r\n    for (let todo of todo_list) {\r\n        if (todo.id == id) {\r\n            todo.status = status;\r\n        }\r\n    }\r\n    localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));\r\n}\r\n\r\n// 删除所有备忘\r\njquery__WEBPACK_IMPORTED_MODULE_1___default()(\r\n    // 找到“删除所有备忘按钮”，监听click事件\r\n    jquery__WEBPACK_IMPORTED_MODULE_1___default()('.deleteall').on('click',\r\n    function () {\r\n        window.alert('删除所有备忘！');\r\n        localStorage.clear();\r\n        window.location.reload();\r\n    }\r\n    )\r\n)\r\n\r\njquery__WEBPACK_IMPORTED_MODULE_1___default()(\r\n    // 是否显示删除操作按钮\r\n    jquery__WEBPACK_IMPORTED_MODULE_1___default()('.quadrant li').hover(function () {\r\n        const div = jquery__WEBPACK_IMPORTED_MODULE_1___default()(this).find('button')[0];\r\n        // console.log(div);\r\n        if (div) {\r\n            jquery__WEBPACK_IMPORTED_MODULE_1___default()(div).removeClass('hidden');\r\n        }\r\n    }, function () {\r\n        const div = jquery__WEBPACK_IMPORTED_MODULE_1___default()(this).find('button')[0];\r\n        // console.log(div);\r\n        if (div) {\r\n            jquery__WEBPACK_IMPORTED_MODULE_1___default()(div).addClass('hidden');\r\n        }\r\n    })\r\n    )\r\n    \r\n    // 删除指定备忘\r\n    // 从localstorage中删除指定的备忘\r\njquery__WEBPACK_IMPORTED_MODULE_1___default()(\r\n    jquery__WEBPACK_IMPORTED_MODULE_1___default()('button[id=deleteone]').on('click', function() {\r\n        let todo_list = getTodoList();\r\n        let id = jquery__WEBPACK_IMPORTED_MODULE_1___default()(this).prev('input').prop('id');\r\n        // console.log(id);\r\n        for (let todo of todo_list) {\r\n            if (todo.id == id) {\r\n                let index = todo_list.indexOf(todo);\r\n                jquery__WEBPACK_IMPORTED_MODULE_1___default()(this).parent().addClass('hidden');\r\n                todo_list.splice(index,1)\r\n            }\r\n        }\r\n        // console.log(todo_list);\r\n        localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));\r\n    })\r\n)\n\n//# sourceURL=webpack:///./src/js/memo.js?");

/***/ }),

/***/ "jquery":
/*!*************************!*\
  !*** external "jQuery" ***!
  \*************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("module.exports = jQuery;\n\n//# sourceURL=webpack:///external_%22jQuery%22?");

/***/ })

/******/ });