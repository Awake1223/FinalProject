from http.client import responses
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import User
import os


# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def rating(request):
    users = User.objects.filter(id__gte=1, id__lte=100)  # Фильтруем по ID
    return render(request, 'app/rating.html', {'users': users})

def currency(request):
    return render(request, 'app/currency.html')

def profile(request):
    user_login = request.session.get('user_login')
    user = User.objects.filter(login=user_login).first()  # Перенаправляем на страницу профиля после сохранения
    return render(request, 'app/profile.html', {'user': user})

def edit_profile(request):
    user_login = request.session.get('user_login')
    user = User.objects.filter(login=user_login).first()  # Получаем текущего пользователя

    if request.method == 'POST':
        new_login = request.POST.get('login')
        if new_login:
            user.login = new_login

        # Проверяем, загружен ли новый аватар
        if request.FILES.get('avatar'):
            avatar_file = request.FILES['avatar']
            # Получаем расширение файла
            ext = os.path.splitext(avatar_file.name)[1].lower()  # Получаем расширение и приводим к нижнему регистру

            # Проверяем, является ли файл изображением с разрешенными расширениями
            if ext in ['.jpg', '.jpeg', '.png']:
                user.avatar = avatar_file  # Сохраняем загруженный файл
            else:
                # Если файл не подходит, можно вернуть ошибку или сообщение
                error_message = "Пожалуйста, загрузите изображение в формате JPG, JPEG или PNG."
                return render(request, 'app/edit_profile.html', {'user': user, 'error_message': error_message})

        # Если аватар не загружен, оставляем текущее значение
        user.save()  # Сохраняем изменения в модели
        return redirect('intro')  # Перенаправляем на страницу профиля после сохранения

    return render(request, 'app/edit_profile.html', {'user': user})

def login(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        currentUser = User.objects.filter(login=login).first()

        if currentUser:
            if check_password(password, currentUser.password):
                request.session['user_id'] = currentUser.id
                request.session['user_login'] = currentUser.login
                return redirect('profile')
            else:
                messages.error(request, "Пароль неверный.")
        else:
            messages.error(request, "Пользователь не найден")

    return render(request, 'app/login.html')

def registration(request):
    # Получаем логин из куки, если он существует
    login = request.COOKIES.get('login', '')

    if request.method == 'POST':
        # Получаем данные из формы
        login = request.POST.get('login')
        mail = request.POST.get('mailAdress')
        password = request.POST.get('password')
        passwordRepeat = request.POST.get('passwordRepeat')

        # Проверка на совпадение паролей
        if password != passwordRepeat:
            messages.error(request, "Пароли не совпадают!")
            return render(request, 'app/registration.html', {'login': login})  # Возвращаемся на страницу

        # Проверка на уникальность логина и email
        if User.objects.filter(login=login).exists():
            messages.error(request, "Логин уже занят!")
            return render(request, 'app/registration.html', {'login': login})  # Возвращаемся на страницу

        if User.objects.filter(mail=mail).exists():
            messages.error(request, "Email уже зарегистрирован!")
            return render(request, 'app/registration.html', {'login': login})  # Возвращаемся на страницу

        # Сохранение нового пользователя с хешированным паролем
        new_user = User(
            login=login,
            mail=mail,
            password=make_password(password)  # Хешируем пароль перед сохранением
        )
        new_user.save()
        messages.success(request, "Регистрация прошла успешно!")

        # Устанавливаем куки с логином и перенаправляем на страницу входа
        response = redirect('login')
        response.set_cookie('login', login, max_age=3600)  # Сохраняем логин в куки
        return response

    return render(request, 'app/registration.html', {'login': login})

def news(request):
    return render(request, 'app/news.html')

def intro(request):
    try:
        del request.session['user_id']
        del request.session['user_login']
    except KeyError:
        pass  # Если ключа нет, ничего не делаем
    return render(request, 'app/intro.html')