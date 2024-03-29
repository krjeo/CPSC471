# Generated by Django 5.0.3 on 2024-03-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Admin_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Email', models.CharField(default='', max_length=255)),
                ('FirstName', models.CharField(default='', max_length=255)),
                ('LastName', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
