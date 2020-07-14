// memo.js
// author: fudami
// power by jQuery

import '../css/memo.scss';
import $ from 'jquery';

// 输入部分
$(
    // 找到添加按钮的节点，监控click事件
    $('input[type=submit]').on('click',
        function () {
            addTodo()
        })
)

function addTodo() {
    // 抓取输入框的元素，保存，更新到页面中

    let todo = $('#new-item').val();
    // console.log(todo);
    let important = $('input[type="radio"]:checked').val()
    // console.log(important);
    addItem(todo, status = 'todo', important = important);
    initTodos();
}

function addItem(memo, status = 'todo', important = 1) {
    // 对输入备忘进行整形并添加到localStorage
    let todo_list = [];

    let old_list = localStorage.getItem('fubaitodo-1');
    // console.log(old_list);
    if (old_list) {
        todo_list = JSON.parse(old_list);
    }

    let todo = {};
    todo.id = 1;
    if (old_list) {
        todo.id += parseInt(todo_list[todo_list.length - 1].id);
    }
    todo.text = memo;
    todo.status = status;
    todo.important = important;

    todo_list.push(todo)

    localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));
    // console.log(localStorage.getItem('fubaitodo-1'));
}

// 提取部分
$(
    // 打开页面时，调用此方法，自动填充页面
    initTodos()
)

function getTodoList() {
    // 从localStorage 中提取所有备忘
    return JSON.parse(localStorage.getItem('fubaitodo-1'));
}

function initTodos() {
    // 获取备忘，分析备忘，根据优先级分成四类，调用填充到DOM的方法
    let todo_list = getTodoList();
    if (todo_list.length) {
        let fq_todos = todo_list.filter(x => x.important == 1);
        let sq_todos = todo_list.filter(x => x.important == 2);
        let tq_todos = todo_list.filter(x => x.important == 3);
        let foq_todos = todo_list.filter(x => x.important == 4);
        // console.log(fq_todos, sq_todos, tq_todos, foq_todos);
        
        insertTodo(fq_todos);
        insertTodo(sq_todos, "second-quadrant",);
        insertTodo(tq_todos, "third-quadrant",);
        insertTodo(foq_todos, "fourth-quadrant",);
        
        $('.todo-info').attr('class', 'todo-info hidden');
    }
    
    updateDoneList();
}

function insertTodo(todos, box_type = 'first-quadrant') {
    // 接收输入的备忘，根据分类生成不同的HTML代码，并填充到DOM树中
    if (!todos.length) {
        return
    }
    let box = $(`#${box_type}`);
    // box.append(`<div class="todo-title">${html}</div>`);// 添加标题节点
    for (let todo of todos) {
        // console.log(todo.status);
        if (todo.status == 'todo') {
            box.append(`<li><input type="checkbox" name="item" id=${todo.id}>${todo.text}<button class="hidden" id="deleteone">删除</button></li>`);
            updateDoneStyle(todo);
        }
    }
    
}

function updateDoneStyle(todo) {
    // 插入备忘时，完成状态不同样式不同
    if (todo.status == 'done') {
        $(`#${todo.id}`).parent().css('textDecoration', 'line-through');
        $(`#${todo.id}`).prop('checked', true);
    } else {
        $(`#${todo.id}`).parent().css('textDecoration', '');
        $(`#${todo.id}`).prop('checked', false);
    }
}

function updateDoneList() {
    // 将已完成备忘添加到已完成列表中
    let box = $('#done-list');
    box.html('');
    let done_list = getTodoList().filter(x => x.status == 'done');

    for (let todo of done_list) {
        box.append(`<li>${todo.text}</li>`);
    }
}

// 备忘样式修改部分
$(
    // 找到备忘的checkbox，监听click事件
    $('input[name=item]').on('click',
        function () {
            checkItem(this)
        }
    )
)

function checkItem(item) {
    // 选中时添加删除线，并修改进行状态，更新已完成列表
    let id = $(item).attr('id');
    // console.log(id);
    let bool = $(item).prop('checked');
    // console.log(bool);
    if (bool) {
        // console.log($(item).parent());
        $(item).parent().css('textDecoration', 'line-through');
        changeStatus(id, 'done');
    } else {
        $(item).parent().css('textDecoration', '');
        changeStatus(id, 'todo');

    }
    updateDoneList();
}

function changeStatus(id, status) {
    // 根据选中与否，更改完成状态，保存
    let todo_list = getTodoList();
    for (let todo of todo_list) {
        if (todo.id == id) {
            todo.status = status;
        }
    }
    localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));
}

// 删除所有备忘
$(
    // 找到“删除所有备忘按钮”，监听click事件
    $('.deleteall').on('click',
    function () {
        window.alert('删除所有备忘！');
        localStorage.clear();
        window.location.reload();
    }
    )
)

$(
    // 是否显示删除操作按钮
    $('.quadrant li').hover(function () {
        const div = $(this).find('button')[0];
        // console.log(div);
        if (div) {
            $(div).removeClass('hidden');
        }
    }, function () {
        const div = $(this).find('button')[0];
        // console.log(div);
        if (div) {
            $(div).addClass('hidden');
        }
    })
    )
    
    // 删除指定备忘
    // 从localstorage中删除指定的备忘
$(
    $('button[id=deleteone]').on('click', function() {
        let todo_list = getTodoList();
        let id = $(this).prev('input').prop('id');
        // console.log(id);
        for (let todo of todo_list) {
            if (todo.id == id) {
                let index = todo_list.indexOf(todo);
                $(this).parent().addClass('hidden');
                todo_list.splice(index,1)
            }
        }
        // console.log(todo_list);
        localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));
    })
)