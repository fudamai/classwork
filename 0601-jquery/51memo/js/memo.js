// memo.js
// author: fudami
// power by jQuery

// 输入部分
// 抓取输入框的元素，保存，更新到页面中,addTodo
// 保存信息：备忘、完成状态（status）、优先级（important）、id
// 对输入备忘进行整形并添加到localStorage,addItem
// 将备忘填充到DOM树中,initTodos
// 
// 提取部分：打开页面自动提取部分、输入备忘自动添加部分
// 从localStorage 中提取所有备忘,getTodoList
// 获取备忘，分析备忘，根据优先级分成四类，调用填充到DOM的方法,initTodos
// 接收输入的备忘，根据分类生成不同的HTML代码，并填充到DOM树中,insertTodo
// 插入备忘时，完成状态不同样式不同,updateDoneStyle
// 将已完成备忘添加到完成列表中,updateDoneList
// 
// 备忘样式修改部分
// 选中时添加删除线，并修改进行状态，更新已完成列表，checkItem
// 根据选中与否，更改完成状态，保存,changeStatus
// 将已完成备忘添加到完成列表中,updateDoneList
// 
// 删除所有备忘,deleteAll

// TODO:完成计划，自动将其从今日计划移除。通过点击完成后调用页面提取部分，重新填充DOM。感觉体验不会好。


// 输入部分
$(
    // 找到添加按钮的节点，监控click事件
    $('input[type=submit]').on('click',
        function () {
            addTodo()
            console.log($(this));
        })
)

function addTodo() {
    // 抓取输入框的元素，保存，更新到页面中

    let todo = $('#new-item').val(); // 抓取备忘输入框的内容
    console.log(todo);
    let important = $('input[type="radio"]:checked').val()
    console.log(important); // 抓取备忘优先级信息
    // 备忘此时完成状态：todo
    addItem(todo, status = 'todo', important = important); // 将备忘保存到localStorage
    initTodos(); // 将备忘添加到DOM中
}

function addItem(memo, status = 'todo', important = 1) {
    // 对输入备忘进行整形并添加到localStorage

    let todo_list = []; // 声明一个空列表

    let old_list = localStorage.getItem('fubaitodo-1'); // 获取一个localStorage对象
    console.log(old_list);

    // 对旧备忘列表进行整形
    if (old_list) { // 判断是否有旧备忘

        todo_list = JSON.parse(old_list); // 对提取出的备忘进行整形，并赋值给todo_list
    }

    // 对待添加备忘进行整形
    let todo = {}; // 声明一个空对象，用于临时保存备忘信息
    todo.id = 1; // 指定一个默认id
    if (old_list) {
        // 如果存在旧备忘，新备忘的id是最后一个备忘id加上默认id
        todo.id += parseInt(todo_list[todo_list.length - 1].id);
    }
    todo.text = memo; // 将memo赋值给todo的text属性
    todo.status = status; // 将status赋值给todo的status属性
    todo.important = important; // 将important赋值给todo的important属性

    // 合并旧备忘与新备忘
    todo_list.push(todo)

    // 存储到localStorage，以json的格式
    localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));
    console.log(localStorage.getItem('fubaitodo-1'));
}

// 提取部分
$(
    // 打开页面时，调用此方法，自动填充页面
    initTodos()
)

function getTodoList() {
    // 从localStorage 中提取所有备忘
    return JSON.parse(localStorage.getItem('fubaitodo-1')); // 提取，整形，返回
}

function initTodos() {
    // 获取备忘，分析备忘，根据优先级分成四类，调用填充到DOM的方法
    let todo_list = getTodoList();// 获取已保存的备忘
    if (todo_list.length) {
        // console.log(todo_list);
        // 区分优先级important
        let fq_todos = todo_list.filter(x => x.important == 1);
        let sq_todos = todo_list.filter(x => x.important == 2);
        let tq_todos = todo_list.filter(x => x.important == 3);
        let foq_todos = todo_list.filter(x => x.important == 4);
        console.log(fq_todos, sq_todos, tq_todos, foq_todos);
        
        // 根据有限级不同，调用方法时给定不同的参数
        insertTodo(fq_todos)
        insertTodo(sq_todos, box_type = 'second-quadrant', html = '重要且紧急')
        insertTodo(tq_todos, box_type = 'third-quadrant', html = '紧急但不重要')
        insertTodo(foq_todos, box_type = 'fourth-quadrant', html = '不重要也不紧急')
        
        // 更改提示的类名，方便隐藏
        $('.todo-info').attr('class', 'todo-info hidden');
    }
    
    updateDoneList();// 调用方法，将已完成备忘添加到已完成列表
}

function insertTodo(todos, box_type = 'first-quadrant', html = '重要但不紧急') {
    // 接收输入的备忘，根据分类生成不同的HTML代码，并填充到DOM树中
    if (!todos.length) {
        // 对输入备忘集进行判断。如果长度为零，跳出循环
        return
    }
    let box = $(`#${box_type}`); // 根据box_type 参数获取节点
    // box.append(`<div class="todo-title">${html}</div>`);// 添加标题节点
    for (let todo of todos) { // 对备忘集进行迭代
        console.log(todo.status);
        if (todo.status == 'todo') {// 添加判断，只有status为todo的备忘插入到今日计划
            // 生成HTML代码并插入到DOM的指定节点中
            box.append(`<li><input type="checkbox" name="item" id=${todo.id}>${todo.text}</li>`);
            // 改变以完成备忘的样式
            updateDoneStyle(todo);
        }
    }
    
}

function updateDoneStyle(todo) {
    // 插入备忘时，完成状态不同样式不同
    if (todo.status == 'done') {
        // status为done，执行以下操作
        $(`#${todo.id}`).parent().css('textDecoration', 'line-through'); // 给备忘添加删除线样式
        $(`#${todo.id}`).prop('checked', true); // 备忘checkbox设为选中
    } else {
        // status不为done，执行以下操作
        $(`#${todo.id}`).parent().css('textDecoration', ''); // 备忘不设样式
        $(`#${todo.id}`).prop('checked', false); // 备忘checkbox设为不选
    }
}

function updateDoneList() {
    // 将已完成备忘添加到已完成列表中
    let box = $('#done-list');// 获取已完成列表节点
    box.html('');// 已完成列表设为空
    let done_list = getTodoList().filter(x => x.status == 'done');// 筛选出status为done的备忘

    for (let todo of done_list) {
        // 迭代已完成备忘，将每条备忘添加进已完成列表节点中
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
    let id = $(item).attr('id');// 声明一个变量用来保存备忘的id
    console.log(id);
    let bool = $(item).prop('checked');// 声明一个变量，用来保存备忘checkbox的真假
    console.log(bool);
    if (bool) {
        // checkbox值为真，执行以下操作
        console.log($(item).parent());
        $(item).parent().css('textDecoration', 'line-through');// 给备忘添加删除线样式
        changeStatus(id, 'done');// 改变备忘的完成状态
    } else {
        $(item).parent().css('textDecoration', '');// 给备忘添加删除线样式
        changeStatus(id, 'todo');// 改变备忘的完成状态

    }
    updateDoneList();// 调用方法，将已完成备忘添加到已完成列表
}

function changeStatus(id, status) {
    // 根据选中与否，更改完成状态，保存
    // 改变输入id对应备忘的完成状态
    let todo_list = getTodoList();// 获取所有的备忘
    for (let todo of todo_list) {
        if (todo.id == id) {
            // 备忘id与给定id相同时，执行以下操作
            todo.status = status;// 将备忘完成状态设为给定值
        }
    }
    localStorage.setItem('fubaitodo-1', JSON.stringify(todo_list));// 将修改后的备忘保存至localStorage中
}

// 删除所有备忘
$(
    // 找到“删除所有备忘按钮”，监听click事件
    $('.delete').on('click',
    function () {
        window.alert('删除所有备忘！');// 弹出提示窗口
        localStorage.clear();// 清除localStorage
        // initTodos();
        // 删除全部备忘后initTodos方法运行时报错。直接自动刷新页面。
        window.location.reload();// 刷新页面
    }
    )
)