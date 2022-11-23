from django.db import models


class News(models.Model):
    objects = None
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Вступление')

    bode = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Разметка')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    delited = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def delete(self, *args, **kwargs):
        self.delete = True
        self.save()


class Course(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    delited = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def delete(self, *args, **kwargs):
        self.delete = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    delited = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.num} {self.title}'
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def delete(self, *args, **kwargs):
        self.delete = True
        self.save()


class CourseTeacher(models.Model):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    delited = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Курс к учителю'
        verbose_name_plural = 'Курсы к учителям'

    def delete(self, *args, **kwargs):
        self.delete = True
        self.save()