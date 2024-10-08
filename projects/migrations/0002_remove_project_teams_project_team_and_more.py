# Generated by Django 5.0.6 on 2024-08-16 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('projects', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='teams',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_team', to='teams.team'),
        ),
        migrations.AlterField(
            model_name='project',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_company', to='companies.company'),
        ),
    ]
