from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField


class ParentCategory(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=255)
  parentCategory_id = models.ForeignKey(ParentCategory, on_delete=CASCADE, null=True)

  def __str__(self):
    return self.name

class Items(models.Model):
  name = models.CharField(max_length=255)
  parentCategory_id = models.ForeignKey(ParentCategory, on_delete=CASCADE, null=True)
  category = models.ManyToManyField(Category, related_name='item')
  needed_furniture = models.CharField(max_length=255)
  needed_material = models.CharField(max_length=255)
  how_to_get = models.TextField()

  def __str__(self):
    return self.name





