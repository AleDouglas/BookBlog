from django.contrib.auth.models import AbstractUser
from django.db import models

class BadgeUser(models.Model):
    title = models.CharField('Títlo da Badge', max_length=40)
    badgeIMG = models.ImageField('Badge',upload_to='badge/', blank=True)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    bio = models.TextField('Biografia',max_length=500, blank=True)
    birth_date = models.DateField('Data de aniversário',null=True, blank=True)
    perfilIMG = models.ImageField('Imagem do perfil',upload_to='perfil/', blank=True)
    badge = models.ForeignKey(BadgeUser,on_delete=models.CASCADE, related_name='badge', blank=True, null=True, default=1)