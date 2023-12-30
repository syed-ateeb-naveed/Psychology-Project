# Generated by Django 4.2.2 on 2023-12-30 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civil_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('relationship', 'In a Relationship')], max_length=20)),
                ('occupation', models.CharField(max_length=100)),
                ('place_of_residence', models.CharField(max_length=400)),
                ('cellphone', models.CharField(max_length=20)),
                ('level_of_school', models.CharField(choices=[('elementary', 'Elementary/junior school'), ('high_school', 'High School'), ('bachelour', 'Bachelor’s degree'), ('master', 'Master')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
