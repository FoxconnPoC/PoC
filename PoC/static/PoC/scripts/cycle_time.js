

$(document).ready(function () {

    var url = document.URL.split("?");
    $(".se-pre-con").hide();
    //$(".building_line").css("display", "none");

    $("a").click(function (e) {
        e.preventDefault();
        console.log(e.target.href);
        displayDetails(e.target.href);

    });

});


function displayDetails(url) {
    $(".se-pre-con").hide();
    var data = { csrftoken: getCookie('csrftoken') };
    $dump_in_me = undefined;
    if (url.indexOf("/line_detail/") >= 0){
        $dump_in_me = $("#Line_Detail");
    } if (url.indexOf("/sysserialno/") >= 0) {
        $dump_in_me = $("#SerialDetailResult");
    }

    //console.log(data);

    $.ajax({
        method: "GET",
        url: url,
        dataType: "text",
        contentType: "application/json; charset=utf-8",
        data: "",
        //data: JSON.stringify({}),

        success: function (response) {

            console.log(response);

            $dump_in_me.empty();
            $dump_in_me.html(response);

            $dump_in_me.find("a").click(function (e) {
                e.preventDefault();
                console.log(e.target.href);
                displayDetails(e.target.href);
            });
            
            $(".se-pre-con").hide();
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
            //console.log(error);
            $(".se-pre-con").hide();
        }
    });

}



function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

// usando jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}