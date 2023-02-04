// Прокрутка экрана вверх

jq13(document).ready(function(){
         
        jq13(window).scroll(function(){
        if (jq13(this).scrollTop() > 100) {
        jq13('.scrollup').fadeIn();
        } else {
        jq13('.scrollup').fadeOut();
        }
        });
         
        jq13('.scrollup').click(function(){
        jq13("html, body").animate({ scrollTop: 0 }, 400);
        return false;
        });
         
        });
