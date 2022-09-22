function bindCaptchaBtnClick() {
    $("#captcha-btn").on('click', function (event) {
        var $this = $(this);
        var email = $("input[name='email']").val();
        if (!email) {
            alert('请先输入邮箱！');
            return;
        }
        $.ajax({
            url: '/user/mail',
            method: "POST",
            data: {
                "email": email
            },
            success: function (res) {
                if (res['code'] === 200) {
                    // 取消点击事件
                    $this.off('click');
                    var countDown = 60;
                    var timer = setInterval(()=>{
                        if(countDown>=0){
                            $this.text(countDown+"秒后重新发送");
                        }else{
                            $this.text('获取验证码');
                            // 重新绑定点击事件
                            bindCaptchaBtnClick();
                            // 清除倒计时
                            clearInterval(timer);
                        }
                        countDown -= 1;
                    },1000)
                    alert('验证码发送成功')
                } else {
                    alert(res['message'])
                }
            }
        });
    })
}

$(function () {
    bindCaptchaBtnClick();
})