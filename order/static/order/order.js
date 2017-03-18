/**
 * Created by yang on 3/16/17.
 */
$(function () {

    $("input:radio[name=haveKit]").change(function () {
        if (this.value == '1') {
            $('.kit_id').removeClass("hide");
        }
        else {
            $('.kit_id').addClass("hide");
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

    $("input[id=number]").change(function () {
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

});

function checkForm() {

    $('#warning').modal('show');

    if (parseInt($("#id_number").val()) < 1) {
        $("$message").html("购买数量至少为1");
        $('#warning').modal('show');
        return false;
    }
    $('#warning').modal('show');
    if ($.trim($("#id_username").val()) == "") {
        $("$message").html("请输入用户名");
        $('#warning').modal('show');
        return false;
    }

    return false;

    var address = document.getElementById('address').value;
    if (address == "") {
        document.getElementById('address').style.color = "red";
        document.getElementById('address').style.borderColor = "red";
        document.getElementById('address').placeholder = "详细地址不能为空";
    }
    if (address != "") {
        document.getElementById('address').style.color = "black";
        document.getElementById('address').style.borderColor = "white";
        document.getElementById('address').placeholder = "详细地址";
    }
    if (document.getElementById('email').value.replace(/\ /g, "").search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/) == -1) {
        alert('输入正确的Email地址');
        return false;
    }
    if (document.getElementById('shouji').value.replace(/\ /g, "").search(/^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/) == -1) {
        alert('输入正确的手机号码');
        return false;
    }
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