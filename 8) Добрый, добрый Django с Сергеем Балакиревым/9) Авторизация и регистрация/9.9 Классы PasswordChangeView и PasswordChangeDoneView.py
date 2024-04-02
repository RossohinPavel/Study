""" Упражнение 1
Подвиг 2. Объявите класс представления ProfilePasswordChange с базовым классом PasswordChangeView и следующими характеристиками:

через атрибуты класса:

стандартный класс формы изменения пароля;
шаблон: "profile/password_change_form.html";
перенаправление при успешном изменении пароля: reverse_lazy("password_change_done");
дополнительные переменные для шаблона: {'title': "Изменение пароля"}.
P.S. На экран ничего выводить не нужно.
"""
from django import forms
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.views import PasswordChangeView


# здесь продолжайте программуъ
class ProfilePasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "profile/password_change_form.html"
    success_url = reverse_lazy("password_change_done")
    extra_context = {'title': "Изменение пароля"}


""" Упражнение 2
Подвиг 3. Объявите класс формы ProfilePasswordChangeForm для смены пароля с базовым классом PasswordChangeForm и следующими характеристиками:

через атрибуты класса:

старый пароль: текстовое поле, название "Старый пароль", CSS-стили attrs={'class': 'form-input'};
новый пароль: поле ввода пароля, название "Новый пароль", CSS-стили attrs={'class': 'form-input'};
повтор пароля: поле ввода пароля, название "Подтверждение пароля", CSS-стили attrs={'class': 'form-input'}.
Атрибуты для полей ввода должны соответствовать базовой форме PasswordChangeForm. 

P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.forms import PasswordChangeForm
from django import forms

# здесь объявляйте класс ProfilePasswordChangeForm
class ProfilePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


""" Упражнение 3
Подвиг 4. Объявите класс представления LectorPasswordChange с базовым классом PasswordChangeView и следующими характеристиками:

через атрибуты класса:

класс формы: LectorPasswordChangeForm;
шаблон: "lector/password_change_form.html";
перенаправление при успешном изменении пароля: reverse_lazy("password_change_done");
дополнительные переменные для шаблона: {'title': "Изменение пароля"}.
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.views import PasswordChangeView
# from django.urls import reverse_lazy
# from .forms import LectorPasswordChangeForm


# здесь объявляйте класс LectorPasswordChange
class LectorPasswordChange(PasswordChangeView):
    form_class = LectorPasswordChangeForm
    template_name = "lector/password_change_form.html"
    success_url = reverse_lazy("password_change_done")
    extra_context = {'title': "Изменение пароля"}

    
""" Упражнение 4
Подвиг 5. Объявите класс представления CompanyPasswordChangeDone с базовым классом PasswordChangeDoneView и следующими характеристиками:

через атрибуты класса:

шаблон отображения: "company/password_change_done.html";
дополнительные переменные для шаблона: {'title': "Пароль изменен"}.
P.S. На экран ничего выводить не нужно.
"""
# from django.contrib.auth.views import PasswordChangeDoneView


# здесь объявляйте класс CompanyPasswordChangeDone
class CompanyPasswordChangeDone(PasswordChangeDoneView):
    template_name = "company/password_change_done.html"
    extra_context = {'title': "Пароль изменен"}

