# Generated by Django 3.2.8 on 2021-11-24 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habibi', '0005_auto_20211124_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kiyimlar',
            name='category',
        ),
    ]
