from django.db import models
from django.template.defaultfilters import slugify
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
'''
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
'''


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    url = models.URLField()
    quality = models.PositiveSmallIntegerField(default=1)
    views = models.IntegerField(default=0)
    likes=models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Tachymeter(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    name =models.CharField(max_length=128)
    url = models.URLField()
    quality = models.PositiveSmallIntegerField(default=1)
    views = models.IntegerField(default=0)
    likes=models.IntegerField(default=0)

    def __unicode__(self):
        return self.title