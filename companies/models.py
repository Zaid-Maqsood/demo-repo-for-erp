from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    ceo = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
