# Generated by Django 4.2.2 on 2023-07-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='media',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
