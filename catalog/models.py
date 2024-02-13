from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование', null=False, blank=False)
    description = models.TextField(verbose_name='описание', default='скоро...', blank=False)
    preview = models.ImageField(upload_to='products/', verbose_name='превью', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='цена', default=0, blank=False)
    # manufactured_at = models.DateField(verbose_name='дата производства', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f"{self.name}, {self.description}, {self.category}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        