# Generated by Django 4.2.3 on 2023-07-19 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='owner',
            new_name='purchaser',
        ),
    ]
