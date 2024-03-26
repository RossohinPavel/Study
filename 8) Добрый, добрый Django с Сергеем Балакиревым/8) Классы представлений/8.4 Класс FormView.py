""" Упражнение 1
Подвиг 4. Пусть имеется следующая функция представления:

from django.views.generic.edit import FormView
# from .forms import AddSubjectForm

def add_subject(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddSubjectForm()

    return render(request, 'subject/addsubject.html', {'title': 'Добавление предмета', 'form': form})
Замените эту функцию классом представления с именем AddSubject, унаследованным от базового класса FormView, со следующим функционалом:

через атрибуты класса:

используемый шаблон: 'subject/addsubject.html';
класс формы: AddSubjectForm;
URL-перенаправления (после успешной обработки формы): reverse_lazy('home');
дополнительные переменные для шаблона: {'title': "Добавление предмета"}.
через методы класса:

form_valid: выполнить сохранение данных формы в БД (используя для этого специальный метод формы, связанной с моделью).
P.S. На экран ничего выводить не нужно.
"""
# --------- models.py ------------------------
from django.views.generic.edit import FormView
# from .forms import AddSubjectForm
# from django.urls import reverse_lazy

# здесь объявляйте класс представления
class AddSubject(FormView):
    form_class = AddSubjectForm
    template_name = 'subject/addsubject.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': "Добавление предмета"}
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
