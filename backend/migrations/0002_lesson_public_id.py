# Generated by Django 4.2.4 on 2023-08-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='public_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
