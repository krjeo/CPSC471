from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code = code).count() ==0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add = True)

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

class Administrator(models.Model):
    administrator_id = models.IntegerField(db_column='Administrator_ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=255)  # Field name made lowercase.
    publish_date = models.DateField(db_column='Publish_Date')  # Field name made lowercase.
    catalog = models.CharField(db_column='Catalog', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    shelf_no = models.ForeignKey('Shelf', models.DO_NOTHING, db_column='Shelf_No', to_field='Shelf_no')  # Field name made lowercase.

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
    Shelf_no = models.IntegerField(db_column='Shelf_No', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shelf'
        unique_together = (('floor_no', 'Shelf_no'),)


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