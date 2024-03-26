""" Упражнение 1
Подвиг 3. Пусть имеется следующая функция представления для авторизации пользователей:

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginUserForm()
    return render(request, 'profile/login.html', {'form': form})
Необходимо ее заменить классом представления LoginProfile, унаследованным от базового класса LoginView, со следующим функционалом:

через атрибуты класса:

форма для авторизации: AuthenticationForm;
шаблон для отображения формы: 'profile/login.html';
дополнительные параметры: {'title': "Авторизация"};
через методы класса:

перенаправление при успешной авторизации по маршруту с именем 'home', используя функцию reverse_lazy.
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy

# здесь объявляйте класс LoginProfile
class LoginProfile(LoginView):
    form_class = AuthenticationForm
    template_name = 'profile/login.html'
    extra_context = {'title': "Авторизация"}
    
    def get_success_url(self):
        return reverse_lazy('home')


""" Упражнение 2
Подвиг 4. На основе базового класса AuthenticationForm объявите новый класс формы с именем UserLoginForm со следующими элементами:

через атрибуты класса:

username: текстовое поле ввода, максимум 100 символов, обязательное, наименование "Логин";
password: поле ввода пароля, максимум 50 символов, обязательное, наименование "Пароль".
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.forms import AuthenticationForm
from django import forms

# здесь объявляйте класс UserLoginForm
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label="Логин")
    password = forms.CharField(max_length=50, label="Пароль", widget=forms.PasswordInput())


""" Упражнение 3
Подвиг 5. На основе базового класса AuthenticationForm объявите новый класс формы с именем NewUserLoginForm со следующими элементами:

через атрибуты вложенного класса Meta:

модель формы: текущая модель пользователя, возвращенная функцией get_user_model();
отображаемые поля в форме авторизации: username, password.
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import get_user_model

# здесь объявляйте класс NewUserLoginForm
class NewUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

        
""" Упражнение 4
Подвиг 6. Объявите в программе класс формы авторизации LoginUserForm, унаследованный от базового класса AuthenticationForm со следующими элементами:

через атрибуты класса:

username: текстовое поле ввода, максимальная длина 100, название "Логин", стили attrs={'class': 'form-input'};
password: поле ввода пароля, максимальная длина 50, название "Пароль", стили attrs={'class': 'form-input'};
через атрибуты вложенного класса Meta:

модель формы: текущая модель пользователя, возвращенная функцией get_user_model();
отображаемые поля в форме авторизации: username, password.
Объявите класс представления LoginUser, унаследованный от базового класса LoginView, со следующими элементами:

через атрибуты класса:

форма для авторизации: LoginUserForm;
шаблон для отображения формы: 'users/login.html';
дополнительные параметры: {'title': "Авторизация пользователя"};
через методы класса:

перенаправление при успешной авторизации по маршруту с именем 'profile', используя функцию reverse_lazy.
P.S. На экран ничего выводить не нужно.
"""
# ------------------ forms.py -----------------------
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import get_user_model
from django import forms

# здесь объявляйте класс формы авторизации LoginUserForm
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=50, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

# ------------------ views.py -----------------------
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from .forms import LoginUserForm

# здесь объявляйте класс представления для авторизации LoginUser
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация пользователя"}
    
    def get_success_url(self):
        return reverse_lazy('profile')
