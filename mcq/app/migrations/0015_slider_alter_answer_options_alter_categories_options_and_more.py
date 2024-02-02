# Generated by Django 4.2.7 on 2023-11-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_questions_set_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='sliderimage/')),
                ('text', models.CharField(blank=True, max_length=150, null=True)),
                ('order_number', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
                'ordering': ['order_number'],
            },
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['-order_number'], 'verbose_name': 'Question Bank', 'verbose_name_plural': "Question Bank's"},
        ),
        migrations.AlterModelOptions(
            name='purchases',
            options={'ordering': ['-id'], 'verbose_name': 'Purchase Question Set', 'verbose_name_plural': 'Purchases Question Sets'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['-id'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='questionsets',
            options={'ordering': ['order_number'], 'verbose_name': 'Question Set', 'verbose_name_plural': 'Question Sets'},
        ),
    ]
