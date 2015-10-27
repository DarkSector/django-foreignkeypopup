$(document).ready(function () {
    /******* Some global variables declared in limited scope ******/
    var host = window.location.protocol + '//' + window.location.hostname + (location.port ? ':'+location.port: '');
    var current_id;
    var a_id;
    var data_url;
    $.each($(".fk-popup"), function (index) {
        current_id = $(this).attr('id');
        a_id = current_id + '_fktrigger_' + index;
        data_url = $(this).attr('data-url');
        $('<a href="#" data-url="'+data_url+'" class="fk-popup-btn" id="' + a_id + '">+</a>').insertAfter($(this));
    });
    $(".fk-popup-btn").on("click", function(){
        // Any time the button gets triggered
        // open a new window and go to the link
        var childWin = window.open(host+$(this).attr('data-url'), '_blank', "toolbar=no, location=no, addressbar=no");
    });

    function addScript(jsFileNameWithPath){

    }
});