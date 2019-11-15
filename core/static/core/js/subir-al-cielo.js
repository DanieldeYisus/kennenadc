$(document).ready(function() {

    $('.up').hide();
    $(window).scroll(function() {
        if ($(this).scrollTop() > 500) {
            $('.up').slideDown(300);
        } else {
            $('.up').slideUp(300);
        }
    });
});