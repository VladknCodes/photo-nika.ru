# Модуль формирования HTML блоков с требованиями по количеству и расположению фотографий.

#   Функция генерации вертикальных фото по 3 шт.

def vert3(gal_adr, f1, f2,f3):
    
    href_var_1 = gal_adr + str(f1) +".jpg"
    scr_var_1 = gal_adr + str(f1) +"s.jpg"
    
    href_var_2 = gal_adr + str(f2) +".jpg"
    scr_var_2 = gal_adr + str(f2) +"s.jpg"
    
    href_var_3 = gal_adr + str(f3) +".jpg"
    scr_var_3 = gal_adr + str(f3) +"s.jpg"
    
    
    ver3_txt = []
    
    ver3_txt.append('\n\n<!-- Вставка фото-блока vert3 -->\n\n')
    ver3_txt.append('<div class="container">\n')
    ver3_txt.append('\t<a rel="group" href="%s"><img class="breakpoint1" style="float: left;" src="%s" width="440" height="660" /></a>\n' % (href_var_1, scr_var_1))
    ver3_txt.append('\t<div class="block1"></div>\n')
    ver3_txt.append('\t<a rel="group" href="%s"><img class="breakpoint1" style="float: left;" src="%s" width="440" height="660" /></a>\n' % (href_var_2, scr_var_2))
    ver3_txt.append('\t<div class="block1"></div>\n')
    ver3_txt.append('\t<a rel="group" href="%s"><img class="breakpoint1" src="%s" width="440" height="660" /></a>\n' % (href_var_3, scr_var_3))
    ver3_txt.append('\t<div class="block2"></div>\n')
    ver3_txt.append('</div>\n\n')
    ver3_txt.append('<!-- End Вставка фото-блока vert3 -->\n\n')
    
    ver3_txt = [''.join(ver3_txt)]
    
    return ver3_txt[0]
    


#   Функция генерации горизонтальных фото по 2 шт.

def goriz2(gal_adr, f1, f2):
    
    href_var_1 = gal_adr + str(f1) +".jpg"
    scr_var_1 = gal_adr + str(f1) +"s.jpg"
    
    href_var_2 = gal_adr + str(f2) +".jpg"
    scr_var_2 = gal_adr + str(f2) +"s.jpg"
    
    
    goriz2_txt = []
    
    goriz2_txt.append('\n\n<!-- Вставка фото-блока goriz2 -->\n\n')
    goriz2_txt.append('<div class="container">\n')
    goriz2_txt.append('\t<a rel="group" href="%s"><img class="breakpoint2" style="float: left;" src="%s" width="680" height="454" /></a>\n' % (href_var_1, scr_var_1))
    goriz2_txt.append('\t<div class="block1"></div>\n')
    goriz2_txt.append('\t<a rel="group" href="%s"><img class="breakpoint2" src="%s" width="680" height="454" /></a>\n' % (href_var_2, scr_var_2))
    goriz2_txt.append('\t<div class="block2"></div>\n')
    goriz2_txt.append('</div>\n\n')
    goriz2_txt.append('<!-- End Вставка фото-блока goriz2 -->\n\n')
    
    
    goriz2_txt = [''.join(goriz2_txt)]
    
    return goriz2_txt[0]



#   Функция генерации вертикальных фото по 3 шт. Last.

def vert3_last(gal_adr, f1, f2,f3):
    
    href_var_1 = gal_adr + str(f1) +".jpg"
    scr_var_1 = gal_adr + str(f1) +"s.jpg"
    
    href_var_2 = gal_adr + str(f2) +".jpg"
    scr_var_2 = gal_adr + str(f2) +"s.jpg"
    
    href_var_3 = gal_adr + str(f3) +".jpg"
    scr_var_3 = gal_adr + str(f3) +"s.jpg"
    
    
    ver3_last_txt = []
    
    
    ver3_last_txt.append('\n\n<!-- Вставка фото-блока vert3_last -->\n\n')
    ver3_last_txt.append('<div class="container">\n')
    ver3_last_txt.append('\t<a rel="group" href="%s"><img class="breakpoint1" style="float: left;" src="%s" width="440" height="660" /></a>\n' % (href_var_1, scr_var_1))
    ver3_last_txt.append('\t<div class="block1"></div>\n')
    ver3_last_txt.append('\t<a rel="group" href="%s"><img class="breakpoint1" style="float: left;" src="%s" width="440" height="660" /></a>\n' % (href_var_2, scr_var_2))
    ver3_last_txt.append('\t<div class="block1"></div>\n')
    ver3_last_txt.append('\t<a rel="group" href="%s"><img class="breakpoint1" src="%s" width="440" height="660" /></a>\n' % (href_var_3, scr_var_3))
    ver3_last_txt.append('\t<!-- Вставка последнего фото блока без class="block2" -->\n')
    ver3_last_txt.append('</div>\n\n')
    ver3_last_txt.append('<!-- End Вставка фото-блока vert3_last -->\n\n')
    
    ver3_last_txt = [''.join(ver3_last_txt)]
    
    return ver3_last_txt[0]
    


#   Функция генерации горизонтальных фото по 2 шт. Last.
   
def goriz2_last(gal_adr, f1, f2):
    
    href_var_1 = gal_adr + str(f1) +".jpg"
    scr_var_1 = gal_adr + str(f1) +"s.jpg"
    
    href_var_2 = gal_adr + str(f2) +".jpg"
    scr_var_2 = gal_adr + str(f2) +"s.jpg"
    
    
    goriz2_last_txt = []
    
    goriz2_last_txt.append('\n\n<!-- Вставка фото-блока goriz2_last -->\n\n')
    goriz2_last_txt.append('<div class="container">\n')
    goriz2_last_txt.append('\t<a rel="group" href="%s"><img class="breakpoint2" style="float: left;" src="%s" width="680" height="454" /></a>\n' % (href_var_1, scr_var_1))
    goriz2_last_txt.append('\t<div class="block1"></div>\n')
    goriz2_last_txt.append('\t<a rel="group" href="%s"><img class="breakpoint2" src="%s" width="680" height="454" /></a>\n' % (href_var_2, scr_var_2))
    goriz2_last_txt.append('\t<!-- Вставка последнего фото блока без class="block2" -->\n')
    goriz2_last_txt.append('</div>\n\n')
    goriz2_last_txt.append('<!-- End Вставка фото-блока goriz2_last -->\n\n')
    
    
    goriz2_last_txt = [''.join(goriz2_last_txt)]
    
    return goriz2_last_txt[0]