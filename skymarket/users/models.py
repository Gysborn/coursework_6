from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    ROLE = [(USER, USER), (ADMIN, ADMIN)]


class User(AbstractBaseUser):
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    phone = PhoneNumberField(max_length=12)
    email = models.EmailField(verbose_name='Email Address', unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.ROLE, default=UserRoles.USER)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media_files/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]

    def __str__(self):
        return self.email


