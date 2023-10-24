from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    username = models.CharField('ユーザー名',max_length=150, blank=True, null=True,
                                validators=[AbstractUser.username_validator])
    
    email = models.EmailField('メールアドレス', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    


# Create your models here.
