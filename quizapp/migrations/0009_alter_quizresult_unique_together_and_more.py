# Generated by Django 4.2.8 on 2024-02-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0008_alter_quizresult_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='quizresult',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='quizresult',
            constraint=models.UniqueConstraint(fields=('id', 'Category'), name='unique_id_category'),
        ),
    ]
