# Generated by Django 4.2.7 on 2023-12-03 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_is_correct_answer_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='categorie',
        ),
    ]
