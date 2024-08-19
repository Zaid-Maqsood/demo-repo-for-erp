from django.db import models
from companies.models import Company


class Asset(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='assets', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
