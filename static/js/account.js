/**
 * Created by yang on 3/20/17.
 */

$(function () {

    var languagecode = $("#languageCode").val();

    verify_register_form('#signup_form');

    /* 注册页面验证 */
    function verify_register_form(myForm) {
        $(myForm).find('[type=text], [type=email], [type=password]').on({
            blur: function () {
                switch ($(this).attr('name')) {
                    case 'username' :
                        var _this = $(this);
                        $("#username-msg").addClass("hide");
                        var username = $.trim($(this).val());
                        if (username.length < 2 || username.length > 18) {
                            $("#username-msg").html("用户名长度不符合，请输入2-18位长度用户名");
                            $("#username-msg").removeClass("hide");
                            return;
                        }

                        var ascii = /^[ -~]+$/;
                        if (!ascii.test(username)) {
                            $("#username-msg").html("用户名只能包含英文字母，数字和@.+-_字符");
                            $("#username-msg").removeClass("hide");
                            return
                        }
                        else {
                            $.post("/" + languagecode + '/accounts/ajax/checkUsername/',
                                {
                                    username: $(this).val(),
                                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                                }, function (result) {
                                    var jsondata = eval(result);
                                    if (jsondata['isExist'] == 1) {
                                        $("#username-msg").html("该用户名已经注册");
                                        $("#username-msg").removeClass("hide");
                                    }
                                }, 'json');
                        }
                        return;

                    case
                    'email'
                    :
                        $("#email-msg").addClass("hide");
                        var emailreg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
                        if (!emailreg.test($(this).val())) {
                            $("#email-msg").html("请输入正确的邮箱地址，参考格式example@example.com");
                            $("#email-msg").removeClass("hide");
                            return;
                        }
                        return;

                    case
                    'password1'
                    :
                        $("#password1-msg").addClass("hide");
                        if ($(this).val().length >= 0 && $(this).val().length < 6) {
                            $("#password1-msg").html("密码位数至少为6");
                            $("#password1-msg").removeClass("hide");
                            return;
                        }
                        return;

                    case
                    'password2'
                    :
                        $("#password2-msg").addClass("hide");
                        if ($(this).val() != $("input[name=password1]").val()) {
                            $("#password2-msg").html("密码不一致");
                            $("#password2-msg").removeClass("hide");
                            return;
                        }
                        return;

                }
            }
        });
    }
});