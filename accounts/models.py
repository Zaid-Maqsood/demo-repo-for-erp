from django.db import models
from teams.models import Team
from companies.models import Company


class User(models.Model):
    TYPE_CHOICES = [
        ('HR', 'Human Resource'),
        ('BD', 'Business Development'),
        ('SE', 'Software Developer'),
        ('QA', 'Quality Assurance'),
        ('PM', 'Product Manager'),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    date_of_join = models.DateField()
    team = models.ForeignKey(Team, related_name='user_team', default=None, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



