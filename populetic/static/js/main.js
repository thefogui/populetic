$(document).ready(function() {
    $("#grab-btn").click(function(event) {
        var categories = []; //categories selected
        //Select all the input checked by the user
        i = 0;
        $.each($('input:checkbox').filter(':checked'), function(){            
            categories.push($(this).val().toUpperCase());
            console.log(categories[0]);
            i = i + 1;
        });
        
        $('.col-sm-4').each(function(i, ele) {
            $(this).hide();
            
            if(categories.includes(ele.getAttribute('id').toUpperCase())) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
});