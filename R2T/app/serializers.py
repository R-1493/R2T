from rest_framework.serializers import ModelSerializer
from .models import *


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
# class RoomMemberSerializer(ModelSerializer):
#     class Meta:
#         model = RoomMember
#         fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'