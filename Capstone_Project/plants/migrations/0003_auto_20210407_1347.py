# Generated by Django 3.1.7 on 2021-04-07 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20210405_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='labels',
            new_name='label',
        ),
    ]