// Слайдер для фотографий
jq13(document).ready(function() {
            jq13("a[rel=group]").fancybox({
                'transitionIn': 'none',
                'transitionOut': 'none',
                'titlePosition': 'over',

                'overlayShow': 'true',
                'overlayOpacity': 0.9,
                'overlayColor': '#000000',

                'titleFormat': function(title, currentArray, currentIndex, currentOpts) {
                    return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? '   ' + title : '') + '</span>';
                }
            });
        });
