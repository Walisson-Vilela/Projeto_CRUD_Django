# Generated by Django 3.1 on 2020-08-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200830_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='apelido',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]