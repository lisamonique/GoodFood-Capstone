# Generated by Django 3.1.7 on 2021-04-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='labels',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]