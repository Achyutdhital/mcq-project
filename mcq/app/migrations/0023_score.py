# Generated by Django 4.2.7 on 2023-12-05 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0022_remove_questions_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('attempt_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_score', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Score',
                'verbose_name_plural': 'Scores',
            },
        ),
    ]
