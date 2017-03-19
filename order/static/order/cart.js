/**
 * Created by yang on 3/16/17.
 */


var aegicare = {
    ajax_post: function (formOrder) //order page, submit
    {
        formOrder.ajaxSubmit(
            {
                dataType: 'json',
                success: function (result) {
                    var jsondata = eval(result);
                    var url = jsondata['url'];
                    if (url) {
                        if (window.location.href == url) {
                            window.location.reload();
                        }
                        else {
                            window.location = decodeURIComponent(url);
                        }
                    }
                },
                error: function (error) {
                    if ($.trim(error.responseText) != '') {
                        alert('发生错误, 错误信息:' + ' ' + error.responseText);
                    }
                }
            });
    },
}


$(function () {

    var languagecode = $("#languageCode").val();

    //address
    _init_area();

    $("input:radio[name=haveKit]").change(function () {
        if (this.value == '1') {
            $('.kit_id').removeClass("hide");
            $('.btn-submit').prop("disabled", true);
        }
        else {
            $('.kit_id').addClass("hide");
            $('.btn-submit').prop("disabled", false);
        }
    });

    $("input:radio[name=radioInvoice]").change(function () {
        if (this.value == '3') {
            $('.invoice_title').removeClass("hide");
        }
        else {
            $('.invoice_title').addClass("hide");
        }
    });

    $("input[name=number]").change(function () {
        var number = parseInt(this.value);
        var price = parseFloat($("#price").text());
        var total = price * number;
        var coupon = parseFloat($("#coupon").text());
        $("#totalPrice").html(total.toFixed(2));
        var final = total - coupon;
        $("#finalPrice").html(final.toFixed(2));

    })

    $(".pay_method").click(function () {
        $(".pay_method").removeClass("active");
        $(this).addClass("active");
        $(this).children("input").prop("checked", true);
    });

    // 提交订单
    $('.btn-submit').click(function () {


        if (parseInt($('#shopping-cart #id_number').val()) < 1) {
            modalAlert('购买数量至少为1!');
            return false;
        }

        if ($.trim($('#shopping-cart #id_username').val()) == "") {
            modalAlert('请输入联系人姓名!');
            return false;
        }

        var reg = /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;

        if (!reg.test($('#shopping-cart #id_email').val())) {
            modalAlert('请填写正确的邮箱地址!');
            return false;
        }

        if ($.trim($('#shopping-cart #id_phone').val()).length != 11) {
            modalAlert('请填写正确的手机号码!');
            return false;
        }

        if ($.trim($("#shopping-cart #id_province").val()) == "省份") {
            modalAlert('请选择省!');
            return false;
        }

        if ($.trim($("#shopping-cart #id_city").val()) == "地级市") {
            modalAlert('请选择市!');
            return false;
        }

        if ($.trim($("#shopping-cart #id_county").val()) == "市、县级市") {
            modalAlert('请选择市、县级市!');
            return false;
        }

        if ($.trim($("#shopping-cart #id_address").val()) == "") {
            modalAlert('请输入详细地址!');
            return false;
        }

        if ($('input:radio[name=radioInvoice]:checked').val() == '3') {
            if ($.trim($("#shopping-cart #id_invoice").val()) == "") {
                modalAlert('请提供发票抬头信息!');
                return false;
            }
        }

        aegicare.ajax_post($('#shopping-form'));
    });

    //kit id validation
    $("#shopping-cart .kitid-validation").click(function () {
        var kitids = $("#shopping-cart #id_kitId").val();
        $.get("/" + languagecode + "/order/validateKit", {kitid: kitids}, function (data) {
            var jsondata = eval(data);
            var status = jsondata['status'];
            var price = parseFloat(jsondata['price']);
            if (status == '0') {   //invalid
                $('.btn-submit').prop("disabled", true);
                modalAlert("采集管编码不存在，请联系客服!");
            } else {
                $('.btn-submit').prop("disabled", false);
                $("#shopping-cart #price").html(price.toFixed(2));

                var number = parseInt($("input[name=number]").val());
                var total = price * number;
                var coupon = parseFloat($("#coupon").text());

                $("#totalPrice").html(total.toFixed(2));
                var final = total - coupon;
                $("#finalPrice").html(final.toFixed(2));

                modalAlert("采集管编码有效!");
            }
        });
    });

});


//set the cookie for current page
function setcookie() {
    if ($.cookie('username')) {
        $('#shopping-cart #username').val($.cookie('username'));
    }
    if ($.cookie('email')) {
        $('#shopping-cart #email').val($.cookie('email'));
    }
    if ($.cookie('phone')) {
        $('#shopping-cart #phone').val($.cookie('phone'));
    }
    if ($.cookie('address')) {
        $('#shopping-cart #address').val($.cookie('address'));
    }
}


function modalAlert(message) {
    $("#message").html(message);
    $('#warning').modal('show');
}

mui.init({
    swipeBack: true //启用右滑关闭功能
});

/* coupon currently is not needed
 function aclick() {
 $("#coupon_number").toggle();
 if($(".glyphicon").hasClass("glyphicon-triangle-bottom")){
 $(".glyphicon").removeClass("glyphicon-triangle-bottom");
 $(".glyphicon").addClass("glyphicon-triangle-top");
 }else{
 $(".glyphicon").removeClass("glyphicon-triangle-top");
 $(".glyphicon").addClass("glyphicon-triangle-bottom");
 }
 }
 */