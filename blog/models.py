from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug")
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(
        upload_to="blog/", verbose_name="превью", null=True, blank=True
    )
    creation_date = models.DateField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="признак публикации")
    views_count = models.IntegerField(default=0, verbose_name="количество просмотров")

    def __str__(self):
        return f"{self.title}, {self.content}, {self.views_count}"
