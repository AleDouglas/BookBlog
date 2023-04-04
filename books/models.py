from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid




class Category(models.Model):
    id = models.UUIDField(primary_key=True,db_index=True,default=uuid.uuid4,editable=False)
    title = models.CharField('Título',max_length=200)
    description = models.CharField('Descrição',max_length=400, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'], name='id_category')]

    def __str__(self):
        return self.title


class Book(models.Model): 
    id = models.UUIDField(primary_key=True,db_index=True,default=uuid.uuid4,editable=False) 
    created = models.DateField('Data de criação', auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categoria')
    title = models.CharField('Título',max_length=200)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    texto = models.TextField('Texto',blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'], name='id_index')]

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model): 
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    review = models.TextField('Comentário')
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.review
        

