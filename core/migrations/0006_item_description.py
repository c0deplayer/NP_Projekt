# Generated by Django 3.1.7 on 2021-05-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210510_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description abcdefghijk'),
            preserve_default=False,
        ),
    ]