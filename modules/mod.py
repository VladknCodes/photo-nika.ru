import mod_div


# Передача функции финального значения объединенных значений DIV из списка
def func_html(photos_mas, gal_adr):
    
    
    # Формирование объединенных значений DIV на основании требований списка фото.
    div_photo_block = []
    
    for i in range(0, len(photos_mas)):
           
        if len(photos_mas[i]) == 3: position = "Vert3"
        if len(photos_mas[i]) == 2: position = "Gor2"
        if (len(photos_mas[i]) == 3 and i == (len(photos_mas) - 1)): position = "Vert3_last"
        if (len(photos_mas[i]) == 2 and i == (len(photos_mas) - 1)): position = "Gor2_last"
        
      
        
        if position == "Vert3": div_photo_block.append(mod_div.vert3(gal_adr, photos_mas[i][0], photos_mas[i][1], photos_mas[i][2]))
        if position == "Gor2": div_photo_block.append(mod_div.goriz2(gal_adr, photos_mas[i][0], photos_mas[i][1]))
        if position == "Vert3_last": div_photo_block.append(mod_div.vert3_last(gal_adr, photos_mas[i][0], photos_mas[i][1], photos_mas[i][2]))
        if position == "Gor2_last": div_photo_block.append(mod_div.goriz2_last(gal_adr, photos_mas[i][0], photos_mas[i][1]))
    
    div_photo_block = [''.join(div_photo_block)]
    

    return div_photo_block[0]    