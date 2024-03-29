from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'host', 'code', 'guest_can_pause', 'votes_to_skip', 'created_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'email', 'firstname', 'middlename', 'lastname')

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('administrator_id', 'email', 'firstname', 'middlename', 'lastname')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'title', 'publisher', 'publish_date', 'catalog', 'genre', 'status', 'shelf_no')

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthors
        fields = ('author', 'book')

class BookRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRent
        fields = ('user', 'book', 'lending_time')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'title', 'date', 'admin')

class EventHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHall
        fields = ('floor_no', 'room_id', 'max_occupancy', 'status')

class EventApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventApply
        fields = ('user', 'event')

class EventHeldSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHeld
        fields = ('room', 'event')

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('facilities', 'floorno', 'roomid')

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ('floorno')

class LendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lend
        fields = ('account', 'book')

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phonenumber', 'person')

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('floorno', 'seat_num', 'type', 'status')

class SeatBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatBook
        fields = ('user', 'sear_num', 'time')

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ('floor_no', 'shelf_no')

class StudyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyRoom
        fields = ('floor_no', 'room_id', 'max_occupancy', 'status', 'hastv')

class StudyroomBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyroomBook
        fields = ('user', 'room', 'floor_no', 'time')

