// cart.js
// author:fudamai
// power by jQuery

$(
    function sumPrice() {
        // 改变商品数量时，改变单个商品总价格
        $('input[name="price"]').on('click',
            // 监听click
            function () {
                // 获取商品数量
                let qty = $(this).val();
                // console.log($(this).val());
                // 剥离出商品的数字id
                let id = $(this).attr('id').split('-')[2];
                // console.log(id);

                // 找到商品的价格节点
                let price_line = $(`.item-price-${id}`);
                console.log(price_line);
                // 找到定义为节点属性的‘price’
                let unit_price = price_line.attr('price')
                // 计算这个商品的总金额
                let sum_price = parseInt(qty) * parseFloat(unit_price);
                // 用计算结果替换掉原金额文本
                price_line.children().text(`￥${sum_price}`);
            }
        )
    }
)

$(
    // 选中商品行是改变背景，进行结算
    // 获取所有商品行的checkbox节点，监听click事件
    $('input[name=item-check]').on('click',
        // 声明匿名函数用于调用checkItem函数
        // 规避作用域问题，将this指向匹配元素
        function () {
            checkItem(this)
        }
    )
)

$(
    function checkAll() {
        // 选中所有商品
        // 找到全选按钮
        $('input[name=check-all]').on('click',
            function () {
                // 获取全选按钮的状态
                let check_all = $(this).prop('checked');
                console.log(check_all);
                // 找到商品行的checkbox节点
                let item_check = $('input[name=item-check]')
                // 将商品总金额初始化
                $('.total-price').text('￥0.00');
                for (let a of item_check) {
                    if (check_all) {
                        // 设置商品行checkbox状态为选中
                        item_check.prop('checked', true);
                        // 修改结算金额
                        checkItem(a)
                    } else {
                        // 设置商品行状态checkbox为未选中
                        item_check.prop('checked', false);
                        // 获取商品行id
                        let id = $(a).attr('id').split('-')[2];
                        // 将商品行背景改为默认
                        $(`#item-${id}`).css('background', '');
                        console.log(id);
                    }
                }
            }
        )
    }
)

$(
    // 删除选中商品
    // 监听“删除选中商品”按钮的click事件
    $('.delete-choose').on('click',
        function () {
            deleteChecked()
        }
    )
)
$(
    // 清理购物车
    // 监听“清理购物车”按钮的click事件
    $('.delete-all').on('click',
        function () {
            deleteChecked(del_all = true)
        }
    )
)


$(
    $('.pay-btn').on('click',
        function () {
            // 弹出新页面，显示价格
            // 获取结算金额
            let total_price = $('.total-price').text();
            // 弹出窗口，显示结算金额
            window.alert(`结算金额：${total_price}`);
        }
    )
)

function deleteChecked(del_all = false) {
    // 删除选中的商品
    // 获取所有商品行的checkbox节点
    let all = $('input[name=item-check]');
    // 对商品行的checkbox进行迭代
    for (let a of all) {
        console.log(a);
        console.log($(a).prop('checked'));
        // 判断商品行checkbox的真假，或者是del_all参数的真假
        if ($(a).prop('checked') || del_all) {
            console.log('你要被删了');
            // 获取商品行id
            let id = $(a).attr('id').split('-')[2];
            // 获取商品行节点
            let line = $(`#item-${id}`);
            // 将商品行节点进行隐藏
            line.attr('hidden', true);
            // 将商品行上一个姊妹节点进行隐藏
            line.prev().attr('hidden', true);
        }
    }
    // 改变全选按钮的状态
    $('input[name=check-all]').prop('checked', false);
    // 将商品总金额初始化
    $('.total-price').text('￥0.00');
}

function checkItem(item) {
    // 选中商品行，改变此行的背景色，将金额加到总金额中
    console.log(item);
    // 获取商品行checkbox的状态
    let check_buy = $(item).prop('checked');
    // 找到并分离id
    let id = $(item).attr('id').split('-')[2];
    console.log(id);
    // 找到代表商品行的元素
    let line = $(`#item-${id}`);
    // click事件能否检测直接被改变checked的元素。不能
    // 获取总结算金额
    let total_price = parseFloat($('.total-price').text().slice(1));
    // 获取当前商品总金额
    let item_price = parseFloat($(`.item-price-${id}`).text().split('￥')[1]);
    console.log(total_price, item_price);
    if (check_buy) {
        // 改变商品行的背景
        line.css('background', 'greenyellow');
        // console.log($(this));
        // 将商品总金额添加到结算金额中
        total_price += item_price;
    } else {
        // 改变商品行的背景
        line.css('background', '');
        // 从结算金额中减去商品总金额
        total_price -= item_price;
    };
    // 总结算金额等于总结算金额加上商品总金额
    $('.total-price').text(`￥${total_price.toFixed(2)}`);
}