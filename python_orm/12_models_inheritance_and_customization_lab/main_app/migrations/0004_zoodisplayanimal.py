# Generated by Django 5.0.4 on 2024-11-25 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_speciality_zookeeper_specialty'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZooDisplayAnimal',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.animal',),
        ),
    ]