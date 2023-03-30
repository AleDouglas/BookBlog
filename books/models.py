from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

class Book(models.Model): 
    id = models.UUIDField(primary_key=True,db_index=True,default=uuid.uuid4,editable=False) 
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', blank=True)
    texto = models.TextField(blank=True)
    class Meta:
        indexes = [models.Index(fields=['id'], name='id_index')]

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model): 
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    review = models.CharField(max_length=800)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.review