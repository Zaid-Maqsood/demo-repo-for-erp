from django.db import models
from companies.models import Company
from teams.models import Team


class Project(models.Model):
    company = models.ForeignKey(Company, related_name='projects_company', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    start_time = models.DateField()
    end_time = models.DateField()
    project_status = models.BooleanField()
    team = models.ForeignKey(Team, related_name='projects_team', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name
