# Generated by Django 5.1.1 on 2024-09-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20210326_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenModle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'TokenModle',
                'verbose_name_plural': 'TokenModle',
            },
        ),
    ]
