from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
import datetime



class Category(models.Model):
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    max_length = 128

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    last_visit = models.TimeField()
    first_visit = models.TimeField()

    def _set_first_visit(self): self.first_visit = datetime.datetime.now()
    def _set_last_visit(self): self.last_visit = datetime.datetime.now()
    def _get_cat(self):return self.category

    def _get_link(self):return self.url

    def __str__(self):  # For Python 2, use __unicode__ too
        return self.title