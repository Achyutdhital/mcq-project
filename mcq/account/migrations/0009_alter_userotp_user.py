# Generated by Django 4.2.7 on 2023-12-03 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_userotp_otp_code_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_otp', to=settings.AUTH_USER_MODEL),
        ),
    ]