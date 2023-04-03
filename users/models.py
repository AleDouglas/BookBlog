from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    bio = models.TextField('Biografia',max_length=500, blank=True)
    birth_date = models.DateField('Data de aniversário',null=True, blank=True)
    perfilIMG = models.ImageField('Imagem do perfil',upload_to='perfil/', blank=True)