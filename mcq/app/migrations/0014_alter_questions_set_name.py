# Generated by Django 4.2.7 on 2023-11-21 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_questions_question_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='set_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_set_name', to='app.questionsets'),
        ),
    ]
