from django.db import models
from companies.models import Company
# from accounts.models import User


class Team(models.Model):
    company = models.ForeignKey(Company, related_name='teams', on_delete=models.CASCADE)
    team_name = models.CharField(max_length=200)
    # leader = models.ForeignKey(User, related_name='led_teams', on_delete=models.SET_NULL, null=False)

    def __str__(self):
        return self.team_name
