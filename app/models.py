from django.db import models

class User(models.Model):
    login=models.CharField('Логин', max_length=30)
    mail=models.EmailField('Почта')
    password=models.CharField('Пароль', max_length=128)
    avatar = models.FileField(upload_to='avatars/', blank=True, null=True)


class Stock(models.Model):
    name = models.CharField('Название компании', max_length = 30)
    price = models.DecimalField('Стоимость акции', max_digits=10, decimal_places=2)

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('USD', 'Доллары'),
        ('RUB', 'Рубли'),
        ('EUR', 'Евро'),
        ('AED', 'Дирхамы'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    account_type = models.CharField('Тип счета', max_length=3, choices=ACCOUNT_TYPES)
    balance = models.DecimalField('Баланс', max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.get_account_type_display()}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('BUY', 'Покупка акции'),
        ('OPEN', 'Открытие счета'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True, related_name='transactions')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='transactions')
    transaction_type = models.CharField('Тип транзакции', max_length=4, choices=TRANSACTION_TYPES)
    amount = models.DecimalField('Сумма', max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField('Время транзакции', auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_transaction_type_display()} - {self.amount}"

class Achievement(models.Model):
    name = models.CharField('Название достижения', max_length=100)
    description = models.TextField('Описание достижения')
    users = models.ManyToManyField(User, related_name='achievements')

    def __str__(self):
        return self.name