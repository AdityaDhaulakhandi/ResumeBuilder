# Generated by Django 3.0.2 on 2021-08-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_resume_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='project',
            field=models.TextField(blank=True),
        ),
    ]