# Generated by Django 4.2.8 on 2024-03-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0016_alter_home_page_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='how_does_it_work_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Cómo funciona Page (frontend)',
            },
        ),
    ]
