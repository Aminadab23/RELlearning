# Generated by Django 4.2.4 on 2023-08-25 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktype',
            old_name='tyle',
            new_name='type',
        ),
    ]
