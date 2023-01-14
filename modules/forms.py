# Настройка и валидация элементров формы.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

# Форма страницы Отзывы.
class ContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired(), Length(max=50)], render_kw={"placeholder": "Ваше Имя"})
    message = TextAreaField("Message", validators=[DataRequired(), Length(max=2000)], render_kw={"placeholder": "Ваш Отзыв"})
    submit = SubmitField("Отправить")
    
    
# Форма страницы Login.    
class ContactFormPass(FlaskForm):
    login = StringField("Login: ", validators=[DataRequired(), Length(max=20)], render_kw={"placeholder": "Your login"})
    password = PasswordField("Password", validators=[DataRequired(), Length(max=20)], render_kw={"placeholder": "Your password"})
    submit = SubmitField("Submit")
