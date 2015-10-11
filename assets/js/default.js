$(document).ready(function(){
    var current_id;
    var a_id;
    $.each($(".fk-popup"),function(index, val){
        current_id = val.attr('id');
        a_id = current_id + 'trigger' + index;
        $('<a href="#" class="fk-popup-btn" id="'+a_id+'">+</a>').insertAfter($(this));
    });
});