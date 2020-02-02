# Generated by Django 3.0.2 on 2020-02-01 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Comment'),
        ),
    ]