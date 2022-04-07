from django.db import models


class Addresses(models.Model):
    address = models.TextField()


class Order(models.Model):
    address = models.TextField()
    description = models.TextField()
