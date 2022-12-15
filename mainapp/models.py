from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')

    deleted = models.BooleanField(default=False, verbose_name='Удален')

    class Meta:
        abstract = True
        ordering = ('-created_at')

    def delete(self, *args, **kwargs):
        self.delete = True
        self.save()


class NewsManager(models.Manager):
    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(BaseModel):
    # objects = NewsManager()
    title = models.CharField(max_length=256, verbose_name=_('Заголовок'))
    preamble = models.CharField(max_length=1024, verbose_name=_('Вступление'))

    bode = models.TextField(verbose_name=_('Содержимое'))
    body_as_markdown = models.BooleanField(default=False, verbose_name=_('Разметка'))

    def __str__(self):
        return f'#{self.pk}{self.title}'

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')


class Course(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return f'{self.pk}{self.title}'
    class Meta:
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.pk} {self.title}'
    class Meta:
        verbose_name = _('Урок')
        verbose_name_plural = _('Уроки')


class CourseTeacher(BaseModel):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    created_at = models.DateTimeField(auto_now_add=True, null=True,  verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Курс к учителю')
        verbose_name_plural = _('Курсы к учителям')


class CourseFeedback(BaseModel):
    RATING_FIVE = 5

    RATINGS = (
        (RATING_FIVE, '⭐⭐⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (3, '⭐⭐⭐'),
        (2, '⭐⭐'),
        (1, '⭐'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.SmallIntegerField(choices=RATINGS, default=5, verbose_name='Рейтинг')
    feedback = models.TextField(verbose_name='Отзыв', default='Без отзыва')

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return f'Отзыв на {self.course} от {self.user}'

