# Generated by Django 4.2.8 on 2024-03-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0022_anxiety_autostima_depression_oriention_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anxiety_quiz_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('disclaimer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Anxiety quiz Page (frontend)',
            },
        ),
        migrations.CreateModel(
            name='Autostima_quiz_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('disclaimer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Autostima quiz Page (frontend)',
            },
        ),
        migrations.CreateModel(
            name='Depression_quiz_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('disclaimer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Depression quiz Page (frontend)',
            },
        ),
        migrations.CreateModel(
            name='Oriention_quiz_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('disclaimer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Oriention quiz Page (frontend)',
            },
        ),
    ]
