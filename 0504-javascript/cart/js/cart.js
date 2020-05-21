function sumPrice(item) {
    // 改变商品数量时，同步更新单个商品的总金额
    // console.log(item);
    // console.log(item.id);
    let id = item.id.split('-')[2]
    let line = document.getElementById(`item-${id}`);

    let price_line = line.querySelector(`.item-price-${id}`);
    // console.log(price_line);
    let qty = item.value;
    let single_price = price_line.getAttribute('price');
    let sum_price = parseInt(qty) * parseFloat(single_price);

    price_line.firstElementChild.textContent = `￥${sum_price}`;
}

function checkItem(item) {
    // 选中商品行，改变此行的背景色，将金额加到总金额中
    console.log(item);
    let id = item.id.split('-')[2];
    let line = document.getElementById('item-' + id);

    line.style.backgroundColor = '';
    // 添加判断，勾选时改变背景颜色
    if (item.checked) {
        line.style.backgroundColor = 'yellowgreen';
    }

    let total_price = parseFloat(document.getElementsByClassName('total-price')[0].textContent.slice(1))

    let line_price = document.querySelector('.item-price-' + id);
    let price_sum = parseFloat(line_price.textContent.split('￥')[1]);
    console.log(price_sum, total_price);
    // 商品总金额由各个商品所用的金额相加
    if (item.checked) {
        total_price += price_sum;
    } else {
        total_price -= price_sum;
    }
    document.getElementsByClassName('total-price')[0].textContent = '￥' + total_price.toFixed(2)

    return total_price
}

function checkAll() {
    // 选中所有商品
    let all = document.getElementsByName('item-check');
    let btn_all = document.getElementById('check-all');
    document.getElementsByClassName('total-price')[0].textContent = '￥0.00'
    for (let a of all) {
        console.log(a);
        a.checked = btn_all.checked;
        if (a.checked) {
            checkItem(a);
        } else {
            let id = a.id.split('-')[2];
            let line = document.getElementById('item-' + id);
            // change bg color
            line.style.backgroundColor = '';
        }
    }
}

function deleteChecked(bAll = false) {
    // 删除选中的商品
    let all = document.getElementsByName('item-check');
    for (let a of all) {
        if (a.checked || bAll) {
            console.log('你要被删了');
            let id = a.id.split('-')[2];
            let line = document.getElementById('item-' + id);
            line.hidden = true
            line.previousElementSibling.hidden = true
            // 找到前面的同级元素
        }
    }
    document.getElementById('check-all').checked = false
    document.getElementsByClassName('total-price')[0].textContent = '￥0.00'
}

function paybtn() {
    // 弹出到新页面，显示价格
    console.log('结算选中商品');

    var doc = document.implementation.createHTMLDocument('Title');
    let pay_price = document.querySelector('.total-price').textContent;
    var p = doc.createElement('p');
    p.innerHTML = `<h1>总金额：${pay_price}<h1>`;
    doc.body.appendChild(p);

    document.replaceChild(
        doc.documentElement,
        document.documentElement
    );
    // createParagraph()
    // 备选方案：弹出窗口，显示总金额
}

function createParagraph() {
    // 创建一个新元素，显示总金额
    // 金额从total-price获取
    let pay_price = document.querySelector('.total-price').textContent;
    let para = document.createElement('div');
    let paraStyle = para.style;
    paraStyle.position = 'Fixed';
    paraStyle.top = '50%';
    paraStyle.left = '50%';
    paraStyle.backgroundColor = 'red';
    paraStyle.border = '1px solid greenyellow'
    paraStyle.color = 'white';
    paraStyle.height = '100px';
    paraStyle.weight = '200px';
    para.textContent = pay_price;
    document.body.appendChild(para);
}