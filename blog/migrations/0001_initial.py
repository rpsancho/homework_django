# Generated by Django 4.2.10 on 2024-03-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='превью')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
        ),
    ]
