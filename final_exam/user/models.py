from django.db import models
from django.contrib.auth.models import AbstractUser


# Project's user roles.
class UserRoles(models.Model):
    role_name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователя'
        db_table = 'user_roles'

    def __str__(self):
        return f'{self.id}: {self.role_name}'


# Project's user model
class BookstoreUser(AbstractUser):
    bio = models.TextField(max_length=500, null=True, blank=True)
    roles = models.ForeignKey(to=UserRoles, on_delete=models.CASCADE, default=2)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
