# Generated by Django 4.2.8 on 2024-03-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0012_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='text1',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='home',
            name='text2',
            field=models.TextField(default='none'),
        ),
    ]