/**
 * Created by yang on 3/16/17.
 */

$(function () {
    trade_no = $("#order #trade_no").val();
    languagecode = $("#order #languageCode").val();
    querytrans = setInterval("gettransac()", 5000);


    $("#timeDiv").html("2:00:00");
    hour = 1;
    minute = 59;
    second = 59;
    timeLeft = setInterval("run()", 1000);
});


//get transaction status
function gettransac() {
    //ajax call
    $.post("/" + languagecode + "/order/ajax/check_transaction",
        {
            trade_no: trade_no,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        function (data) {
            var jsondata = eval(data);
            var status = jsondata['status'];
            if (status == '1') {
                clearInterval(querytrans);
                window.location = ("/" + languagecode + "/order/payment/success");
            }
        });
}

function run() {
        --second;
        if (second < 0) {
            --minute;
            second = 59;
        }
        if (minute < 0) {
            --hour;
            minute = 59
        }
        if (hour < 0) {
            second = 0;
            minute = 0;
        }
        $("#timeDiv").html(hour + ":" + minute + ":" + second);

        if (hour == 0 && minute == 0 && second == 0) {
            clearInterval(timeLeft);
            //we can cancel this order in back, but for convenience we keep this order since wechat will give the error message
            window.location = ("/" + languagecode + "/order/cart");
        }
    }
