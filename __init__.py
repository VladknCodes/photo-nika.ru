# photo-nika.ru
# Developed by Vladislav Kartashov
# 2023




import sys

sys.path.append(".....")

from flask import Flask, flash, render_template, request, session, redirect, url_for

# Обработка форм wtforms
from flask_script import Manager, Command, Shell
from forms import ContactForm, ContactFormPass


# Хеширования пароля
from werkzeug.security import generate_password_hash, check_password_hash



import datetime
import mysql.connector
import sqlalchemy

# Модули данных для фотографий
import mod

import index_data
import g1_data, g2_data, g3_data, g4_data
import children_data
import zhanr_portret_data

import data_log





app = Flask(__name__)
app.debug = True

# Установка секретного ключа Для обработки форм wtforms и сессий
app.config['SECRET_KEY'] = '.....'
manager = Manager(app)







# Работа с базой данных через SQLAlchemy - Начало
#-----------------------------------------------------------------------------------

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import GBase, GBook


# Страница отображения записей из БД GBmessageTMP

@app.route('/records/')
def showRecords():
    
    # Подключаемся и создаем сессию базы данных
    # engine = create_engine(f"mysql+mysqlconnector://{username}:{password_db}@{host}/{db_name}")
    engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(data_log.username, data_log.password_db, data_log.host, data_log.db_name))
    
    
    
    
    GBase.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session_db = DBSession()
    
    
    records = session_db.query(GBook).all()
    session_db.close()
    engine.dispose()
    
    return render_template("records.html", records=records)


# Работа с базой данных через SQLAlchemy - Конец
#-----------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------
# Страницы сайта - Начало
#-----------------------------------------------------------------------------------


@app.route('/')
def index():
    return render_template('photo_page.html', html_string = mod.func_html(index_data.photos_mas, index_data.gal_adr), title = "Главная страница")


@app.route('/children/')
def children():
    return render_template('photo_page.html', html_string = mod.func_html(children_data.photos_mas, children_data.gal_adr), title = "Дети")


@app.route('/zhanr_portret/')
def zhanr_portret():
    return render_template('photo_page.html', html_string = mod.func_html(zhanr_portret_data.photos_mas, zhanr_portret_data.gal_adr), title = "Жанровый портрет")
    
    

# Gallery - Начало
#---------------------------------------------------------------------------

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html', title = "Галерея")
    

@app.route('/gallery/g1/')
def g1():
    return render_template('photo_page.html', html_string = mod.func_html(g1_data.photos_mas, g1_data.gal_adr), title = "Галерея")
    
    
@app.route('/gallery/g2/')
def g2():
    return render_template('photo_page.html', html_string = mod.func_html(g2_data.photos_mas, g2_data.gal_adr), title = "Галерея")


@app.route('/gallery/g3/')
def g3():
    return render_template('photo_page.html', html_string = mod.func_html(g3_data.photos_mas, g3_data.gal_adr), title = "Галерея")


@app.route('/gallery/g4/')
def g4():
    return render_template('photo_page.html', html_string = mod.func_html(g4_data.photos_mas, g4_data.gal_adr), title = "Галерея")

# Gallery - Конец
#---------------------------------------------------------------------------    



@app.route('/conditions/')
def conditions():
    return render_template('conditions.html', title = "Условия")
    

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html', title = "Контакты")
    

#-----------------------------------------------------------------------------------
# Страницы сайта - Конец
#-----------------------------------------------------------------------------------







#-----------------------------------------------------------------------------------
# GB - Начало
#-----------------------------------------------------------------------------------

@app.route('/gb/', methods=['get', 'post'])
def gb():

# Чтение данных из таблицы GBmessageMain - Начало

    mydb = mysql.connector.connect(
    host = data_log.host,
    user = data_log.username,
    passwd = data_log.password_db,
    database = data_log.db_name
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM GBmessageMain ORDER BY id DESC")

    myresult = mycursor.fetchall()
    
    zn = []

    for x in myresult:
        zn.append(x)
        
    
    mydb.commit()
    mycursor.close()
    mydb.close()
    
# Чтение данных из таблицы GBmessageMain - Конец




# Работа с формой - Начало

# Запись данных в таблицу GBmessageTMP - Начало

    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data
        
        
        name = name[:50]
        name = name.replace("<", "&lt;")
        name = name.replace(">", "&gt;")
        name = name.replace("\r\n", "<br>")
        name = name.replace("\r", "<br>")
        name = name.replace("\n", "<br>")
        
        message = message[:2000]
        message = message.replace("<", "&lt;")
        message = message.replace(">", "&gt;")
        message = message.replace("\r\n", "<br>")
        message = message.replace("\r", "<br>")
        message = message.replace("\n", "<br>")
        
        
        daterec = datetime.datetime.today().strftime("%Y-%m-%d")
        
        mydb = mysql.connector.connect(
        host = data_log.host,
        user = data_log.username,
        passwd = data_log.password_db,
        database = data_log.db_name
        )
        
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO GBmessageTMP (name, DateMes, Message) VALUES (%s, %s, %s)"
        val = (name, daterec, message)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()

# Запись данных в таблицу GBmessageTMP - Конец

        print("\nData received. Now redirecting ...")
        flash("Благодарим Вас за отзыв, через некоторое время он появится на сайте...", "success")
        return redirect(url_for('gb'))
    return render_template('gb.html', form=form, records=zn, title = "Отзывы")
    
# Работа с формой - Конец

#-----------------------------------------------------------------------------------
# GB - Конец
#-----------------------------------------------------------------------------------






#-----------------------------------------------------------------------------------
# Login -Начало
#-----------------------------------------------------------------------------------

@app.route('/login/', methods=['get', 'post'])
def login():


# Записи из БД GBmessageTMP - Начало

    # Подключаемся и создаем сессию базы данных
    # engine = create_engine(f"mysql+mysqlconnector://{username}:{password_db}@{host}/{db_name}")
    engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(data_log.username, data_log.password_db, data_log.host, data_log.db_name))
    
    
    GBase.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session_db = DBSession()
    
    
    records = session_db.query(GBook).all()
    session_db.close()
    engine.dispose()

# Записи из БД GBmessageTMP - Конец 
    


# Работа с формой - Начало 


    form = ContactFormPass()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        
        log_ch = check_password_hash(data_log.log_hash, login)
        passw_ch = check_password_hash(data_log.passw_hash, password)
        
        
        if log_ch and passw_ch:
            session["login"] = True
        else:
            flashtxt = "Имя пользователя или пароль введены неверно"
            flash(flashtxt, "success")

        return redirect(url_for('login'))
    
    return render_template('login.html', form=form, title = "Login", records=records)
    
# Работа с формой - Конец


#-----------------------------------------------------------------------------------
# Login - Конец
#-----------------------------------------------------------------------------------



# Logout
#-----------------------------------------------------------------------------------
@app.route('/logout/')
def logout ():
    session.pop("login", None) # удаление сессии
    return redirect(url_for('login'))
    
    

    

# Удаления записи из БД GBmessageTMP - Начало
#-----------------------------------------------------------------------------------

@app.route('/login/<int:rec_id>/delete/', methods=['GET', 'POST'])
def deleterec(rec_id):
    
    if 'login' in session:
        
    
        engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(data_log.username, data_log.password_db, data_log.host, data_log.db_name))
        
        
        GBase.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session_db = DBSession()
        
        
        
        recToDelete = session_db.query(GBook).filter_by(id=rec_id).one()
        if request.method == 'POST':
            session_db.delete(recToDelete)
            session_db.commit()
            return redirect(url_for('login'))
        else:
            return render_template('deleterec.html', record=recToDelete)
    
        
        session_db.close()
        engine.dispose()
    
    
    
    else:
        return redirect(url_for('login'))

        
# Удаления записи из БД GBmessageTMP - Конец
#-----------------------------------------------------------------------------------






# Перемещение записи из БД GBmessageTMP в GBmessageMain - Начало
#-----------------------------------------------------------------------------------

@app.route('/login/<int:rec_id>/move/', methods=['GET', 'POST'])
def moverec(rec_id):
    
    if 'login' in session:
        
    
        engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(data_log.username, data_log.password_db, data_log.host, data_log.db_name))
        
        
        GBase.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session_db = DBSession()
        
        
        recToMove = session_db.query(GBook).filter_by(id=rec_id).one()
        
        if request.method == 'POST':
            
            mydb = mysql.connector.connect(
            host = data_log.host,
            user = data_log.username,
            passwd = data_log.password_db,
            database = data_log.db_name
            )
            
            
            mycursor = mydb.cursor()
            sql = "INSERT INTO GBmessageMain (Name, DateMes, Message) VALUES (%s, %s, %s)"
            val = (recToMove.name, recToMove.DateMes, recToMove.Message)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()
            mydb.close()
            
            
            
            session_db.delete(recToMove)
            session_db.commit()
            return redirect(url_for('login'))
        
        else:
            return render_template('move.html', record=recToMove)
    
        
        session_db.close()
        engine.dispose()
    
    
    
    else:
        return redirect(url_for('login'))
        

# Перемещение записи из БД GBmessageTMP в GBmessageMain - Конец
#-----------------------------------------------------------------------------------





# Обработка ошибок 404 и 500 - Начало
#-----------------------------------------------------------------------------------
# 404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404
 
# 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'),500

# Обработка ошибок 404 и 500 - Конец
#-----------------------------------------------------------------------------------






if __name__ == '__main__':
    app.run()
