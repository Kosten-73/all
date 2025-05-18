from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Можно добавить дополнительные поля, если нужно
    pass

    def __str__(self):
        return self.username
