from django.db import models

# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('done', 'Done'),
        ('in progress', 'In Progress'),
    ]

    title = models.CharField('Название',max_length=100)
    task = models.TextField('Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # РАЗОБРАТЬ ЭТИ ЧАСТИ ПОЛНОСТЬЮ СУКА ()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

