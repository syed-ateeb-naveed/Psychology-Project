# Generated by Django 4.2.8 on 2024-03-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0024_alter_autostima_quiz_page_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='enduser_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='enduser_photos/')),
            ],
        ),
    ]