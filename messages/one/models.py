from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Ticket(models.Model):
    id = models.SlugField('id', primary_key=True)
    title = models.CharField('Тема обращения', max_length=120)
    mess = models.TextField('Вопрос')
    name = models.ForeignKey(User, verbose_name='Имя пользователя', on_delete=models.CASCADE)
    mail = models.CharField('Почта', max_length=120)
    load = models.FileField('Файл от пользователя', default='default.txt', upload_to='users_files')
    date = models.DateTimeField('Дата', default=timezone.now)

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
