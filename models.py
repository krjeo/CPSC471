# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    administrator_id = models.IntegerField(db_column='Administrator_ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'


class ApiRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=8)
    host = models.CharField(unique=True, max_length=50)
    guest_can_pause = models.IntegerField()
    votes_to_skip = models.IntegerField()
    created_at = models.DateTimeField()
    stuff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_room'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=255)  # Field name made lowercase.
    publish_date = models.DateField(db_column='Publish_Date')  # Field name made lowercase.
    catalog = models.CharField(db_column='Catalog', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    shelf_no = models.ForeignKey('Shelf', models.DO_NOTHING, db_column='Shelf_No', to_field='Shelf_No')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class BookAuthors(models.Model):
    author = models.CharField(db_column='Author', primary_key=True, max_length=255)  # Field name made lowercase. The composite primary key (Author, book_id) found, that is not supported. The first column is selected.
    book = models.OneToOneField(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_authors'
        unique_together = (('author', 'book'),)


class BookRent(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Book_ID) found, that is not supported. The first column is selected.
    book = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_ID')  # Field name made lowercase.
    lending_time = models.DateField(db_column='Lending_Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book_rent'
        unique_together = (('user', 'book'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Event(models.Model):
    event_id = models.IntegerField(db_column='Event_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    admin = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='Admin_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event'


class EventHall(models.Model):
    floor_no = models.OneToOneField('Floor', models.DO_NOTHING, db_column='Floor_No', primary_key=True)  # Field name made lowercase. The composite primary key (Floor_No, Room_ID) found, that is not supported. The first column is selected.
    room_id = models.IntegerField(db_column='Room_ID', unique=True)  # Field name made lowercase.
    max_occupancy = models.IntegerField(db_column='Max Occupancy')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event hall'
        unique_together = (('floor_no', 'room_id'),)


class EventApply(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Event_ID) found, that is not supported. The first column is selected.
    event = models.OneToOneField(Event, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_apply'
        unique_together = (('user', 'event'),)


class EventHeld(models.Model):
    room = models.OneToOneField(EventHall, models.DO_NOTHING, db_column='Room_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Room_ID, Event_ID) found, that is not supported. The first column is selected.
    event = models.OneToOneField(Event, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_held'
        unique_together = (('room', 'event'),)


class Facilities(models.Model):
    facilities = models.CharField(db_column='Facilities', primary_key=True, max_length=255)  # Field name made lowercase. The composite primary key (Facilities, FloorNo, RoomID) found, that is not supported. The first column is selected.
    floorno = models.OneToOneField(EventHall, models.DO_NOTHING, db_column='FloorNo')  # Field name made lowercase.
    roomid = models.OneToOneField(EventHall, models.DO_NOTHING, db_column='RoomID', related_name='facilities_roomid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facilities'
        unique_together = (('facilities', 'floorno', 'roomid'),)


class Floor(models.Model):
    floorno = models.IntegerField(db_column='FloorNo', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'floor'


class Lend(models.Model):
    account = models.OneToOneField('User', models.DO_NOTHING, db_column='Account_ID', primary_key=True)  # Field name made lowercase. The composite primary key (Account_ID, Book_ID) found, that is not supported. The first column is selected.
    book = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lend'
        unique_together = (('account', 'book'),)


class Phone(models.Model):
    phonenumber = models.IntegerField(db_column='PhoneNumber', primary_key=True)  # Field name made lowercase. The composite primary key (PhoneNumber, Person_ID) found, that is not supported. The first column is selected.
    person = models.OneToOneField('User', models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone'
        unique_together = (('phonenumber', 'person'),)


class Seat(models.Model):
    floorno = models.OneToOneField(Floor, models.DO_NOTHING, db_column='FloorNo', primary_key=True)  # Field name made lowercase. The composite primary key (FloorNo, Seat_num) found, that is not supported. The first column is selected.
    seat_num = models.IntegerField(db_column='Seat_num', unique=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seat'
        unique_together = (('floorno', 'seat_num'),)


class SeatBook(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Sear_num) found, that is not supported. The first column is selected.
    sear_num = models.OneToOneField(Seat, models.DO_NOTHING, db_column='Sear_num')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seat_book'
        unique_together = (('user', 'sear_num'),)


class Shelf(models.Model):
    floor_no = models.OneToOneField(Floor, models.DO_NOTHING, db_column='Floor_No', primary_key=True)  # Field name made lowercase. The composite primary key (Floor_No, Shelf_No) found, that is not supported. The first column is selected.
    shelf_no = models.IntegerField(db_column='Shelf_No', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shelf'
        unique_together = (('floor_no', 'shelf_no'),)


class StudyRoom(models.Model):
    floor_no = models.OneToOneField(Floor, models.DO_NOTHING, db_column='Floor_No', primary_key=True)  # Field name made lowercase. The composite primary key (Floor_No, Room_ID) found, that is not supported. The first column is selected.
    room_id = models.IntegerField(db_column='Room_ID', unique=True)  # Field name made lowercase.
    max_occupancy = models.IntegerField(db_column='Max_Occupancy')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    hastv = models.IntegerField(db_column='HasTv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'study_room'
        unique_together = (('floor_no', 'room_id'),)


class StudyroomBook(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Room_ID, Floor_No) found, that is not supported. The first column is selected.
    room = models.OneToOneField(StudyRoom, models.DO_NOTHING, db_column='Room_ID')  # Field name made lowercase.
    floor_no = models.OneToOneField(StudyRoom, models.DO_NOTHING, db_column='Floor_No', related_name='studyroombook_floor_no_set')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studyroom_book'
        unique_together = (('user', 'room', 'floor_no'),)


class User(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        db_table_comment = 'Table for users in website'
