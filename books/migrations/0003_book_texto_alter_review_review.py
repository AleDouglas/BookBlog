# Generated by Django 4.1.7 on 2023-03-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='texto',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.CharField(max_length=800),
        ),
    ]