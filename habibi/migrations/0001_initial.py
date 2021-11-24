# Generated by Django 3.2.8 on 2021-11-24 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Kiyimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('content', models.TextField(default='')),
                ('image', models.ImageField(upload_to='')),
                ('size', models.IntegerField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category', to='habibi.category')),
            ],
            options={
                'verbose_name': 'Kiyim',
                'verbose_name_plural': 'Kiyimlar',
                'ordering': ['name'],
            },
        ),
    ]
