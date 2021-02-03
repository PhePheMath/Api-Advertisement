from django.db import models


class Enterprise(models.Model):
    name = models.CharField('Nome Fantasia', max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Nome Produto', max_length=120)
    enterprise = models.ForeignKey('enterprise.Enterprise', on_delete=models.NOT_PROVIDED)

    def __str__(self):
        return self.name
