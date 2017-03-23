/**
 * Created by yang on 3/20/17.
 */

$(function () {

    /*
     update the navbar status, based on the url pattern
     * */
    var position = window.location.pathname;
    var idx1 = position.indexOf('/', 1);
    var language = 'en';
    if (idx1 > 0) {
        language = position.substr(1, idx1 - 1);
    }

    //set language code
    if (language == 'en') {
        $("#en").addClass("active");
        $("#zh_cn").removeClass("active");

    } else {
        $("#zh_cn").addClass("active");
        $("#en").removeClass("active");
    }

    //set nav bar
    if (idx1 > 0) {
        var idx2 = position.indexOf('/', idx1 + 1);
        if (idx2 > 0) {
            var posName = position.substr(idx1 + 1, idx2 - idx1 - 1);
            $('#' + posName + '-nav').addClass('active');

        }
    }
});