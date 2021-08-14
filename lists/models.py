from django.db import models


class List(models.Model):
    '''список'''
    def __str__(self):
        return('This is list object')

class Item(models.Model):
    '''элемент списка'''
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
