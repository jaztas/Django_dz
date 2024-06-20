# Generated by Django 5.0.6 on 2024-06-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='человекопонятный URL')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blogpost/', verbose_name='изображение')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='дата записи')),
                ('publication_sign', models.BooleanField(default=True, verbose_name='публикация')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]
