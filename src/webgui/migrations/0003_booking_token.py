# Generated by Django 3.1.2 on 2020-10-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0002_auto_20201008_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='token',
            field=models.CharField(blank=True, max_length=16, verbose_name='Token'),
        ),
    ]