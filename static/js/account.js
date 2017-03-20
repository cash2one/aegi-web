/**
 * Created by yang on 3/20/17.
 */

$(function () {


    verify_register_form('#signup_form');

    /* 注册页面验证 */
    function verify_register_form(myForm) {
        $(myForm).find('[type=text], [type=email], [type=password]').on({
            blur: function () {
                switch ($(this).attr('name')) {
                    case 'username' :
                        var _this = $(this);
                        if ($(this).val().length < 2 || $(this).val().length > 18) {
                            $("#username-msg").html("用户名长度不符合，请输入2-18位长度用户名");
                            $("#username-msg").removeClass("hide");
                            return;
                        }
                        else {
                            $.post('/account/ajax/check_username/',
                                {
                                    username: $(this).val()
                                }, function (result) {
                                    if (result.errno == -1) {
                                        $("#username-msg").html(result.err);
                                        $("#username-msg").removeClass("hide");
                                    }
                                    else {
                                        $("#username-msg").addClass("hide");
                                    }
                                }, 'json');
                        }
                        return;

                    case 'email' :
                        $(this).parent().find('.aw-reg-tips').detach();
                        var emailreg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
                        if (!emailreg.test($(this).val())) {
                            $(this).parent().find('.aw-reg-tips').detach();
                            $(this).parent().append('<span class="aw-reg-tips aw-reg-err"><i class="aw-icon i-err"></i>' + $(this).attr('errortips') + '</span>');
                            return;
                        }
                        else {
                            $(this).parent().find('.aw-reg-tips').detach();
                            $(this).parent().append('<span class="aw-reg-tips aw-reg-right"><i class="aw-icon i-followed"></i></span>');
                        }
                        return;

                    case 'password' :
                        $(this).parent().find('.aw-reg-tips').detach();
                        if ($(this).val().length >= 0 && $(this).val().length < 6) {
                            $(this).parent().find('.aw-reg-tips').detach();
                            $(this).parent().append('<span class="aw-reg-tips aw-reg-err"><i class="aw-icon i-err"></i>' + $(this).attr('errortips') + '</span>');
                            return;
                        }
                        if ($(this).val().length > 17) {
                            $(this).parent().find('.aw-reg-tips').detach();
                            $(this).parent().append('<span class="aw-reg-tips aw-reg-err"><i class="aw-icon i-err"></i>' + $(this).attr('errortips') + '</span>');
                            return;
                        }
                        else {
                            $(this).parent().find('.aw-reg-tips').detach();
                            $(this).parent().append('<span class="aw-reg-tips aw-reg-right"><i class="aw-icon i-followed"></i></span>');
                        }
                        return;

                }
            }
        });
    }
});