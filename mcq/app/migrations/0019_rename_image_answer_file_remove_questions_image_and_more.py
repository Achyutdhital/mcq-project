# Generated by Django 4.2.7 on 2023-12-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_answer_image_questions_categorie_questions_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='image',
            new_name='file',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='image',
        ),
        migrations.AddField(
            model_name='questions',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='file/'),
        ),
    ]
