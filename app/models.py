from django.db import models

class Articles(models.Model):
    login=models.CharField('Логин', max_length=30)
    email=models.EmailField('Почта')
    password=models.CharField('Пароль', max_length=30)