from django.conf import settings
from django.db import models


class Ad(models.Model):
    image = models.ImageField(upload_to='media_files/', null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ad = models.ForeignKey(Ad, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
        ordering = ['-created_at']

    def __str__(self):
        return self.text
