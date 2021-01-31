from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Tytuł')
    content = models.TextField(verbose_name='Treść')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Data')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))
