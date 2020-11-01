console.log('edit starting...');

$(function($) {
    $('#btn-edit-topic').click(function() {
        // let user = $('#topic-user');
        // console.log(user.text());
        if($(this).text() == '编辑'){
            $(this).text('更新');
            let input_text = $('#topic-text').text();
            let input = '<input id="topic-text-input" class="mx-2" type="text" value="' + input_text + ' ">'
            
            // let input = '<input id="topic-text-input" class="mb-0 lh-100" type="text" value="{{ topic.topic_text }}">'
            $('#topic-text').replaceWith(input);
        } else { // btn 更新
            $(this).text('编辑');
            console.log('更新数据...');
            // ajax post data
            // $.post("/topic", {
            $.post("/bbs/", {
                'pk': $('#topic-id').text(),
                'topic_text': $('#topic-text-input').val(),
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
            }, function(data){
                console.log('修改成功1');
                let h6 = '<h3 class="mx-2" id="topic-text">' + $('#topic-text-input').val() + '</h3>'
                $('#topic-text-input').replaceWith(h6);
                $(this).text('编辑');
            })
            // 修改页面
            console.log('修改成功2');

        }
    })
    
    // 把对象转为url
    // 把文件转成浏览器能认识的url
    function getObjectURL(file) {
        var url = null; 
        if (window.createObjectURL != undefined) { // basic
            url = window.createObjectURL(file);
        } else if (window.URL != undefined) { // mozilla(firefox)
            url = window.URL.createObjectURL(file);
        } else if (window.webkitURL != undefined) { // webkit or chrome
            url = window.webkitURL.createObjectURL(file);
        }
        return url;
    };
    
    // 预览图片
    // this.file[]，捕捉类型为file的input元素上传的文件
    $("#user_picture").change(function(){
        var objUrl = getObjectURL(this.files[0]);
        console.log("objUrl = "+ objUrl);
        if (objUrl) {
            $("#user_picture_img").attr("src", objUrl);
        }
    });

});