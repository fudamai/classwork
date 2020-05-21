// js for 51memo

function addTodo() {
    // 抓取输入框的元素，保存，更新到页面中
    // 抓取输入框的元素
    let todo = document.getElementById('new-item').value;
    // 获取分类信息
    let important = document.querySelector('input[type="radio"]:checked').value;
    console.log(todo, important);
    // 添加到localStorage
    addItem(todo, status = 'todo', important = important)
    // insert to box
    init_todos();
}

function addItem(memo, status = 'todo', important = 1) {
    // 对输入备忘进行整形并添加到localStorage 
    let todo_list = [];
    let old_list = localStorage.getItem('fubaitodo');
    // 获取旧的记录并保存
    if (old_list) {
        // 如果有旧的记录，将其赋值给todo_list
        todo_list = JSON.parse(old_list);
    }
    let todo = {};
    todo.id = 1;
    if (old_list) {
        // 本地有存储的todo才添加id
        todo.id += parseInt(todo_list[todo_list.length - 1].id);
    }

    todo.text = memo;
    todo.status = status; // todo, done
    todo.important = important; // 1 important, 2 not
    todo_list.push(todo)

    // 存储到本地。以json的格式
    localStorage.setItem('fubaitodo', JSON.stringify(todo_list));
    console.log(localStorage.getItem('fubaitodo'));
}

function insertTodo(todos, box_type='important', html ='高优先级的事') {
    // 接收输入的记录，根据分类生成不同的HTML代码，并填充到盒模型中
    if (!todos.length) {
        // 对输入添加判断
        return;
    }
    let box = document.getElementById(box_type)
    // 根据类型获取节点
    box.innerHTML = `<div class="todo-title">${html}</div>`;
    for (let todoi of todos) {
        let li = document.createElement('li');
        // 生成HTML代码
        li.innerHTML = `<input type="checkbox" onclick="checkItem(this);" name="item" id=${todoi.id}>${todoi.text}`;
        // 添加为同级标签
        box.append(li);
        updateDoneStyle(todoi, li);
        // box.appendChild(li);
    }
}

function getTodoList() {
    // 用来取所有结果
    let todo_list = [];
    return JSON.parse(localStorage.getItem('fubaitodo'))
}

function init_todos() {
    // 将记录按分类填充到不同的盒模型中
    // insert to box
    // 1.get list
    let todo_list = getTodoList()
    if (todo_list.length) {
        // 2.区分重要性important
        // console.log(todo_list);
        let imp_todos = todo_list.filter(x => x.important == 1);
        let low_todos = todo_list.filter(x => x.important == 2);
        console.log(imp_todos, low_todos);
        // 分开放入对应的div box
        insertTodo(imp_todos)
        insertTodo(low_todos, box_type = 'low-level', html = '低优先级的事')
        let info = document.getElementsByClassName('todo-info')[0];
        info.className = 'todo-info hidden'
        // 更改类名，方便隐藏
    }
    // 添加到今日计划的记录，status应是todo
    updateDoneList();
}

function checkItem(item) {
    // 选中时添加删除线，并修改进行状态
    console.log(item);
    let li = item.parentElement;
    if (item.checked) {
        li.style.textDecoration = 'line-through';
        // 修改状态值
        changeStatus(item.id, 'done');
    } else {
        li.style.textDecoration = '';
        // 修改状态值
        changeStatus(item.id, 'todo');
    }
    updateDoneList();
}

function updateDoneList() {
    // 将勾选的项目添加到完成列表中
    // 获取以完成标签
    let box = document.getElementById('done-list');
    box.innerHTML = "";
    let done_list = getTodoList().filter(x => x.status == 'done');

    for (let todo of done_list) {
        let li = document.createElement('li');
        li.innerHTML = todo.text;
        // 添加到已完成列表中
        box.appendChild(li);
    }
}

function changeStatus(id, status) {
    // 根据选中与否，更改状态
    let todo_list = getTodoList();
    for (let todo of todo_list) {
        if (todo.id == id) {
            todo.status = status;
        }
    }
    localStorage.setItem('fubaitodo', JSON.stringify(todo_list));
    // 修改本地存储
}

function updateDoneStyle(todo, li) {
    console.log(todo, li, li.firstChild);
    // 载入时根据status添加样式
    if (todo.status == 'done'){
        li.style.textDecoration = 'line-through';
        li.firstElementChild.checked = true;
    } else {
        li.style.textDecoration = '';
        li.firstElementChild.checked = false;
    }
}

// 刷新页面初始化
init_todos();