# Generated by Django 4.2.8 on 2024-01-02 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0005_alter_quizresult_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionwithparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Partsofquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.questionwithparts')),
            ],
        ),
    ]
