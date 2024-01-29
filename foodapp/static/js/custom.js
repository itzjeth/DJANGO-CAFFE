(function ($) {

  "use strict";

    $(window).load(function(){
      $('.preloader').fadeOut(1000); // set duration in brackets    
    });

    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });

    $(window).scroll(function() {
      if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
          } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
          }
    });

    $(function() {
      $('.custom-navbar a, #home a').on('click', function(event) {
        var $anchor = $(this);
          $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
          }, 1000);
            event.preventDefault();
      });
    });  


    new WOW({ mobile: false }).init();

})(jQuery);


$(document).ready(function() {

        $('.card').delay(1800).queue(function(next) {
            $(this).removeClass('hover');
            $('a.hover').removeClass('hover');
            next();
        });
    });