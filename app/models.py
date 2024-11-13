from django.db import models

class User(models.Model):
    login=models.CharField('Логин', max_length=30)
    mail=models.EmailField('Почта')
    password=models.CharField('Пароль', max_length=128)