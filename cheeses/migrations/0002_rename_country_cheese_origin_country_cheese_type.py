# Generated by Django 4.2.5 on 2023-09-19 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheese',
            old_name='country',
            new_name='origin_country',
        ),
        migrations.AddField(
            model_name='cheese',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
