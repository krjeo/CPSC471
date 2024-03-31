# Generated by Django 5.0.3 on 2024-03-31 00:55

import api.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('administrator_id', models.IntegerField(db_column='Administrator_ID', primary_key=True, serialize=False)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('firstname', models.CharField(db_column='FirstName', max_length=255)),
                ('middlename', models.CharField(db_column='MiddleName', max_length=255)),
                ('lastname', models.CharField(db_column='LastName', max_length=255)),
            ],
            options={
                'db_table': 'administrator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=255)),
                ('publisher', models.CharField(db_column='Publisher', max_length=255)),
                ('publish_date', models.DateField(db_column='Publish_Date')),
                ('catalog', models.CharField(db_column='Catalog', max_length=255)),
                ('genre', models.CharField(db_column='Genre', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=255)),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BookAuthors',
            fields=[
                ('author', models.CharField(db_column='Author', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'book_authors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(db_column='User_ID', primary_key=True, serialize=False)),
                ('email', models.CharField(db_column='Email', max_length=255)),
                ('firstname', models.CharField(db_column='FirstName', max_length=255)),
                ('middlename', models.CharField(db_column='MiddleName', max_length=255)),
                ('lastname', models.CharField(db_column='LastName', max_length=255)),
            ],
            options={
                'db_table': 'user',
                'db_table_comment': 'Table for users in website',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(db_column='Event_ID', primary_key=True, serialize=False)),
                ('title', models.CharField(db_column='Title', max_length=255)),
                ('date', models.DateTimeField(db_column='Date')),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floorno', models.IntegerField(db_column='FloorNo', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'floor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('facilities', models.CharField(db_column='Facilities', max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'facilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('phonenumber', models.IntegerField(db_column='PhoneNumber', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'phone',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generate_unique_code, max_length=8, unique=True),
        ),
        migrations.CreateModel(
            name='BookRent',
            fields=[
                ('user', models.OneToOneField(db_column='User_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('lending_time', models.DateField(db_column='Lending_Time')),
            ],
            options={
                'db_table': 'book_rent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventApply',
            fields=[
                ('user', models.OneToOneField(db_column='User_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
            ],
            options={
                'db_table': 'event_apply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lend',
            fields=[
                ('account', models.OneToOneField(db_column='Account_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
            ],
            options={
                'db_table': 'lend',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeatBook',
            fields=[
                ('user', models.OneToOneField(db_column='User_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('time', models.DateTimeField(db_column='Time')),
            ],
            options={
                'db_table': 'seat_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudyroomBook',
            fields=[
                ('user', models.OneToOneField(db_column='User_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('time', models.DateTimeField(db_column='Time')),
            ],
            options={
                'db_table': 'studyroom_book',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventHall',
            fields=[
                ('floor_no', models.OneToOneField(db_column='Floor_No', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.floor')),
                ('room_id', models.IntegerField(db_column='Room_ID', unique=True)),
                ('max_occupancy', models.IntegerField(db_column='Max Occupancy')),
                ('status', models.CharField(db_column='Status', max_length=255)),
            ],
            options={
                'db_table': 'event hall',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('floorno', models.OneToOneField(db_column='FloorNo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.floor')),
                ('seat_num', models.IntegerField(db_column='Seat_num', unique=True)),
                ('type', models.CharField(db_column='Type', max_length=255)),
                ('status', models.CharField(db_column='Status', max_length=255)),
            ],
            options={
                'db_table': 'seat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('floor_no', models.OneToOneField(db_column='Floor_No', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.floor')),
                ('Shelf_no', models.IntegerField(db_column='Shelf_No', unique=True)),
            ],
            options={
                'db_table': 'shelf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudyRoom',
            fields=[
                ('floor_no', models.OneToOneField(db_column='Floor_No', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.floor')),
                ('room_id', models.IntegerField(db_column='Room_ID', unique=True)),
                ('max_occupancy', models.IntegerField(db_column='Max_Occupancy')),
                ('status', models.CharField(db_column='Status', max_length=255)),
                ('hastv', models.IntegerField(db_column='HasTv')),
            ],
            options={
                'db_table': 'study_room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EventHeld',
            fields=[
                ('room', models.OneToOneField(db_column='Room_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.eventhall')),
            ],
            options={
                'db_table': 'event_held',
                'managed': False,
            },
        ),
    ]