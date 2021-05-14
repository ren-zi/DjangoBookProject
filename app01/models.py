from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64,null=False)
    address = models.CharField(max_length=64,null=False)


class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,null=False)
    address=models.CharField(max_length=64,null=False)


class Book(models.Model):
    id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=64,null=False)
    author = models.CharField(max_length=64,null=False)
    publisher = models.CharField(max_length=64,null=False)
    book_put_on = models.CharField(max_length=64, null=False)
    price = models.CharField(max_length=64, null=False)
    score = models.CharField(max_length=64, null=False)
    comment_num = models.CharField(max_length=64, null=False)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    password = models.CharField(max_length=64, null=False)