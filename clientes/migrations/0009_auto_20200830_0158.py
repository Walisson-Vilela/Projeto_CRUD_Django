# Generated by Django 3.1 on 2020-08-30 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_person_data_nascimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='bio',
            new_name='observacao',
        ),
    ]